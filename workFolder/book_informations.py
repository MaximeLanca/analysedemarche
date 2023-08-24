import re

from __init__ import connection_check_url
from constents import url_book


def get_book_informations_in_html_page() -> tuple:
    """return a tuple containing book information"""
    soup = connection_check_url(url_book)
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

    get_picture_link_book = get_picture_book.get('src')

    gathering_book_informations = [get_book_availability, get_books_informations_list,
                                   get_description_book, tag_href_list[3], get_book_title,
                                   book_rating_value_dictionary, get_picture_link_book]

    return gathering_book_informations


