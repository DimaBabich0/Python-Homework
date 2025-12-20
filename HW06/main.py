import mysql.connector

db_ini = {
  'host': 'localhost',
  'port': 3306,
  'user': 'user_knp_221',
  'password': 'pass_221',
  'database': 'server_221',
  'charset': 'utf8mb4',
  'collation': 'utf8mb4_unicode_ci',
  'use_unicode': True
}

db_connection = None


def connect_db():
  global db_connection
  
  try:
    db_connection = mysql.connector.connect(**db_ini)
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Connection OK")


def close_connection():
  db_connection.close()


def show_databases():
  global db_connection

  if db_connection is None:
    return

  cursor = None
  try:
    cursor = db_connection.cursor()
    cursor.execute("""SELECT uuid(), uuid()
                   UNION ALL
                   SELECT uuid(), uuid()
                   UNION ALL
                   SELECT uuid(), uuid()""")
  except mysql.connector.Error as err:
    print(err)
  else:
    print_table(cursor)
  finally:
    cursor.close()


def print_table(cursor):
  print("║", cursor.column_names[0], "".rjust(
    29, ' '), "║", cursor.column_names[0], "║".rjust(31, ' '))
  print("╠" + "═" * 38 + "╬" + "═" * 38 + "╣")

  for row in cursor:
    print("║", " ║ ".join(row), "║")


def main():
  connect_db()
  show_databases()
  close_connection()


if __name__ == '__main__':
  main()
