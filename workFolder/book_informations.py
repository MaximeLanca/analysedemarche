import csv
from urllib.parse import urljoin
from workFolder.scraping import connection_url
from workFolder.save import save_picture


def get_book_informations(url_compiled: str) -> list:
    """return a list containing book information"""
    soup = connection_url(url_compiled)

    book_availability = soup.find('p', class_='instock availability').text.strip

    book_rating = soup.find('p', class_='star-rating')
    class_attribute = book_rating['class']
    check_rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', 'Five': '5/5'}
    for rating in check_rating:
        if rating == class_attribute[-1]:
            book_rating_value = check_rating[class_attribute[-1]]
            break
    else:
        print('--Rating book error--')

    product_informations = {}
    for tr in soup.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        product_informations[th.text] = td.text

    if (soup.find('p', class_=False)):
        book_description = (soup.find('p', class_=False)).text
    else:
        book_description = 'unavailable'

    href_tag = []
    book_category = soup.find('ul', class_='breadcrumb').find_all('a')
    for a in book_category:
        href_tag.append(a.text)

    book_title = soup.find('h1').text

    book_picture = soup.find('img')

    picture_link = urljoin(url_compiled, book_picture.get('src'))

    book_informations = [book_availability, product_informations, book_description, href_tag[2], book_title,
                         book_rating_value, picture_link]

    save_picture(book_informations[4], book_informations[6])
    save_books_inforations_in_csv_file(book_informations)
    return book_informations


def csv_file_creation():
    with open('../output/books_informations.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'UPC', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Number_available',
                      'Product description', 'Category book', 'Review_rating', 'Picture URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def save_books_inforations_in_csv_file(recovery_book_information: list):
    """csv extraction file"""
    books_informations_dict = recovery_book_information[1]
    with open('../output/books_informations.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'UPC', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Number_available',
                      'Product description', 'Category book', 'Review_rating', 'Picture URL']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
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

