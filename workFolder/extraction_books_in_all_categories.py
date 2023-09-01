##SCRAPING
##PROJET 01 - OpenClassrooms
import re

from scraping import connection_check_url
from workFolder.constants import books_toscrape_url, link_book_from_catalogue_web_page


def select_all_url_categories() -> list:
    soup = connection_check_url(books_toscrape_url)
    categories_url_reconstitution = []
    for category_link in soup.find('ul', class_='nav nav-list').find('ul').find_all('a'):
        categories_url_reconstitution.append(books_toscrape_url + category_link['href'])
    books_url_reconstitution = []
    for links_from_categories_url_reconstitution in categories_url_reconstitution:
        soup = connection_check_url(links_from_categories_url_reconstitution)
        books_links_from_web_page = soup.find('ol', class_='row').find('h3').find('a')
        books_url_reconstitution.append((link_book_from_catalogue_web_page + books_links_from_web_page['href'])
                                        .replace('../../../', ''))
    return books_url_reconstitution

