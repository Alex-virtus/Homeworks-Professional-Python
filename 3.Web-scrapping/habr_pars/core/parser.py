from bs4 import BeautifulSoup
from config.settings import BASE_URL


def get_articles_list(soup: BeautifulSoup) -> list:
    return soup.select('div.tm-article-snippet')


def extract_article_info(article) -> dict:
    link = BASE_URL + article.select_one('a.tm-title__link')['href']
    title = article.select_one('a.tm-title__link').text.strip()
    date_tag = article.find('time')
    date = date_tag['datetime'] if date_tag else 'unknown'
    preview = article.get_text().lower()
    return {'date': date, 'title': title, 'link': link, 'preview': preview}


def get_article_body(soup: BeautifulSoup) -> str:
    body = soup.select_one('div.tm-article-body')
    return body.get_text().lower() if body else ''
