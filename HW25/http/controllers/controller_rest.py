from http.server import BaseHTTPRequestHandler
from controllers.rest_response import RestResponse, RestStatus
from controllers.rest_error import RestError


# С целью избегания адреса /rest меняем правило именования для класса
class ControllerRest : 
  def __init__(self, handler: BaseHTTPRequestHandler):
    self.handler = handler 


  def before_execution(self):
    self.rest_response = RestResponse()


  # Основной метод запуска контроллера, который обеспечивает жизненный цикл запроса
  def serve(self):
    self.before_execution()
    mname = 'do_' + self.handler.command
    if not hasattr(self, mname):
      self.rest_response.status = RestStatus.method_not_allowed_405
      self.rest_response.data = f"Method {self.handler.command} is not allowed for this resource"
    else:
      method = getattr(self, mname)
      # выполняем метод, передавая управление контроллеру
      try:
        method()
        self.send_success()
        return
      except RestError as err:
        self.rest_response.status = RestStatus(
          is_ok = False,
          code = err.code,
          phrase = err.phrase)
        self.rest_response.data = err.data
      except Exception as ex:
        self.rest_response.status = RestStatus(
          is_ok = False,
          code = 500,
          phrase = "Request processing error " + str(ex)
        )
    self.send_error()


  def send_success(self):
    self.handler.send_rest_response(self.rest_response)


  def send_error(self):
    self.handler.send_rest_response(self.rest_response)

