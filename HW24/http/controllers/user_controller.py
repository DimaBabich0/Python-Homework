from http.server import BaseHTTPRequestHandler
from controllers.controller_rest import ControllerRest


class UserController(ControllerRest):
  def __init__(self, handler: BaseHTTPRequestHandler):
    super().__init__(handler)

  def do_GET(self):
    self.rest_response.data = {
      "method": self.handler.api["method"],
      "service": self.handler.api["service"],
      "section": self.handler.api["section"],
      "query_params": self.handler.query_params if self.handler.query_params else None
    }

