import datetime
from models.request import CgiRequest
import json
import sys


class OrderController:
  def __init__(self, request: CgiRequest):
    self.request = request

  def serve(self):
    action = "do_" + self.request.request_method.lower()
    controller_action = getattr(self, action, None)

    if self.request.headers.get("Custom-Header") is None:
      print("Content-Type: application/json; charset=utf-8\n")
      print(json.dumps({"Status": "403 Forbidden"}, ensure_ascii=False))
      return

    if controller_action:
      controller_action()
    else :
      print("Status: 405 Method Not Allowed\n")


  def do_get(self):
    data = {
      "requestMethod": "GET",
      "headers": self.request.headers
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))


  def do_post(self):
    data = {
      "requestMethod": "POST",
      "headers": self.request.headers
    }
    sys.stdout.buffer.write(b"Content-Type: application/json; charset=utf-8\n")
    print()
    print(json.dumps(data, ensure_ascii=False))

  def do_put(self):
    data = {
      "requestMethod": "PUT",
      "headers": self.request.headers
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))


  def do_patch(self):
    data = {
      "requestMethod": "PATCH",
      "headers": self.request.headers
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))

  
  def do_delete(self):
    data = {
      "requestMethod": "DELETE",
      "headers": self.request.headers
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))