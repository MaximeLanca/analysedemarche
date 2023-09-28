# Projet 02 d'OPC 

## Etat des lieux du dépot sur GitHub

Dans le dossier workfolder:
 - init.py --> non utlisé dans l'application
 - main.py --> Démarage de l'application
 - book_information.py --> Cherche et transforme les informations des livres
 - constants.py --> Contient les constentes
 - extraction_url_books.py --> chercher les url des pages "catégories" et les url des livres
 - save.py --> enregistres les informations des lirves
 - scraping.py --> scrapîng des pages web

## Installation du programme 

1. Utiliser le fichier requirements.txt, pour télécharger les dépendances utlisées. La commande à utliser dans le terminal est : pip install -r requirements.txt

2. Dans le fichier workFolder, Démarrer l'application avec la commande: python3 __main__.py

3. Après d'avoir démarrer le projet, le programme analysera tous les livres automatiquement sur le site "https://books.toscrape.com/" déja indiqué dans une variable appelée "BOOKS_TOSCRAPE_URL".

4. Un dossier "Output" sera crée après la finalisation du programme ou un arret manuel dans le terminal. L'emplacement de dossier sera à la racine de l'application
Dans ce dossier "Output", vous trouverez un fichier .csv avec toutes les informations des livres du sites et les images des livres dans un dossier sous-ajacent appelé "pictures"


