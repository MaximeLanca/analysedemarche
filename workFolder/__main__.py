##SCRAPING
##PROJET 01 - OpenClassrooms
from workFolder.book_informations import connection_check_url, get_book_informations_in_html_page
from workFolder.extraction_books_all_categories import select_all_categories
from workFolder.tools import import_selected_picture, data_books_extraction_to_csv

select_all_categories()
get_book_informations_in_html_page()
import_selected_picture()
data_books_extraction_to_csv()




