import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL страницы с объявлениями
URL = "https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

# Получение HTML-кода страницы
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

# Поиск объявлений
apartments = []
for item in soup.find_all("article", class_="_93444fe79c--container--Povoi"):
    title = item.find("span", class_="_93444fe79c--color_black_100--EphiD").text if item.find("span", class_="_93444fe79c--color_black_100--EphiD") else "Не указано"
    price = item.find("span", class_="_93444fe79c--color_black_100--EphiD").text if item.find("span", class_="_93444fe79c--color_black_100--EphiD") else "Не указано"
    link = item.find("a", class_="_93444fe79c--link--eoxce")["href"] if item.find("a", class_="_93444fe79c--link--eoxce") else "Нет ссылки"
    apartments.append([title, price, link])

# Запись данных в Excel
columns = ["Название", "Цена", "Ссылка"]
df = pd.DataFrame(apartments, columns=columns)
df.to_excel("cian_apartments.xlsx", index=False)

print("Данные сохранены в файл cian_apartments.xlsx")