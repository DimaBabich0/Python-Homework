from controllers.controller_rest import ControllerRest
from controllers.rest_error import RestError


class UserController(ControllerRest):
  def do_GET(self):
    self.rest_response.data = {
      "method": self.handler.api["method"],
      "service": self.handler.api["service"],
      "section": self.handler.api["section"],
      "query_params": self.handler.query_params if self.handler.query_params else None
    }
  

  def do_POST(self):
    # Использования исключений как передача данных про аварийное окончание
    raise RestError(code=422, phrase="Unprocessable Entity",
                    data="Invalid format for E-mail")

