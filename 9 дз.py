import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def convert(self, amount):
        return amount / self.rate


def get_usd_exchange_rate():
    url = "https://bank.gov.ua/ua/markets/exchangerates"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Не вдалося отримати дані з сайту! Код статусу: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", {"class": "table table-striped"})
    if table is None:
        raise Exception("Не вдалося знайти таблицю з курсами на сторінці.")

    rows = table.find_all("tr")
    if not rows:
        raise Exception("Не вдалося знайти рядки в таблиці.")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) > 0 and "USD" in cols[0].text.strip():
            try:
                usd_rate = float(cols[1].text.replace(",", "."))
                return usd_rate
            except ValueError:
                raise Exception(f"Невірний формат курсу для USD: {cols[1].text}")

    raise Exception("Не вдалося знайти курс долара на сайті.")


def main():
    try:
        usd_rate = get_usd_exchange_rate()
        print(f"Курс долара США: {usd_rate} грн.")

        converter = CurrencyConverter(usd_rate)

        amount_in_local_currency = float(input("Введіть кількість вашої валюти: "))

        amount_in_usd = converter.convert(amount_in_local_currency)

        print(f"Сума в доларах США: {amount_in_usd:.2f} USD")

    except Exception as e:
        print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()
