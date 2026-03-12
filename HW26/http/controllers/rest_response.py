import math


class RestStatus:
  def __init__(self,
               is_ok:bool=True,
               code:int=200,
               phrase:str="OK"):
    self.is_ok = is_ok
    self.code = code
    self.phrase = phrase
    
  def __json__(self):
    return {
      "isOK": self.is_ok,
      "code": self.code,
      "phrase": self.phrase
    }

RestStatus.ok_200 = RestStatus(True, 200, "OK")
RestStatus.created_201 = RestStatus(True, 201, "Created")
RestStatus.no_content_204 = RestStatus(True, 204, "No Content")
RestStatus.bad_request_400 = RestStatus(False, 400, "Bad Request")
RestStatus.unauthorized_401 = RestStatus(False, 401, "Unauthorized")
RestStatus.forbidden_403 = RestStatus(False, 403, "Forbidden")
RestStatus.not_found_404 = RestStatus(False, 404, "Not Found")
RestStatus.method_not_allowed_405 = RestStatus(False, 405, "Method Not Allowed")
RestStatus.internal_server_error_500 = RestStatus(False, 500, "Internal Server Error")
RestStatus.not_implemented_501 = RestStatus(False, 501, "Not Implemented")
RestStatus.service_unavailable_503 = RestStatus(False, 503, "Service Unavailable")

class RestPagination:
  def __init__(self,
               per_page:int,
               page:int,
               total_items:int,
               total_pages:int|None,
               links,
               has_prev:bool|None=None,
               has_next:bool|None=None):
    self.per_page = per_page
    self.page = page
    self.total_items = total_items
    self.total_pages = total_pages if total_pages != None else math.ceil(total_items / per_page)
    self.links = links
    self.has_prev = page > 1 if has_prev is None else has_prev
    self.has_next = page < self.total_pages if has_next is None else has_next

  def __json__(self):
    return {
      "perPage": self.per_page,
      "currentPage": self.page,
      "totalItems": self.total_items,
      "totalPages": self.total_pages,
      "hasPrev": self.has_prev,
      "hasNext": self.has_next,
      "links": self.links
    }


class RestLink:
  def __init__(self, name:str, num:int, url:str):
    self.name = name
    self.num = num
    self.url = url

  def __json__(self):
    return {
      "name": self.name,
      "num": self.num,
      "url": self.url
    }


class RestMeta:
  def __init__(self, pagination:RestPagination|None):
    self.pagination = pagination
  
  def __json__(self):
    return {
      "pagination": self.pagination
    }


class RestResponse:
  def __init__(self,
               status:RestStatus|None=None,
               meta:RestMeta|None=None,
               data:any=None):
    self.status = status if status != None else RestStatus()
    self.meta = meta
    self.data = data

  def __json__(self):
    return {
      "status": self.status,
      "meta": self.meta,
      "data": self.data
    }
