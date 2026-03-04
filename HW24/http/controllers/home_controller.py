from http.server import BaseHTTPRequestHandler
from controllers.controller_rest import ControllerRest


class HomeController(ControllerRest):
  def __init__(self, handler: BaseHTTPRequestHandler):
    super().__init__(handler)
  

  def html_params_table(self) -> str:
    table_params = ""
    for x in self.handler.query_params:
      table_params += f"""
        <tr>
          <td>{x}</td>
          <td>{self.handler.query_params[x]}</td>
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


  def do_GET(self):
    links_html = """
      <h2>Тестування маршрутів</h2>
      <ul>
        <li><a href="/">Без параметрів</a></li>
        <li><a href="/home/">З сервісом</a></li>
        <li><a href="/home/auth/">З розділами</a></li>
        <li><a href="/home?hash=1a2d==&p=50/50&q=who?&x=10&y=20&x=30&json/">З параметрами та повторами ключів</a></li>
        <li><a href="/home/Уніфікований/">URL-кодованими значеннями</a></li>
      </ul>
    """

    self.handler.send_response(200, "OK")
    self.handler.send_header("Content-Type", "text/html; charset=utf-8")
    self.handler.end_headers()
    self.handler.wfile.write(f"""
      <title>Title</title>
      <link rel="stylesheet" href="css/site.css" />
      
      {links_html}
      self.path = {self.handler.path}<br/>
      api = {self.handler.api}<br/>


      <h1>HTTP</h1>
      <img src="/img/cat.png" alt="cat.png" width=300 />
      <img src="/img/cat.jpg" alt="cat.jpg" width=500 />
      <img src="/img/cat.gif" alt="cat.gif" width=300 />
      <hr/>

      <h2>Результат розбору</h2>
      self.path = {self.handler.path}<br/>
      query_params:
      {("empty" if not self.handler.query_params else self.html_params_table())}                      
      <hr/>

      <button onclick="linkClick()">LINK</button>
      <p id="out"></p>
      <script src="/js/site.js"></script>
    """.encode())



  def do_LINK(self):
    self.handler.send_response(200, "OK")
    self.handler.send_header("Content-Type", "text/html; charset=utf-8")
    self.handler.end_headers()
    self.handler.wfile.write(f"LINK method response".encode())
