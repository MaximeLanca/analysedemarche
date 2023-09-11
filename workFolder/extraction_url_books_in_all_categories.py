##SCRAPING
##PROJET 01 - OpenClassrooms

from scraping import connection_url
from workFolder.constants import books_toscrape_url, link_book_from_catalogue_web_page
from workFolder.book_informations import get_book_informations


def get_all_url_categories():
    soup = connection_url(books_toscrape_url)
    categories_url_reconstitution = []
    for category_link in soup.find('ul', class_='nav nav-list').find('ul').find_all('a'):
        categories_url_reconstitution.append(books_toscrape_url + category_link['href'])

    for categories_url_reconstitution in categories_url_reconstitution:
        soup = connection_url(categories_url_reconstitution)
        for books_links in soup.find('ol', class_='row').find_all('a', title=True):
            get_book_informations((link_book_from_catalogue_web_page + books_links['href'])
                                  .replace('../../../', ''))

