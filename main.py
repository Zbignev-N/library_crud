from data import demo_data
from list_CRUD import *

def print_info():
    print("Pasirinkite, ką norite daryti")
    print("1. Peržiūrėti bibliotekos knygas")
    print("2. Pridėti naują autoriu")
    print("3. Redaguoti autoriu")
    print("4. Ištrinti autoriu")
    print("5. Išeiti iš parduotuvės")

authors = demo_data()
id_counter = 3
while True:
    print_info()
    option = input()
    match option:
        case "1":
            print("1. Peržiūrėti bibliotekos knygas")
            print_authors(authors)
        case "2":
            id_counter = add_author(id_counter, authors)
        case "3":
            edit_author(authors)
        case "4":
            delete_author(authors)
        case "5":
            print("5. Jus pasirinkote iseiti is bibliotekos")
            break
        case _:  # defaultas, kai ivedama belekas
            print("Pasitikrinkite ka ivedete")

