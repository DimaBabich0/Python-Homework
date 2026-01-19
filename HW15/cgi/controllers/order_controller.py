from models.request import CgiRequest
import json
import sys

from controllers.controller_rest import RestResponse, RestMeta, RestCache, RestStatus


class OrderController:
  def __init__(self, request: CgiRequest):
    self.request = request

  def serve(self):
    self.response = RestResponse(
      meta=RestMeta(
        service="Order API",
        request_method=self.request.request_method,
        links={
          "get": "GET /order",
          "post": "POST /order",
          "put": "PUT /order",
          "patch": "PATCH /order",
          "delete": "DELETE /order"
        }
      )
    )

    action = "do_" + self.request.request_method.lower()
    controller_action = getattr(self, action, None)

    if controller_action:
      controller_action()
    else :
      self.response.status = RestStatus.status405
      self.response.meta.data_type = "null"
    
    sys.stdout.buffer.write(b"Content-Type: application/json; charset=utf-8\n\n")
    sys.stdout.buffer.write(
        json.dumps(self.response,
                   ensure_ascii=False,
                   default=lambda x: x.to_json() if hasattr(x, "to_json") else str
                  ).encode())


  def do_get(self):
    self.response.meta.service += ": authentication"
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "requestMethod": "GET",
      "headers": self.request.headers
    }



  def do_post(self):
    self.response.meta.service += ": registration"
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "requestMethod": "POST",
      "headers": self.request.headers
    }


  def do_put(self):
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "requestMethod": "PUT",
      "headers": self.request.headers
    }
    


  def do_patch(self):
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "requestMethod": "PATCH",
      "headers": self.request.headers
    }
    

  
  def do_delete(self):
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "requestMethod": "DELETE",
      "headers": self.request.headers
    }
    