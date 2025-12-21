#!C:/Python314/python.exe

import os

env_items = sorted(os.environ.items(), key=lambda item: item[0])

rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in env_items)

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
  <h1>Variables environment:</h1>
  <table>
    <tr>
      <th>Name</th>
      <th>Value</th>
    </tr>
    {rows}
  </table>
</body>
</html>
"""

print("Content-Type: text/html; charset=cp1251")
print(f"Content-Length: {len(html)}")
print()
print(html)