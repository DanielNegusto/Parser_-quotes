import requests
from bs4 import BeautifulSoup
import json

# URL сайта
url = 'https://quotes.toscrape.com/'

# Выполнение GET-запроса
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Сбор данных
quotes = []
for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    quotes.append({'text': text, 'author': author})

# Сохранение в JSON файл
with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quotes, f, ensure_ascii=False, indent=4)
