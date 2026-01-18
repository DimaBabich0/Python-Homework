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
    if controller_action:
      controller_action()
    else :
      print("Status: 405 Method Not Allowed\n")


  def do_get(self):
    data = {
      "requestMethod": "GET"
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))


  def do_post(self):
    data = {
      "requestMethod": "POST"
    }
    sys.stdout.buffer.write(b"Content-Type: application/json; charset=utf-8\n")
    print()
    print(json.dumps(data, ensure_ascii=False))

  def do_put(self):
    data = {
      "requestMethod": "PUT"
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))


  def do_patch(self):
    data = {
      "requestMethod": "PATCH"
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))

  
  def do_delete(self):
    data = {
      "requestMethod": "DELETE"
    }
    print("Content-Type: application/json; charset=utf-8")
    print()
    print(json.dumps(data, ensure_ascii=False))