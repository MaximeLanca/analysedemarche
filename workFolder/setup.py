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

    #Data extraction part one from HTML
    dataPartOne = []
    classAttribut = soup.find('div', {'class': 'col-sm-6 product_main'})
    for classAttributs in classAttribut :
        dataPartOne.append(classAttributs)

    titleBook = (str(dataPartOne[1])).replace('<h1>', '').replace('</h1>', '')

    availability = str(dataPartOne[5]).splitlines()
    availableBook= availability[3]
    print(availableBook)


    # Product description extraction
    description = soup.find('div', {'id': 'content_inner'}).findAll('p')
    descriptionList = []
    for a in description:
        descriptionList.append(a)
    productDescription = descriptionList[3].text.replace(',', '')
    print(productDescription)

    # Data extraction part two from HTML
    dataPartTwo = {}
    tdAttribute = soup.findAll('table')
    for trs in tdAttribute:
        tr = trs.findAll('tr')

        for ths in tr:
            th = ths.find('th')
            td = ths.find('td')
            dataPartTwo[th.text] = td.text
    #print('Données de la page HTML :' + '\n', data)

    # Picture extraction
    picture = soup.find('img')
    # print('Lien de la converture du livre :' + '\n', picture.get('src'))

    # review_rating extraction
    reviewRating = soup.find_all('p')
    listRating = str(reviewRating[2])
    splitlinesList = listRating.splitlines()
    replaceElementList = str(splitlinesList[0]).replace('<p class="', '').replace('">', '').lower()
    listTransformation= replaceElementList.split()

    for words in listTransformation:

        match words:
            case 'one':
                starNumbers= 1
            case 'two':
                starNumbers= 2
            case 'three':
                starNumbers= 3
            case 'four':
                starNumbers= 4
            case 'five':
                starNumbers= 5

    # category extraction


    # csv.file creation
    with open('Information_du_livre.csv', 'w') as outf:
        outf.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url\n')
        outf.write(str(url) + ',' + dataPartTwo['UPC'] + ' , ' + titleBook + ',' + dataPartTwo['Price (excl. tax)'] + ',' + dataPartTwo['Price (incl. tax)'] + ',' + availableBook + ',' + productDescription)

        ##outf.write(str(url) + ',' + data['UPC'] + ',' + str(title.text) + ',' + data['Price (excl. tax)'] + ',' + data['Price (incl. tax)'] + ',' + data['Availability'] + ',' + str(descriptionList[3].text) + ',' + str(starNumbers) + ',' + picture.get('src'))

    
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