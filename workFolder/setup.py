##SCRAPING
##PROJET 01 - OpenClassrooms

import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

if response.ok:
    # Vérification de la connexion
    soup = BeautifulSoup(response.text)

    #Recupere le titre du livre
    title = soup.find('title')
    print(title.text)

    #Récuperation des données de la page HTML
    data = {}
    tdAttribute = soup.findAll('table')
    for trs in tdAttribute:
        tr = trs.findAll('tr')
        for ths in tr:
            th = ths.find('th')
            td = ths.find('td')
            ##print(str(th) + ' : ' + str(td) + '\n')


