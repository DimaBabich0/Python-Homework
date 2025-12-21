import mysql.connector
from datetime import datetime

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
    print("Connected")


def close_connection():
  db_connection.close()


def input_date() -> str:
  while True:
    date = input("Input date [yyyy-mm-dd]: ")

    if len(date) != 10 or not date.isdigit() and date[4] != "-" and date[7] != "-":
      print("Invalid format")
      continue

    try:
      return datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError as err:
      print("Error:", err)


def show_prep(date: str):
  sql = "SELECT DATEDIFF(CURRENT_TIMESTAMP, STR_TO_DATE(%s, '%Y-%m-%d')) AS `date difference`"

  global db_connection
  if db_connection is None:
    return

  try:
    with db_connection.cursor(dictionary=True) as cursor:
      cursor.execute(sql, (date,))
      for row in cursor:
        diff = row["date difference"]
        if diff == 0:
          print("Дата є поточною")
        elif diff > 0:
          print(f"Дата у минулому за {diff} днів від поточної дати")
        elif diff < 0:
          print(f"Дата у майбутньому через {-diff} дні від поточної дати")

  except mysql.connector.Error as err:
    print("Error:", err)
    print("SQL:", sql)


def main():
  connect_db()
  show_prep(input_date())
  close_connection()


if __name__ == '__main__':
  main()
