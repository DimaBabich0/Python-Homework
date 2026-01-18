from models.request import CgiRequest
import io, json, sys

class UserController:

  def __init__(self, request: CgiRequest):
    self.request = request


  def serve(self):
    action = "do_" + self.request.request_method.lower()
    controller_action = getattr(self, action, None)
    if controller_action:
      controller_action()
    else :
      print("Status: 405 Method Not Allowed\n")


  def do_get(self):
    data = {
      "int":  10,
      "float": 1e-3,
      "str": "Hello",
      "cyr": "Привет",
      "method": "GET"
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))


  def do_post(self):
    data = {
      "int":  10,
      "float": 1e-3,
      "str": "Hello",
      "cyr": "Привет",
      "method": "POST"
    }
    sys.stdout.buffer.write(b"Content-Type: application/json; charset=utf-8\n")
    print()
    print(json.dumps(data, fp=sys.stdout.buffer, ensure_ascii=False))
