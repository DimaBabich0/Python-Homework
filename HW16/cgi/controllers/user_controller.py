from models.request import CgiRequest
from controllers.controller_rest import RestController, RestResponse, RestMeta, RestCache, RestStatus
import base64
import binascii
import re


class UserController(RestController):
  def serve(self):
    self.response = RestResponse(
      meta=RestMeta(
        service="User API",
        request_method=self.request.request_method,
        links={
          "get": "GET /user",
          "post": "POST /user",
          "put": "PUT /user",
          "patch": "PATCH /user",
          "delete": "DELETE /user"
        }
      )
    )
    super().serve()


  def send_401(self, message: str):
    self.response.status = RestStatus.status401
    self.response.meta.cache = RestCache.no
    self.response.meta.data_type = "string"
    self.response.data = message


  def do_get(self):
    self.response.meta.service += ": authentication"

    auth_header = self.request.headers.get("Authorization", None)
    if not auth_header:
      self.send_401("Missing required header 'Authorization'")
      return

    auth_scheme = 'Basic '
    if not auth_header.startswith(auth_scheme):
      self.send_401(f"Invalid authorization scheme: {auth_scheme} only")
      return

    credentials = auth_header[len(auth_scheme):]
    if len(credentials) < 7:
      self.send_401(f"{auth_scheme} credentials too short: {credentials}")
      return

    match = re.search(r"[^a-zA-Z0-9+/=]", credentials)
    if match:
      self.send_401(
        f"Format error (invalid symbol) for credentials: {credentials}")
      return
    
    user_pass = None
    try :
      user_pass = base64.standard_b64decode(credentials).decode(encoding="utf-8")
    except binascii.Error:
      self.send_401(f"Padding error for credentials: {credentials}")
      return
    except Exception as err:
      self.send_401(f"Decode error '{err}' for credentials: {credentials}")
      return
    
    if ":" not in user_pass:
      self.send_401(f"User-pass format error (missing ':') {user_pass}")

    login, password = user_pass.split(":", 1)

    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "login": login,
      "password": password
    }


  def do_post(self):
    self.response.meta.service += ": registration"
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "int": 10,
      "float": 1e-3,
      "str": "Hello",
      "cyr": "Привет",
      "method": "POST",
      "headers": self.request.headers
    }


  def do_put(self):
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "int": 10,
      "float": 1e-3,
      "str": "Hello",
      "cyr": "Привет",
      "method": "PUT",
      "headers": self.request.headers
    }
    

  def do_patch(self):
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "int": 10,
      "float": 1e-3,
      "str": "Hello",
      "cyr": "Привет",
      "method": "PATCH",
      "headers": self.request.headers
    }
    

  def do_delete(self):
    self.response.meta.cache = RestCache.hrs1
    self.response.meta.data_type = "object"
    self.response.data = {
      "int": 10,
      "float": 1e-3,
      "str": "Hello",
      "cyr": "Привет",
      "method": "DELETE",
      "headers": self.request.headers
    }
    
