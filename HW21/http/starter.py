from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import socket


def url_decode(input: str | None) -> str | None:
  return None if input is None else urllib.parse.unquote_plus(input)


def print_params_table(params: dict) -> str:
  table_params = ""
  for x in params:
    table_params += f"""
      <tr>
        <td>{x}</td>
        <td>{params[x]}</td>
      </tr>
    """

  html = f"""
    <table>
      <thead>
        <tr>
          <th>Key</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        {table_params}
      </tbody>
    </table>
  """
  return html


class AccessManagerRequestHandler(BaseHTTPRequestHandler):
  def handle_one_request(self):
    '''
    Базовая реализация BaseHTTPRequestHandler не позволяет внедрить
    диспетчер доступа, который, в свою очередь, является нормативным требованием,
    например https://tzi.com.ua/downloads/1.1-002-99.pdf
    '''
    # https://tedboy.github.io/python_stdlib/_modules/BaseHTTPServer.html#BaseHTTPRequestHandler.handle
    try:
      self.raw_requestline = self.rfile.readline(65537)
      if len(self.raw_requestline) > 65536:
        self.requestline = ''
        self.request_version = ''
        self.command = ''
        self.send_error(414)
        return
      if not self.raw_requestline:
        self.close_connection = 1
        return
      if not self.parse_request():
        # An error code has been sent, just exit
        return
      
      # Замена - все запросы переводятся на единственный метод access_manager
      mname = 'access_manager'
      if not hasattr(self, mname):
        self.send_error(501, "Method 'access_manager' not overriden")
        return
      # Конец замены

      method = getattr(self, mname)
      method()
      self.wfile.flush() # actually send the response if not already done.
    except socket.timeout as e:
      # a read or a write timed out.  Discard this connection
      self.log_error("Request timed out: %r", e)
      self.close_connection = 1
      return
    

  def access_manager(self):
    mname = 'do_' + self.command
    if not hasattr(self, mname):
      self.send_error(405, "Unsupported method (%r)" % self.command)
      return
    method = getattr(self, mname)
    method()


class RequestHandler(AccessManagerRequestHandler):
  def __init__(self, request, client_address, server):
    self.query_params = {}
    self.api = {
      "method": None,
      "service": None,
      "section": None,
    }
    super().__init__(request, client_address, server)


  def access_manager(self):
    parts = self.path.split('?', 1)
    self.api["method"] = self.command
    splitted_path = [url_decode(p) for p in parts[0].strip("/").split("/", 1)]
    self.api["service"] = splitted_path[0] if len(splitted_path) > 0 and len(splitted_path[0]) > 0 else "home"
    self.api["section"] = splitted_path[1] if len(splitted_path) > 1 else None

    query_string = parts[1] if len(parts) > 1 else ""
    for key, value in (map(url_decode, (item.split('=', 1) if '=' in item else [item, None]))
      for item in query_string.split('&') if len(item) > 0):
        self.query_params[key] = value if not key in self.query_params else [
          *(self.query_params[key] if isinstance(self.query_params[key],
            (list, tuple)) else [self.query_params[key]]),
          value
        ]

    return super().access_manager()


  def do_GET(self):
    print(self.path)
    print(self.command)

    self.send_response(200, "OK")
    self.send_header("Content-Type", "text/html; charset=utf-8")
    self.end_headers()
    
    links_html = """
      <h2>Тестування маршрутів</h2>
      <ul>
        <li><a href="/">Без параметрів</a></li>
        <li><a href="/user/">З сервісом</a></li>
        <li><a href="/user/auth">З розділами #1</a></li>
        <li><a href="/user/auth/secret">З розділами #2</a></li>
        <li><a href="/user/Уніфікований">URL-кодованими значеннями</a></li>
      </ul>
    """

    self.wfile.write(f"""<h1>HTTP</h1>
      {links_html}
      <h2>Результат розбору</h2>

      self.path = {self.path}<br/>

      api = {self.api}<br/>

      query_params:
      {print_params_table(self.query_params)}

      <hr/>

      <button onclick="linkClick()">LINK</button>
      <p id="out"></p>
      <script>
        function linkClick() {{
          fetch("/", {{
            method: "LINK",
          }}).then(r => r.text()).then(t => out.innerText = t);
        }}
      </script>
    """.encode())

  def do_LINK(self):
    self.send_response(200, "OK")
    self.send_header("Content-Type", "text/html; charset=utf-8")
    self.end_headers()
    self.wfile.write(f"LINK method response".encode())
  
def main():
  host = '127.0.0.1'
  port = 8080
  endpoint = (host, port)
  http_server = HTTPServer(endpoint, RequestHandler)
  try:
    print(f"Try start server http://{host}:{port}")
    http_server.serve_forever()
  except:
    print("Server stopped")


if __name__ == '__main__':
  main()
