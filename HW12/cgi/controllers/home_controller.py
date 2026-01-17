from models.request import CgiRequest
from utils.html import dict_to_table


class HomeController:

  def __init__(self, request: CgiRequest):
    self.request = request


  def serve(self):
    action = (self.request.path_parts[2].lower()
              if len(self.request.path_parts) > 2
              and len(self.request.path_parts[2].strip()) > 0
              else 'index')
    controller_action = getattr(self, action)
    controller_action()


  def index(self):
    envs = dict_to_table(self.request.server, "Env", "Value")
    hdrs = dict_to_table(self.request.headers, "Header", "Value")
    qp = dict_to_table(self.request.query_params, "Param", "Value")

    html = f"""
      <!DOCTYPE html>
      <html lang="uk">
      <head>
        <meta charset="windows-1251">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index</title>
        <link rel="icon" href="/worst_lang_in_the_world.png" />
        <link rel="stylesheet" href="/css/site.css" />
      </head>
      <body>
        <li><a href="/uk-UA/Home/params/">To params</a></li>
        <script src="/js/site.js"></script>
      </body>
      </html>
    """

    print("Content-Type: text/html; charset=cp1251")
    # print(f"Content-Length: {len(html)}")
    print()
    print(html)


  def params(self):
    envs = dict_to_table(self.request.server, "Env", "Value")
    hdrs = dict_to_table(self.request.headers, "Header", "Value")
    qp = dict_to_table(self.request.query_params, "Param", "Value")

    html = f"""
      <!DOCTYPE html>
      <html lang="uk">
      <head>
        <meta charset="windows-1251">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Params</title>
        <link rel="icon" href="/worst_lang_in_the_world.png" />
        <link rel="stylesheet" href="/css/site.css" />
      </head>
      <body>
        <h1>Environment variables:</h1>

        <h2>Environment</h2>
        {envs}

        <h2>Headers</h2>
        {hdrs}

        <h2>Query params</h2>
        {qp}

        <p><a href="/">To main</a></p>
      </body>
      </html>
    """

    print("Content-Type: text/html; charset=cp1251")
    print()
    print(html)
