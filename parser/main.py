import requests
from bs4 import BeautifulSoup
from time import sleep


HEADERS = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"}

BASE_URL = "https://pstu.ru"

def get_news_urls(pages = 2):
    for count in range(1, pages + 1):
        url = f"{BASE_URL}/news/current/?p={count}"
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_= "news_item")

        for i in data:
            news_url = "https://pstu.ru" + i.find("a").get("href")
            yield news_url


def parse_news(news_url):
    response = requests.get(news_url, headers=HEADERS)
    sleep(3)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="content")

    name = data.find("h1").text.strip()
    text_news = data.find("div", class_="text").text.strip()

    print(f"\nЗаголовок: {name}\n")
    print(f"Текст:\n{text_news}\n")


for news_url in get_news_urls(1):
    parse_news(news_url)