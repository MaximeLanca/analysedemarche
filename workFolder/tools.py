import requests
import io
from PIL import Image
from pathlib import Path
import csv


def import_selected_picture(recovery_book_information_from_tuple: tuple):
    """book picture import from html page"""
    if recovery_book_information_from_tuple[6]:
        web_link_book = recovery_book_information_from_tuple[6]
        picture_url_book = requests.get(web_link_book).content
        io_module_conversion = io.BytesIO(picture_url_book)
        image = Image.open(io_module_conversion).convert("RGB")
        file_path = Path("../load_picture", recovery_book_information_from_tuple[4] + '.png')
        image.save(file_path, "PNG", quality=80)
        print(f'--- Successful import of "{recovery_book_information_from_tuple[4]}" picture ---')
