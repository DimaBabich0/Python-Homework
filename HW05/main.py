import requests
from datetime import datetime


class NbuRate:
  def __init__(self, j: dict):
    self.r030 = j["r030"]
    self.name = j["txt"]
    self.rate = j["rate"]
    self.abbr = j["cc"]

  def __str__(self):
    return "%s (%s): %.4f" % (self.abbr, self.name, self.rate)


class RatesData:
  def __init__(self):
    self.exchange_date = None
    self.rates = []


class NbuRatesData(RatesData):
  __url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

  def __init__(self, date: str):
    request = requests.get(f"{NbuRatesData.__url}&date={date}")
    response = request.json()
    if not response:
      raise ValueError("No data returned for this date")
    self.exchange_date = response[0]["exchangedate"]
    self.rates = [NbuRate(r) for r in response]


def validate_date(date_str: str) -> str:
  try:
    date_obj = datetime.strptime(date_str, "%d.%m.%Y")
  except ValueError:
    raise ValueError("Invalid date format. Use DD.MM.YYYY")

  today = datetime.today()
  if date_obj >= today:
    raise ValueError("Date must be in the past")

  return date_obj.strftime("%Y%m%d")


def main():
  user_date = input("Enter date (DD.MM.YYYY): ").strip()
  try:
    api_date = validate_date(user_date)
  except ValueError as e:
    print("Error:", e)
    return
  rates_data = NbuRatesData(api_date)
  sorted_rates = sorted(rates_data.rates, key=lambda r: r.abbr)

  print("Exchange rates for %s:" % (rates_data.exchange_date))
  for rate in sorted_rates:
    print(rate)


if __name__ == '__main__':
  main()
