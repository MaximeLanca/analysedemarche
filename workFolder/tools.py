import requests
import io
from PIL import Image
from pathlib import Path
import csv
from urllib.parse import urljoin

from constents import url_book
from book_informations import get_book_informations

recovery_book_information_from_tuple = get_book_informations()
#recovery_book_information_from_tuple[2]
def import_selected_picture():
    if recovery_book_information_from_tuple[6]:
        web_link_book = urljoin(url_book, recovery_book_information_from_tuple[6])
        picture_url_book = requests.get(web_link_book).content
        image_file_book_in_page_web = io.BytesIO(picture_url_book)
        image = Image.open(image_file_book_in_page_web).convert("RGB")
        file_path = Path("../load_picture", recovery_book_information_from_tuple[4] + '.png')
        image.save(file_path, "PNG", quality=80)

# csv.file creation
def data_books_extraction_to_csv():
   with open('../output/data_book.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['URL', 'UPC', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Number_available',
                  'Product description', 'Category book', 'Review_rating', 'Picture URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'URL': recovery_book_information_from_tuple[6],
                     'UPC': recovery_book_information_from_tuple[1].get_books_informations['UPC'],
                     'Book Title': recovery_book_information_from_tuple[4],
                     'Price (excl. tax)': recovery_book_information_from_tuple[1].get_books_informations
                     ['Price (excl. tax)'],
                     'Price (incl. tax)': recovery_book_information_from_tuple[1].get_books_informations
                     ['Price (incl. tax)'],
                     'Number_available': recovery_book_information_from_tuple[1].book_availability_in_page_web['Availability'],
                     'Product description': recovery_book_information_from_tuple[2],
                     'Category book': recovery_book_information_from_tuple[1].get_category_in_page['Product Type'],
                     'Review_rating': recovery_book_information_from_tuple[5],
                     'Picture URL': recovery_book_information_from_tuple[6]
                     })


