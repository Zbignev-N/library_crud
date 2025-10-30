
def print_authors(authors):
    for author in authors:
        print(f"{author['id']}. Vardas - \"{author['name']}\", Pavardė - {author['surname']}, Knyga -"
              f" {author['book']} ")
def add_author(id_counter,authors):
    print("2. Pridėti autoriaus varda")
    name = input()
    print("iveskite autoriaus pavarde")
    surname = input()
    print("iveskite autoriaus knyga")
    book = input()
    id_counter += 1
    author = {'id': id_counter, "name": name, "surname": surname, "book": book}
    authors.append(author)
    return id_counter
def edit_author(authors):
    print("Jus pasirinkote redaguoti autoriu")
    print_authors(authors)
    print("irasykite autoriaus id kuria norite redaguoti")
    edit_id = input()
    for i, author in enumerate(authors):
        if str(author['id']) == edit_id:
            print(author)
            print("iveskite autoriaus varda")
            authors[i]['name'] = input()
            print("iveskite prekes tipa")
            authors[i]['surname'] = input()
            print("iveskite prekes kaina")
            authors[i]['book'] = input()
def delete_author(authors):
    print(" Jus pasirinkote pasalinti preke")
    print(" Irasykite autoriaus id kuria norite pasalinti")
    del_id = input()
    for author in authors:
        if str(author['id']) == del_id:
            print(author)
            print(" Spauskite 0 jeigu norite atsaukti, 1 jei norite trinti ")
            if input() == 0:
                break
            authors.remove(author)
            break