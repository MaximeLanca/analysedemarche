##SCRAPING
##PROJET 01 - OpenClassrooms

import requests
from bs4 import BeautifulSoup

url='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response= requests.get(url)
print(response)



