from models.request import CgiRequest
from utils.html import dict_to_table


class HomeController:

  def __init__(self, request: CgiRequest):
    self.request = request


  def serve(self):
    action = self.request.action.lower()
    controller_action = getattr(self, action)
    controller_action()


  def index(self):
    with open("./views/_layout.html", mode="rt", encoding="utf-8") as file:
      layout = file.read()

    print("Content-Type: text/html; charset=utf-8\n")
    print(layout)


  def params(self):
    envs = dict_to_table(self.request.server, "Env", "Value")
    hdrs = dict_to_table(self.request.headers, "Header", "Value")
    qp = dict_to_table(self.request.query_params, "Param", "Value")

    body = f"""
        <h1>Environment variables:</h1>

        <h2>Environment</h2>
        {envs}

        <h2>Headers</h2>
        {hdrs}

        <h2>Query params</h2>
        {qp}
    """

    with open("./views/_layout.html", mode="rt", encoding="utf-8") as file:
      layout = file.read()

    print("Content-Type: text/html; charset=utf-8\n")
    print(layout.replace("<!-- RenderBody -->", body))
