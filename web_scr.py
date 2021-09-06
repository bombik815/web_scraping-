import requests
from bs4 import BeautifulSoup


# определяем список ключевых слов
KEYWORDS = {'Дизайн', 'Фото', 'Web', 'Python*','Java*', 'Беспроводные технологии*'}

URL = 'https://habr.com'
response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
soup = BeautifulSoup(response.text, "lxml")
articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')
    hubs = {hub.text.strip() for hub in hubs}
    if KEYWORDS & hubs:
        dts = article.find('span', class_="tm-article-snippet__datetime-published").find('time').get('title')
        titles = article.find('h2', class_="tm-article-snippet__title tm-article-snippet__title_h2").find('span').text
        href = article.find('a').attrs.get('href')
        print(dts, titles, URL + href)

