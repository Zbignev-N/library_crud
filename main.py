authors = [
    {
        'id': 1,
        'name': 'J.K',
        'surname': 'Rowling',
        'book': 'Goblet of Fire'
    },
    {
        'id': 2,
        'name': 'Andrzej',
        'surname': 'Sapkowski',
        'book': 'the Witcher: The Lesser Evil'

    },
    {
        'id': 3,
        'name': 'Robert',
        'surname': 'Kirkman',
        'book': 'Invincible Volume 1'

    }
]
id_counter = 3
while  True:
    print("Pasirinkite, ką norite daryti")
    print("1. Peržiūrėti bibliotekos knygas")
    print("2. Pridėti naują autoriu")
    print("3. Redaguoti autoriu")
    print("4. Ištrinti autoriu")
    print("5. Išeiti iš parduotuvės")

    option = input()
    match option:
        case "1":
            print("1. Peržiūrėti bibliotekos knygas")
            for item in authors:
                print(item)
        case "2":
            print("2. Pridėti autoriaus varda")
            name = input()
            print("iveskite autoriaus pavarde")
            surname = input()
            print("iveskite autoriaus knyga")
            book = input()
            id_counter += 1
            item = {'id': id_counter, "name": name,"surname": surname,"book": book}
            authors.append(item)

        case "3":
            print("Jus pasirinkote redaguoti autoriu")
            print("irasykite autoriaus id kuria norite redaguoti")
            edit_id = input()
            for i, item in enumerate(authors):
                if str(item['id']) == edit_id:
                    print(item)
                    print("iveskite autoriaus varda")
                    authors[i]['name'] = input()
                    print("iveskite prekes tipa")
                    authors[i]['surname'] = input()
                    print("iveskite prekes kaina")
                    authors[i]['book'] = input()
        case "4":
            print(" Jus pasirinkote pasalinti preke")
            print(" Irasykite autoriaus id kuria norite pasalinti")
            del_id = input()
            for item in authors:
                if str(item['id']) == del_id:
                    authors.remove(item)
                    break
        case "5":
            print("5. Jus pasirinkote iseiti is bibliotekos")
            break
        case _:  # defaultas, kai ivedama belekas
            print("Pasitikrinkite ka ivedete")

