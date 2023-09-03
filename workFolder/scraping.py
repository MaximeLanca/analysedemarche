from bs4 import BeautifulSoup
import requests


def connection_url(url: str) -> BeautifulSoup:
    """return soup argument of BeautifulSoup"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

