##SCRAPING
##PROJET 01 - OpenClassrooms
import re
from __init__ import connection_check_url
from constents import books_toscrape_url

def select_all_categories():
    list = []
    soup = connection_check_url(books_toscrape_url)
    for a in soup.find_all(href=re.compile("catalogue/category/books")):
        list.append(a)
    #print(list)



