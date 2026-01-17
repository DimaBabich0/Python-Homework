#!C:/Python314/python.exe

DEV_MODE = True

import sys
import os
import importlib
from models.request import CgiRequest

def header_name(hdr: str) -> str:
  '''Convert Apache casing form HEADER_NAME to classic Header-Name'''
  return "-".join(
    s[0].upper() + s[1:].lower()
    for s in hdr.split('_'))


def send_error(message, code=404, phrase="Not Found"):
  print(f"Status: {code} {phrase}")
  print("Content-Type: text/plain, utf-8")
  print()
  print(message)
  sys.stdout.flush()
  os._exit(0)


server = {k: v for k, v in os.environ.items() if k in
           ('REQUEST_URI', 'QUERY_STRING', 'REQUEST_METHOD')}

query_params = {k: v
                for k, v in (item.split('=') if '=' in item else (item, None)
                             for item in server['QUERY_STRING'].split('&'))}

if not "htctrl" in query_params:
  print("Status: 403 Forbidden")
  print()
  exit()

path = server['REQUEST_URI'].split("?", 1)[0]
if not path.endswith('/'):
  ext = path[(path.rindex(".") + 1):]
  allowed_media_types = {
      "png": "image/png",
      "jpg": "image/jpeg",
      "css": "text/css",
      "js": "text/javascript",
  }
  if ext in allowed_media_types:
    try:
      with open(os.path.abspath("./static") + path, mode="rb") as file:
        sys.stdout.buffer.write(f"Content-Type: {allowed_media_types[ext]}\n\n".encode())
        sys.stdout.buffer.write(file.read())
        sys.stdout.flush()
      os._exit(0)
    except:
      pass

headers = {header_name(k[5:]): v for k,
           v in os.environ.items() if k.startswith('HTTP_')}

parts = path.split('/', 4)
lang = parts[1] if len(parts) > 1 and len(parts[1].strip()) > 0 else 'uk-UA'
controller = parts[2] if len(parts) > 2 and len(parts[2].strip()) > 0 else 'Home'
action = parts[3] if len(parts) > 3 and len(parts[3].strip()) > 0 else 'Index'
id = parts[4] if len(parts) > 4 and len(parts[4].strip()) > 0 else None


module_name = controller.lower() + "_controller"
class_name = controller.capitalize() + "Controller"
action_name = "do_" + server["REQUEST_METHOD"].lower()

sys.path.append(".")
try:
  controller_module = importlib.import_module(f"controllers.{module_name}")

  controller_class = getattr(controller_module, class_name)
  controller_object = controller_class(
      CgiRequest(
          server=server,
          query_params=query_params,
          headers=headers,
          path=path,
          controller=controller,
          path_parts=parts[1:]
      )
  )

  controller_action = getattr(controller_object, "serve")
  controller_action()

  sys.stdout.flush()
  os._exit(0)
except Exception as ex:
    message = "Request processing error "
    if DEV_MODE:
        message += str(ex)
    send_error(message, code=500, phrase="Internal Server Error")
