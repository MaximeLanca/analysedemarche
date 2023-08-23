import requests
import io
from PIL import Image
from pathlib import Path
import csv
from urllib.parse import urljoin

from constents import url_book
from book_informations import get_book_informations_in_html_page

recovery_book_information_from_tuple = get_book_informations_in_html_page()


def import_selected_picture():
    """book picture import from html page"""
    if recovery_book_information_from_tuple[6]:
        web_link_book = urljoin(url_book, recovery_book_information_from_tuple[6])
        picture_url_book = requests.get(web_link_book).content
        io_module_conversion = io.BytesIO(picture_url_book)
        image = Image.open(io_module_conversion).convert("RGB")
        file_path = Path("../load_picture", recovery_book_information_from_tuple[4] + '.png')
        image.save(file_path, "PNG", quality=80)
        print(f'--- Successful import of "{recovery_book_information_from_tuple[4]}" picture ---')


def data_books_extraction_to_csv():
    """csv extraction file"""
    get_dictionary_in_tuple = recovery_book_information_from_tuple[1]
    with open('../output/books_informations.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'UPC', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Number_available',
                      'Product description', 'Category book', 'Review_rating', 'Picture URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'URL': recovery_book_information_from_tuple[6],
                         'UPC': get_dictionary_in_tuple['UPC'],
                         'Book Title': recovery_book_information_from_tuple[4],
                         'Price (excl. tax)': get_dictionary_in_tuple['Price (excl. tax)'],
                         'Price (incl. tax)': get_dictionary_in_tuple['Price (incl. tax)'],
                         'Number_available': get_dictionary_in_tuple['Availability'],
                         'Product description': recovery_book_information_from_tuple[2],
                         'Category book': get_dictionary_in_tuple['Product Type'],
                         'Review_rating': recovery_book_information_from_tuple[5],
                         'Picture URL': recovery_book_information_from_tuple[6]
                         })
    print(f'--- Successful exctraction of "{recovery_book_information_from_tuple[4]}" books informations ---')

