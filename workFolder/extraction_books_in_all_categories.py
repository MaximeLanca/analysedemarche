##SCRAPING
##PROJET 01 - OpenClassrooms
import re

from __init__ import connection_check_url
from constents import books_toscrape_url
from book_informations import get_book_informations_in_html_page

def select_all_url_categories() -> list:
    reconstitution_url = []
    soup = connection_check_url(books_toscrape_url)
    for a in soup.find_all(href=re.compile("catalogue/category/books")):
        reconstitution_url.append(books_toscrape_url + a['href'])
    #print(reconstitution_url)
    return reconstitution_url
def extraction_books_in_each_categories(reconstitution_url : list):
    for url_selection in reconstitution_url:
    soup=connection_check_url(url_selection)
