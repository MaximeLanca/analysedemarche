from urllib.parse import urljoin
from workFolder.scraping import connection_url
from workFolder.save import save_picture
from workFolder.save import save_books_informations_in_csv_file


def get_book_informations(url_compiled: str) -> dict:
    """return a list containing book information"""
    book_informations = {}
    soup = connection_url(url_compiled)
    book_informations['url'] = url_compiled

    book_rating = soup.find('p', class_='star-rating')
    class_attribute = book_rating['class']
    check_rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', 'Five': '5/5'}
    for rating in check_rating:
        if rating == class_attribute[-1]:
            book_rating_value = check_rating[class_attribute[-1]]
            book_informations['rating'] = book_rating_value
            break
    else:
        print('--Rating book error--')

    for tr in soup.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        book_informations[th.text] = td.text

    if soup.find('p', class_=False):
        book_description = (soup.find('p', class_=False)).text
        book_informations['description'] = book_description
    else:
        book_informations['description'] = 'unavailable'

    href_tag = []
    book_category = soup.find('ul', class_='breadcrumb').find_all('a')
    for a in book_category:
        href_tag.append(a.text)
    book_informations['category'] = href_tag[2]

    book_title = soup.find('h1').text
    book_informations['title'] = book_title

    book_picture = soup.find('img')
    book_informations['picture'] = book_picture

    picture_link = urljoin(url_compiled, book_picture.get('src'))
    book_informations['picture_link'] = picture_link

    save_picture(book_informations['title'], book_informations['UPC'], book_informations['picture_link'])
    save_books_informations_in_csv_file(book_informations)

    return book_informations





