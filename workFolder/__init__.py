from bs4 import BeautifulSoup
import requests

from constents import url_book

url = url_book
def connection_check_url(url: str) -> BeautifulSoup:
    """return soup argument of BeautifulSoup"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

