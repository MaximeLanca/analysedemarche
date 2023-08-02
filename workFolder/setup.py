##SCRAPING
##PROJET 01 - OpenClassrooms

import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

if response.ok:
    # Connection check
    soup = BeautifulSoup(response.text, 'html.parser')

    # Title extraction
    title = soup.find('title')

    # Product description extraction
    description = soup.find('div', {'id': 'content_inner'}).findAll('p')
    descriptionList = []
    for a in description :
        descriptionList.append(a)

    # Data extraction from HTML
    data = {}
    tdAttribute = soup.findAll('table')
    for trs in tdAttribute:
        tr = trs.findAll('tr')

        for ths in tr:
            th = ths.find('th')
            td = ths.find('td')
            data[th.text] = td.text

    #Picture extraction

    print('Titre de la page HTML :', title.text)
    print('Description du livre :' + '\n', descriptionList[3].text)
    print('Données de la page HTML :' + '\n', data)
