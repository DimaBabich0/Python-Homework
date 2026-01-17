#!C:/Python314/python.exe

import os


def header_name(hdr: str) -> str:
  '''Convert Apache casing form HEADER_NAME to classic Header-Name'''
  return "-".join(
    s[0].upper() + s[1:].lower()
    for s in hdr.split('_'))


def dict_to_table(data: dict, col1="Key", col2="Value") -> str:
  rows = "".join(
      f"<tr><td>{k}</td><td>{v}</td></tr>"
      for k, v in data.items()
  )
  return f"""
    <table>
      <thead>
        <tr>
          <th>{col1}</th>
          <th>{col2}</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
    """


request = {k: v for k, v in os.environ.items() if k in
           ('REQUEST_URI', 'QUERY_STRING', 'REQUEST_METHOD')}

query_params = {k: v
                for k, v in (item.split('=') if '=' in item else (item, None)
                             for item in request['QUERY_STRING'].split('&'))}

if not "htctrl" in query_params:
  print("Status: 403 Forbidden")
  print()
  exit()

path = request['REQUEST_URI'].split("?", 1)[0]
static_dir = "."


headers = {header_name(k[5:]): v for k,
           v in os.environ.items() if k.startswith('HTTP_')}

parts = path.split('/', 4)
lang = parts[1] if len(parts) > 1 and len(parts[1].strip()) > 0 else 'uk-UA'
controller = parts[2] if len(parts) > 2 and len(parts[2].strip()) > 0 else 'Home'
action = parts[3] if len(parts) > 3 and len(parts[3].strip()) > 0 else 'Index'
id = parts[4] if len(parts) > 4 and len(parts[4].strip()) > 0 else None


module_name = controller.lower() + "_controller"
class_name = controller.capitalize() + "Controller"
action_name = "do_" + request["REQUEST_METHOD"].lower()

envs = dict_to_table(request, "Env", "Value")
hdrs = dict_to_table(headers, "Header", "Value")
qp = dict_to_table(query_params, "Param", "Value")

html = f"""
<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="windows-1251">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Py-CGI</title>
  <style>
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #444;
      padding: 6px 10px;
      text-align: left;
    }}
    th {{
      background-color: #eee;
    }}
  </style>
</head>
<body>
  <h1>Environment variables:</h1>
  Language: {lang}<br/>
  Controller: {controller}<br/>
  Action: {action}<br/>
  Id: {id}<br/>
  ----------------------------------------<br/>
  Module_name: {module_name}<br/>
  Class_name: {class_name}<br/>
  Action_name: {action_name}<br/>

  <h2>Request</h2>
  {envs}

  <h2>Headers</h2>
  {hdrs}

  <h2>Query params</h2>
  {qp}
</body>
</html>
"""

print("Content-Type: text/html; charset=cp1251")
# print(f"Content-Length: {len(html)}")
print()
print(html)
