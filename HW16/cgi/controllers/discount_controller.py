from controllers.controller_rest import RestController, RestResponse, RestMeta, RestCache, RestStatus


class DiscountController(RestController):
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
    super().serve()

  def do_get(self):
    self.response.meta.service += ": Users's bonuses"
    self.response.meta.data_type = "object"
    self.response.meta.cache = RestCache.hrs1
    self.response.data = {
      "int": 10,
      "float": 1e-3,
      "str": "GET",
      "cyr": "Привет",
      "headers": self.request.headers
    }

  def do_post(self):
    self.response.meta.service += ": registration"
    self.response.meta.data_type = "object"
    self.response.data = {
      "int": 10,
      "float": 1e-3,
      "str": "POST",
      "cyr": "Привет",
      "headers": self.request.headers
    }
