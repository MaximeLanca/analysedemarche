from bs4 import BeautifulSoup
import requests

from workFolder.constents import url_book


def connection_check_url() -> BeautifulSoup:
    response = requests.get(url_book)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def get_book_informations() -> tuple:
    """The fonction returns main informations of book"""
    soup = connection_check_url()
    get_book_availability_in_page_web = (soup.find('p', class_='instock availability').text).strip
    get_rating_book_in_page = soup.find('p', class_='star-rating')
    get_class_html_tag_of_rating = get_rating_book_in_page['class']
    dictionary_for_search_rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', '<Five': '5/5'}
    for a in dictionary_for_search_rating:
        if a == get_class_html_tag_of_rating[-1]:
            book_rating_value_dictionary = dictionary_for_search_rating[get_class_html_tag_of_rating[-1]]
            break
    else:
        print('--Rating book error--')

    get_books_informations = {}
    for tr in soup.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        get_books_informations[th.text] = td.text

    get_description_book_in_page = (soup.find('p', class_=False)).text

    get_category_in_page = soup.find('a', href="../category/books/poetry_23/index.html")

    get_book_title_in_page = soup.find('h1').text

    picture_in_page_web = soup.find('img')
    web_link_book = picture_in_page_web.get('src')


    gathering_book_informations = [get_book_availability_in_page_web, get_books_informations,
                                   get_description_book_in_page, get_category_in_page, get_book_title_in_page,
                                   book_rating_value_dictionary, web_link_book]


    return gathering_book_informations

