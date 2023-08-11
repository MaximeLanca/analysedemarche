##SCRAPING
##PROJET 01 - OpenClassrooms

import requests
from bs4 import BeautifulSoup

def pagehtml () :
    
    url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

    response = requests.get(url)

    if response.ok:
        # Connection check
        soup = BeautifulSoup(response.text, 'html.parser')

        """
        Data extraction Part one
        targeted information: Title, Availability, Review rating,
        """

        dataPartOne = []
        classAttribut = soup.find('div', {'class': 'col-sm-6 product_main'})
        for classAttributs in classAttribut :
            dataPartOne.append(classAttributs)

        # Title extraction from dataPartOne list
        titleBook = (str(dataPartOne[1])).replace('<h1>', '').replace('</h1>', '')

        # Availability book from dataPartOne list
        availability = str(dataPartOne[5]).splitlines()
        availableBook= availability[3]

        # Review rating from dataPartOne LIst
        listRating = str(dataPartOne[7])
        splitlinesList = listRating.splitlines()
        replaceElementList = str(splitlinesList[0]).replace('<p class="', '').replace('">', '').lower()
        listTransformation = replaceElementList.split()

        for words in listTransformation:
            match words:
                case 'one':
                    starNumbers = 1
                case 'two':
                    starNumbers = 2
                case 'three':
                    starNumbers = 3
                case 'four':
                    starNumbers = 4
                case 'five':
                    starNumbers = 5

        """
        Data extraction Part two
        targeted information: UPC, Product type, Price excl. tax, Price incl. tax, Tax, Number of review
        """
        dataPartTwo = {}
        tdAttribute = soup.findAll('table')
        for trs in tdAttribute:
            tr = trs.findAll('tr')

            for ths in tr:
                th = ths.find('th')
                td = ths.find('td')
                dataPartTwo[th.text] = td.text

        # Picture extraction
        picture = soup.find('img')

        # Product description extraction
        description = soup.find('div', {'id': 'content_inner'}).findAll('p')
        dataListForProductDescription = []
        for a in description:
            dataListForProductDescription.append(a)
        productDescription = dataListForProductDescription[3].text.replace(',', '')

        # category extraction
        categoryExtraction = soup.findAll('a')
        dataListForCategory = []
        for a in categoryExtraction:
            dataListForCategory.append(a)

        # csv.file creation
        with open('Information_du_livre.csv', 'w') as outf:
            outf.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url\n')
            outf.write(str(url) + ',' + dataPartTwo['UPC'] + ' , ' + titleBook + ',' + dataPartTwo['Price (excl. tax)'] + ',' + dataPartTwo['Price (incl. tax)'] + ',' + availableBook + ',' + productDescription + ',' + categoryExtraction[3].text + ',' + str(starNumbers) + ',' + picture.get('src'))