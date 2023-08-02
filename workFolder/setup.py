##SCRAPING
##PROJET 01 - OpenClassrooms
import item as item
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

if response.ok:
    # Connection check
    soup = BeautifulSoup(response.text, 'html.parser')

    # Title extraction
    title = soup.find('title')
    print('Titre de la page HTML :', title.text)

    # Product description extraction
    description = soup.find('div', {'id': 'content_inner'}).findAll('p')
    descriptionList = []
    for a in description :
        descriptionList.append(a)
    print('Description du livre :' + '\n', descriptionList[3].text)

    # Data extraction from HTML
    data = {}
    tdAttribute = soup.findAll('table')
    for trs in tdAttribute:
        tr = trs.findAll('tr')

        for ths in tr:
            th = ths.find('th')
            td = ths.find('td')
            data[th.text] = td.text
    print('Données de la page HTML :' + '\n', data)

    # Picture extraction
    picture = soup.find('img')
    print('Lien de la converture du livre :' + '\n', picture.get('src'))

    #csv.file creation
    with open('Information_du_livre.csv', 'w') as outf:
        outf.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url\n')
        outf.write(url + ',' + data['UPC'] + ',' + title.text + ',' + data['Price (excl. tax)'] + ',' + data['Price (incl. tax)'] + ',' + data['Availability'] + ',' + descriptionList[3].text + ',' + picture.get('src'))

    
##product_page_url
##universal_ product_code (upc)
##title
##price_including_tax
##price_excluding_tax
##number_available
##product_description
##category
##review_rating
##image_url