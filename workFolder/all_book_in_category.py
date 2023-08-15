##SCRAPING
##PROJET 01 - OpenClassrooms
from bs4 import BeautifulSoup
import requests


def allbookincategory():

    url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'
    response = requests.get(url)

    # Connection check
    if response.ok:

        soup = BeautifulSoup(response.text, 'html.parser')
        bookInCategory = []
        category = soup.findAll('h3')

        for a in category:
            aText = a.text
            bookInCategory.append(aText)
        print(bookInCategory)

allbookincategory()