import csv
import re
from urllib.parse import urljoin

from workFolder.scraping import connection_url
from workFolder.save import get_import_selected_picture


def get_book_informations_in_html_page(url_compiled: str):
    """return a tuple containing book information"""
    soup = connection_url(url_compiled)
    book_availability = soup.find('p', class_='instock availability').text.strip
    rating_book = soup.find('p', class_='star-rating')
    class_html_tag = rating_book['class']
    dictionary_for_check_rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', 'Five': '5/5'}
    for a in dictionary_for_check_rating:
        if a == class_html_tag[-1]:
            book_rating_value_dictionary = dictionary_for_check_rating[class_html_tag[-1]]
            break
    else:
        print('--Rating book error--')

    books_informations_dict = {}
    for tr in soup.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        books_informations_dict[th.text] = td.text

    if (soup.find('p', class_=False)):
        description_book = (soup.find('p', class_=False)).text
    else:
        description_book = 'unavailable'

    href_tag_list = []
    category_book = soup.find('ul', class_='breadcrumb').find_all('a')
    for a in category_book:
        href_tag_list.append(a.text)

    book_title = soup.find('h1').text

    picture_book = soup.find('img')

    picture_link_book = urljoin(url_compiled, picture_book.get('src'))

    gathering_book_informations = [book_availability, books_informations_dict,
                                   description_book, href_tag_list[2], book_title,
                                   book_rating_value_dictionary, picture_link_book]

    get_import_selected_picture(gathering_book_informations)
    data_books_extraction_to_csv(gathering_book_informations)


def data_books_extraction_to_csv(recovery_book_information: list):
    """csv extraction file"""
    get_dictionary_in_tuple = recovery_book_information[1]
    with open('../output/books_informations.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'UPC', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Number_available',
                      'Product description', 'Category book', 'Review_rating', 'Picture URL']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'URL': recovery_book_information[6],
                         'UPC': get_dictionary_in_tuple['UPC'],
                         'Book Title': recovery_book_information[4],
                         'Price (excl. tax)': get_dictionary_in_tuple['Price (excl. tax)'],
                         'Price (incl. tax)': get_dictionary_in_tuple['Price (incl. tax)'],
                         'Number_available': get_dictionary_in_tuple['Availability'],
                         'Product description': recovery_book_information[2],
                         'Category book': recovery_book_information[3],
                         'Review_rating': recovery_book_information[5],
                         'Picture URL': recovery_book_information[6],
                         })
    print(f'--- Successful extraction of "{recovery_book_information[4]}" books informations ---')

