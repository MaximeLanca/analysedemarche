import urllib

import requests
import io
from PIL import Image
from pathlib import Path


def get_import_selected_picture(book_name, web_link_book):
    """book picture import from html page"""
    picture_url_book = requests.get(web_link_book).content
    io_module_conversion = io.BytesIO(picture_url_book)
    image = Image.open(io_module_conversion).convert("RGB")
    file_path = Path("../load_picture", book_name + '.png')
    image.save(file_path, "PNG", quality=80)
   #try:
   #    picture_url_book = requests.get(web_link_book).content
   #    with urllib.request.urlopen(picture_url_book) as web_file:
   #        data = web_file.read()
   #        with open('../output/load_picture', mode='w') as local_file:
   #            local_file.write(data)
   #except urllib.error.URLError as e:
   #    print(e)
   #
   #print(f'--- Successful import of "{book_name}" picture ---')