from models.request import CgiRequest
import json
import sys

from controllers.controller_rest import RestResponse, RestMeta, RestCache, RestStatus


class DiscountController:
  def __init__(self, request: CgiRequest):
    self.request = request

  def serve(self):
    self.response = RestResponse(
      meta=RestMeta(
        service="Discount API",
        request_method=self.request.request_method,
        links={
          "get": "GET /discount",
          "post": "POST /discount"
        }
      )
    )

    action = "do_" + self.request.request_method.lower()
    controller_action = getattr(self, action, None)

    if controller_action:
      controller_action()
    else:
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
      "method": "GET",
      "headers": self.request.headers
    }


  def do_post(self):
    self.response.meta.service += ": registration"
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "method": "POST",
      "headers": self.request.headers
    }
    
