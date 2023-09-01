import csv
import re
from urllib.parse import urljoin

from workFolder.scraping import connection_check_url
from workFolder.tools import import_selected_picture


def get_book_informations_in_html_page(url_compiled: str):
    """return a tuple containing book information"""
    soup = connection_check_url(url_compiled)
    get_book_availability = soup.find('p', class_='instock availability').text.strip
    get_rating_book = soup.find('p', class_='star-rating')
    get_class_html_tag = get_rating_book['class']
    dictionary_for_check_rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', '<Five': '5/5'}
    for a in dictionary_for_check_rating:
        if a == get_class_html_tag[-1]:
            book_rating_value_dictionary = dictionary_for_check_rating[get_class_html_tag[-1]]
            break
    else:
        print('--Rating book error--')

    get_books_informations_list = {}
    for tr in soup.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        get_books_informations_list[th.text] = td.text

    get_description_book = (soup.find('p', class_=False)).text

    tag_href_list = []
    get_category_book = soup.find_all(href=re.compile('index.html'))
    for a in get_category_book:
        tag_href_list.append(a.text)

    get_book_title = soup.find('h1').text

    get_picture_book = soup.find('img')

    get_picture_link_book = urljoin(url_compiled, get_picture_book.get('src'))

    gathering_book_informations = [get_book_availability, get_books_informations_list,
                                   get_description_book, tag_href_list[3], get_book_title,
                                   book_rating_value_dictionary, get_picture_link_book]

    import_selected_picture(gathering_book_informations)
    data_books_extraction_to_csv(gathering_book_informations)


def data_books_extraction_to_csv(recovery_book_information_from_tuple: tuple):
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
                         'Category book': recovery_book_information_from_tuple[3],
                         'Review_rating': recovery_book_information_from_tuple[5],
                         'Picture URL': recovery_book_information_from_tuple[6]
                         })
    print(f'--- Successful exctraction of "{recovery_book_information_from_tuple[4]}" books informations ---')

