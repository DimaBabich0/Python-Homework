from http.server import BaseHTTPRequestHandler


class HomeController():
  def __init__(self, handler: BaseHTTPRequestHandler):
    self.handler = handler


  def do_GET(self):
    self.handler.send_response(200, "OK")
    self.handler.send_header("Content-Type", "text/html; charset=utf-8")
    self.handler.end_headers()
    self.handler.wfile.write(f"""
      <title>Title</title>
      <link rel="stylesheet" href="css/site.css" />

      <h1>HTTP</h1>
      <img src="/img/cat.png" alt="cat.png" width=300 />
      <img src="/img/cat.jpg" alt="cat.jpg" width=500 />
      <img src="/img/cat.gif" alt="cat.gif" width=300 />
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
