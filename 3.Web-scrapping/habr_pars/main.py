from config.settings import URL_ARTICLES, KEYWORDS
from core.fetcher import get_soup
from core.parser import get_articles_list, extract_article_info, get_article_body
from core.utils import contains_keywords


def main():
    results = []
    soup = get_soup(URL_ARTICLES)
    articles = get_articles_list(soup)

    for article in articles:
        info = extract_article_info(article)

        if contains_keywords(info['preview'], KEYWORDS):
            print(f'{info['date']} - {info['title']} - {info['link']}')
            results.append((info['date'], info['title'], info['link']))
            continue

        article_soup = get_soup(info['link'])
        article_text = get_article_body(article_soup)
        if contains_keywords(article_text, KEYWORDS):
            print(f'{info['date']} - {info['title']} - {info['link']}')
            results.append((info['date'], info['title'], info['link']))


if __name__ == '__main__':
    main()