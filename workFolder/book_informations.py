##SCRAPING
##PROJET 01 - OpenClassrooms

import requests
import io
from PIL import Image
import hashlib
from pathlib import Path
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def book_informations_from_page():
    """
    The fonction returns main informations of book
    """
    url_book = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    response = requests.get(url_book)
    # Connection check
    if response.ok:

        soup = BeautifulSoup(response.content, 'html.parser')

        # Title extraction from web site
        book_title_in_page_web = soup.find('h1').text

        # Availability book
        book_availability_in_page_web = (soup.find('p', class_='instock availability').text).strip


        # Review rating book
        dictionary_for_search_rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', '<Five': '5/5'}
        rating_book_in_page_web = soup.find('p', class_='star-rating')
        class_values_of_rating = rating_book_in_page_web['class']

        for a in dictionary_for_search_rating:
            if a == class_values_of_rating[-1]:
                rating_book_extract_of_dictionary = dictionary_for_search_rating[class_values_of_rating[-1]]
                break
        else:
            print('--Rating book error--')

        # book extraction
        dictionary_for_put_book_information_from_page_web = {}
        for tr in soup.find_all('tr'):
            th = tr.find('th')
            td = tr.find('td')
            dictionary_for_put_book_information_from_page_web[th.text] = td.text

        # Picture extraction
        picture_in_page_web = soup.find('img')
        web_link_book = picture_in_page_web.get('src')
        if web_link_book:
            web_link_book = urljoin(url_book, web_link_book)

        picture_url_book = requests.get(web_link_book).content
        image_file_book_in_page_web = io.BytesIO(picture_url_book)
        image = Image.open(image_file_book_in_page_web).convert("RGB")
        file_path = Path("../load_picture", hashlib.sha1(picture_url_book).hexdigest()[:10] + ".png")
        image.save(file_path, "PNG", quality=80)

        # Product description extraction
        description_book_in_page_web = (soup.find('p', class_=False)).text

        # category extraction
        category_in_page_web = soup.find('a', href="../category/books/poetry_23/index.html")
        print(category_in_page_web.text)

        # csv.file creation
        with open('../output/data_book.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['URL', 'UPC', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Number_available',
                          'Product description', 'Category book', 'Review_rating', 'Picture URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'URL': url_book,
                             'UPC': dictionary_for_put_book_information_from_page_web['UPC'],
                             'Book Title': book_title_in_page_web,
                             'Price (excl. tax)': dictionary_for_put_book_information_from_page_web
                             ['Price (excl. tax)'],
                             'Price (incl. tax)': dictionary_for_put_book_information_from_page_web
                             ['Price (incl. tax)'],
                             'Number_available': book_availability_in_page_web,
                             'Product description': description_book_in_page_web,
                             'Category book': category_in_page_web.text,
                             'Review_rating': rating_book_extract_of_dictionary,
                             'Picture URL': web_link_book
                             })

    else:
        print('-- Connexion server error --')


book_informations_from_page()
