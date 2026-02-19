from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse


def url_decode(input: str | None) -> str | None:
  return None if input is None else urllib.parse.unquote_plus(input)


class RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    print(self.path)
    print(self.command)

    parts = self.path.split('?', 1)
    path = parts[0]  # /user/auth

    query_string = parts[1] if len(parts) > 1 else ""

    query_params = {}
    for key, value in (map(url_decode, (item.split('=', 1) if '=' in item else [item, None]))
                       for item in query_string.split('&') if len(item) > 0):
      query_params[key] = value if not key in query_params else [
          *(query_params[key] if isinstance(query_params[key],
            (list, tuple)) else [query_params[key]]),
          value
      ]

    self.send_response(200, "OK")
    self.send_header("Content-Type", "text/html; charset=utf-8")
    self.end_headers()

    links_html = """
    <h2>Тестування розбору параметрів</h2>
    <ul>
        <li><a href="/user/auth">Без параметрів</a></li>
        <li><a href="/user/auth?">Без параметрів, але з ?</a></li>
        <li><a href="/user/auth?hash=1a2d==&amp;p=50/50&amp;q=who?&amp;x=10&amp;y=20&amp;x=30&amp;json">З параметрами та повторами ключів</a></li>
        <li><a href="/user/auth?hash=1a2d==&amp;p=50/50&amp;q=who?&amp;&amp;x=10&amp;y=20&amp;x=30&amp;json&amp;url=%D0%A3%D0%BD%D1%96%D1%84%D1%96%D0%BA%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B9&amp;%D0%BB%D0%BE%D0%BA%D0%B0%D1%82%D0%BE%D1%80=%D1%80%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%96%D0%B2&amp;2+2=4">URL-кодовані ключі та значення</a></li>
    </ul>
    """
    self.wfile.write(f"""<h1>HTTP</h1>
        {links_html}
        <h2>Результат розбору</h2>
        self.path = {self.path}<br/>   
        path = {path}<br/>   
        query_string = {query_string}<br/>   
        query_params = {query_params}<br/>   
        """.encode())


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
