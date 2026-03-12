import math
from controllers.controller_rest import ControllerRest
from controllers.rest_error import RestError
from controllers.rest_response import RestLink, RestMeta, RestPagination

products = [
  { "id": 1,  "name": "Product 1",  "price": 10.99  },
  { "id": 2,  "name": "Product 2",  "price": 19.99  },
  { "id": 3,  "name": "Product 3",  "price": 29.99  },
  { "id": 4,  "name": "Product 4",  "price": 39.99  },
  { "id": 5,  "name": "Product 5",  "price": 49.99  },
  { "id": 6,  "name": "Product 6",  "price": 59.99  },
  { "id": 7,  "name": "Product 7",  "price": 69.99  },
  { "id": 8,  "name": "Product 8",  "price": 79.99  },
  { "id": 9,  "name": "Product 9",  "price": 89.99  },
  { "id": 10, "name": "Product 10", "price": 99.99  },
  { "id": 11, "name": "Product 11", "price": 109.99 },
  { "id": 12, "name": "Product 12", "price": 119.99 },
]


class ProductController(ControllerRest):
  def do_GET(self):
    # pagination
    # - total items
    # - total pages
    # - items per page
    # - page number

    total_items = len(products)

    per_page = self.query_params.get("perpage", 5)
    if not isinstance(per_page, int):
      try:
        per_page = int(per_page)
      except:
        per_page = 0
    if per_page <= 0:
      raise RestError(400, "Bad Request", "Pagination error: 'perpage' is not valid (positive number expected)")

    total_pages = math.ceil(total_items / per_page)

    page = self.query_params.get("page", 1)
    if not isinstance(page, int):
      try:
        page = int(page)
      except:
        page = 0
    if page <= 0 or page > total_pages:
      raise RestError(400, "Bad Request", f"Pagination error: 'page' is not valid, must be in range (1 - {total_pages})")

    has_prev = page > 1
    has_next = page < total_pages

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paged_items = products[start_idx:end_idx]

    self.rest_response.meta = RestMeta(pagination = RestPagination(
      page = page,
      total_items = total_items,
      per_page = per_page,
      total_pages = total_pages,
      links=[
        RestLink("firstPage", "1", f"?perpage={per_page}"),
        RestLink("lastPage", str(total_pages), f"?page={total_pages}&perpage={per_page}"),
        RestLink("previousPage", str(page - 1), f"?page={page - 1}&perpage={per_page}") if has_prev else None,
        RestLink("nextPage", str(page + 1), f"?page={page + 1}&perpage={per_page}") if has_next else None,
      ],
      has_prev=has_prev,
      has_next=has_next
    ))

    self.rest_response.data = {
      "items": paged_items
    }

