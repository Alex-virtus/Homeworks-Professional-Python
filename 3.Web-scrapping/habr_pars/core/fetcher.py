import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


def get_headers():
    return Headers(browser='chrome', os='linux').generate()

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return BeautifulSoup(response.text, 'lxml')
