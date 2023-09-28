##SCRAPING
##PROJET 02 - OpenClassrooms
from urllib.parse import urljoin

from scraping import connection_url
from constants import BOOKS_TOSCRAPE_URL
from book_informations import get_book_informations


def get_all_url_categories():
    """get book link from list for scraping"""
    soup = connection_url(BOOKS_TOSCRAPE_URL)
    categories_url = []
    for link in soup.find('ul', class_='nav nav-list').find('ul').find_all('a'):
        url = BOOKS_TOSCRAPE_URL + link['href']
        categories_url.append(url)

        soup = connection_url(url)
        try:
            current_category_page = soup.find('ul', class_='pager').find('li', class_='current')
            current_category_page = current_category_page.text.split()
            total_pages_numbers = current_category_page[3]
            for page_number in range(2, (int(total_pages_numbers)+1)):
                page_url = url.replace('index', f'page-{page_number}')
                categories_url.append(page_url)
                print(f"Fetched page {page_number} for category {page_url}")
        except:
            print("Analysis of the number of pages in each category : 1 pages to cover for one category")

    get_all_url_books(categories_url)


def get_all_url_books(categories_url):
    """get books links from list for scraping"""
    for category_url in categories_url:
        soup = connection_url(category_url)
        for books_link in soup.find('ol', class_='row').find_all('a', title=True):
            get_book_informations(urljoin(category_url, books_link['href']))



