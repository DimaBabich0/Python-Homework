from models.request import CgiRequest

class OrdertestController:
  def __init__(self, request: CgiRequest):
    self.request = request


  def serve(self):
    action = self.request.action.lower()
    controller_action = getattr(self, action, None)
    if controller_action:
      controller_action()
    else :
      print("Status: 405 Method Not Allowed\n")


  def index(self):
    with open("./views/_layout.html", mode="rt", encoding="utf-8") as file:
      layout = file.read()

    with open("./views/ordertest_index.html", mode="rt", encoding="utf-8") as file:
      body = file.read()

    print("Content-Type: text/html; charset=utf-8\n")
    print(layout.replace("<!-- RenderBody -->", body))
