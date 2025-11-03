from data import demo_data
from list_CRUD import *
from books import books

def print_info():
    print("Pasirinkite, ką norite daryti")
    print("1. Peržiūrėti bibliotekos autorius ir knygas")
    print("2. Pridėti naują autoriu")
    print("3. Redaguoti autoriu")
    print("4. Ištrinti autoriu")
    print("5. Išeiti iš parduotuvės")

authors = demo_data()
books = books()
id_counter = 3
book_id_counter = 3

while True:
    print_info()
    option = input()
    match option:
        case "1":
            print("1. Peržiūrėti bibliotekos autorius ir knygas")
            print_authors(authors)
            print_books(books)
        case "2":
            id_counter, book_id_counter = add_author(id_counter,book_id_counter, authors,books)
        case "3":
            edit_author(authors,books)
        case "4":
            delete_author(authors)
        case "5":
            print("5. Jus pasirinkote iseiti is bibliotekos")
            break
        case _:  # defaultas, kai ivedama belekas
            print("Pasitikrinkite ka ivedete")



