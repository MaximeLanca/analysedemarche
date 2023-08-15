##SCRAPING
##PROJET 01 - OpenClassrooms

import requests
from bs4 import BeautifulSoup

def allBookInAlLCategory():

    url='http://books.toscrape.com/catalogue/category/books_1/index.html'

    response= requests.get(url)

    # Connection check
    if response.ok:

        soup = BeautifulSoup(response.text, 'html.parser')
        
        """
        Book extraction in all category
        """
        categoryDataList = []
        categoryData = soup.findAll('a', href=True)
        print(categoryData)
        for li in categoryData:
            get_a=li.find('a')
        ##    get_href= get_a.find('href')
        ##print(get_href  )


 ##for i in table:
 ##  get_td = i.find_all('td')
 ##  for j in get_td:
 ##    get_ = j.find('a')['href'].strip().split('/')[-2]
 ##    link = "{}/{}".format(_baseurl_, get_)
 ##    print(link)


allBookInAlLCategory()