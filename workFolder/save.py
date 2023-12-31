import requests
from constants import FIELDNAMES
import csv
import os


def save_picture(book_title, upc_number, picture_link):
    """book picture import from html page"""
    picture = requests.get(picture_link).content
    with open(f"../output/pictures/{upc_number}.png", 'wb') as f:
        f.write(picture)
        print(f'--- Successful import of "{book_title}" picture ---')
        f.close()


def create_folders_and_csv_file():
    """folders and csv file creation"""
    try:
        os.mkdir('../output')
        os.mkdir('../output/pictures')
    except:
        print('Folders and files already exist. deliverables will be create in existing folder ')

    with open('../output/books_informations.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()


def save_books_informations_in_csv_file(book_informations: dict):
    """save information in csv file"""
    with open('../output/books_informations.csv', 'a', newline='', encoding='utf-8') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
       writer.writerow({'URL': book_informations['url'],
                        'UPC': book_informations['UPC'],
                        'Book Title': book_informations['title'],
                        'Price (excl. tax)': book_informations['Price (excl. tax)'],
                        'Price (incl. tax)': book_informations['Price (incl. tax)'],
                        'Number_available': book_informations['Availability'],
                        'Product description': book_informations['description'],
                        'Category book': book_informations['category'],
                        'Review_rating': book_informations['rating'],
                        'Picture URL': book_informations['picture_link'],
                        })
    print(f'--- Successful extraction of {book_informations["title"]} books informations ---')
    print("-----------------------------------------------------")

