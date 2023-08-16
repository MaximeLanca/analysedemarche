##SCRAPING
##PROJET 01 - OpenClassrooms

import requests
import io
from PIL import Image
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup


def book_informations():
    """
    The fonction returns main informations of book
    """
    url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

    response = requests.get(url)

    # Connection check
    if response.ok:

        soup = BeautifulSoup(response.text, 'html.parser')

        # Title extraction
        book_title = soup.title.text

        # Availability book
        book_availability = soup.find('p', class_='instock availability').text

        # Review rating book
        rating_system = {'<p class="star-rating One">': '1/5', '<p class="star-rating Two">': '2/5', '<p class="star-rating Three">': '3/5', '<p class="star-rating Four">': '4/5', '<p class="star-rating Five">': '5/5'}
        rating_book = str(soup.find('p', class_='star-rating')).splitlines()
        for i in range(0, 6):
                for a in rating_system:
                    if a == rating_book[i]:
                        break
                if i == 6:
                    print('--Rating book error--')

        # UPC book extraction
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
        #print(picture['src'])
        web_link_book = picture.get('src')
        if web_link_book:
            web_link_book = requests.compat.urljoin(url, web_link_book)

        picture_url_book = requests.get(web_link_book).content
        image_file_book = io.BytesIO(picture_url_book)
        image = Image.open(image_file_book).convert("RGB")
        file_path = Path("../load_picture", hashlib.sha1(picture_url_book).hexdigest()[:10] + ".png")
        image.save(file_path, "PNG", quality=80)

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
            outf.write(str(url) + ',' + dataPartTwo['UPC'] + ' , ' + book_title + ',' + dataPartTwo['Price (excl. tax)'] + ',' + dataPartTwo['Price (incl. tax)'] + ',' + book_availability + ',' + productDescription + ',' + categoryExtraction[3].text + ',' + rating_book[i] + ',' + web_link_book)
    else:
        print('-- Connexion server error --')

book_informations()
