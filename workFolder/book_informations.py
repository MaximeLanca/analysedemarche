import csv
from urllib.parse import urljoin

from workFolder.scraping import connection_url
from workFolder.save import get_import_selected_picture


def get_book_informations_in_html_page(url_compiled: str):
    """return a tuple containing book information"""
    soup = connection_url(url_compiled)
    book_availability = soup.find('p', class_='instock availability').text.strip
    book_rating = soup.find('p', class_='star-rating')
    class_html_tag = book_rating['class']
    dictionary_for_check_rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', 'Five': '5/5'}
    for a in dictionary_for_check_rating:
        if a == class_html_tag[-1]:
            book_rating_value_dictionary = dictionary_for_check_rating[class_html_tag[-1]]
            break
    else:
        print('--Rating book error--')

    product_informations_dict = {}
    for tr in soup.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        product_informations_dict[th.text] = td.text

    if (soup.find('p', class_=False)):
        description_book = (soup.find('p', class_=False)).text
    else:
        description_book = 'unavailable'

    href_tag_list = []
    book_category = soup.find('ul', class_='breadcrumb').find_all('a')
    for a in book_category:
        href_tag_list.append(a.text)

    book_title = soup.find('h1').text

    book_picture = soup.find('img')

    picture_link_book = urljoin(url_compiled, book_picture.get('src'))

    gathering_book_informations = [book_availability, product_informations_dict,
                                   description_book, href_tag_list[2], book_title,
                                   book_rating_value_dictionary, picture_link_book]

    get_import_selected_picture(gathering_book_informations[4], gathering_book_informations[6])
    get_data_books_extraction_to_csv(gathering_book_informations)


def get_data_books_extraction_to_csv(recovery_book_information: list):
    """csv extraction file"""
    books_informations_dict = recovery_book_information[1]
    with open('../output/books_informations.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'UPC', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Number_available',
                      'Product description', 'Category book', 'Review_rating', 'Picture URL']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'URL': recovery_book_information[6],
                         'UPC': books_informations_dict['UPC'],
                         'Book Title': recovery_book_information[4],
                         'Price (excl. tax)': books_informations_dict['Price (excl. tax)'],
                         'Price (incl. tax)': books_informations_dict['Price (incl. tax)'],
                         'Number_available': books_informations_dict['Availability'],
                         'Product description': recovery_book_information[2],
                         'Category book': recovery_book_information[3],
                         'Review_rating': recovery_book_information[5],
                         'Picture URL': recovery_book_information[6],
                         })
    print(f'--- Successful extraction of "{recovery_book_information[4]}" books informations ---')

