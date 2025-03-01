import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    date_time TEXT,
    temperature REAL
)
''')
conn.commit()

url = 'https://weather.com/weather/today/l/your_location'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    temperature_element = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ')

    if temperature_element:
        temperature = float(temperature_element.text.replace('°', ''))
        print(f"Температура: {temperature}°C")

        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (current_datetime, temperature))

        conn.commit()
        conn.close()

        print("Дані успішно додано до БД.")
    else:
        print("Не вдалося знайти температуру.")
else:
    print(f"Не вдалося отримати дані з сайту, код статусу: {response.status_code}")
