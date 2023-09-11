import requests


def save_picture(book_name, picture_link):
    """book picture import from html page"""
    picture = requests.get(picture_link).content
    with open(f"../load_picture/{book_name}.png", 'wb') as f:
        f.write(picture)
        print(f'--- Successful import of "{book_name}" picture ---')
        f.close()


