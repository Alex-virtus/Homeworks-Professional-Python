import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


def get_headers():
    return Headers(browser='chrome', os='linux').generate()

def get_soup(url: str) -> BeautifulSoup:
    for _ in range(3):
        try:
            response = requests.get(url, headers=get_headers())
            response.raise_for_status()
            return BeautifulSoup(response.text, 'lxml')
        except requests.RequestException:
            continue
    raise RuntimeError(f'Не удалось загрузить страницу: {url}')
