import datetime


class RestStatus:
  def __init__(self,
               is_ok: bool,
               code: int,
               message: str):
    self.is_ok = is_ok
    self.code = code
    self.message = message

  def to_json(self):
    return {
      "isOK": self.is_ok,
      "code": self.code,
      "message": self.message
    }


RestStatus.status200 = RestStatus(True, 200, "OK")
RestStatus.status401 = RestStatus(True, 401, "UnAuthorized")
RestStatus.status405 = RestStatus(True, 405, "Method Nok Allowed")


class RestCache:
  def __init__(self,
               exp: str | int | None = None,
               lifetime: int | None = None):
    self.exp = exp
    self.lifetime = lifetime

  def to_json(self):
    return {
      "exp": self.exp,
      "lifetime": self.lifetime,
      "units": "seconds"
    }


RestCache.no = RestCache()
RestCache.hrs1 = RestCache(lifetime=60*60)


class RestMeta:
  def __init__(self,
               service: str,
               request_method: str | None = None,
               data_type: str = "null",
               auth_user_id: str | int | None = None,
               cache: RestCache = RestCache.no,
               server_time: int | None = None,
               params: dict | None = None,
               links: dict | None = None):
    self.service = service
    self.request_method = request_method
    self.auth_user_id = auth_user_id
    self.data_type = data_type
    self.cache = cache
    self.server_time = server_time if server_time is not None else datetime.datetime.now().timestamp()
    self.params = params
    self.links = links

  def to_json(self):
    return {
      "service": self.service,
      "requestMethod": self.request_method,
      "dataType": self.data_type,
      "cache": self.cache.to_json(),
      "serverTime": self.server_time,
      "params": self.params,
      "links": self.links,
      "authUserId": self.auth_user_id
    }


class RestResponse:
  def __init__(self,
               meta: RestMeta | None = None,
               status: RestStatus = RestStatus.status200,
               data: any = None):
    self.meta = meta
    self.status = status
    self.data = data

  def to_json(self):
    return {
      "meta": self.meta,
      "status": self.status,
      "data": self.data,
    }
