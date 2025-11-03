from books import books

# books = books()


def print_authors(authors):
    for author in authors:
        print(f"{author['id']}. Vardas - \"{author['name']}\", Pavardė - {author['surname']}")

def print_books(books):
    for book in books:
        print(f"{book['id']}. {book['title']} - {book['price']}€")

def add_author(id_counter,book_id_counter,authors,books):
    print("2. Pridėti autoriaus varda")
    name = input()
    print("Iveskite autoriaus pavarde")
    surname = input()
    print("Iveskite autoriaus knyga")
    book = input()
    print("Iveskite prekes kaina")
    price = float(input())
    id_counter += 1
    book_id_counter += 1
    author = {f'id': id_counter, "name": name, "surname": surname}
    authors.append(author)
    books.append({'id':book_id_counter, "title": book, "price": price})
    return id_counter, book_id_counter
def edit_author(authors,books):
    print("Jus pasirinkote redaguoti autoriu")
    print_authors(authors)
    print_books(books)
    print("Irasykite autoriaus id kuria norite redaguoti")
    edit_id = input()
    for i, author in enumerate(authors):
        if str(author['id']) == edit_id:
            print(author)
            print("Iveskite autoriaus varda")
            authors[i]['name'] = input()
            print("Iveskite autoriaus pavarde")
            authors[i]['surname'] = input()
            print("Iveskite autoriaus knyga")
            # authors[i]['title'] = input()
            # print("Iveskite prekes kaina")
            # authors[i]['price'] = float(input())

def delete_author(authors):
    print(" Jus pasirinkote pasalinti preke")
    print_authors(authors)
    print(" Irasykite autoriaus id kuria norite pasalinti")
    del_id = input()
    found = False
    for author in authors:
        if str(author['id']) == del_id:
            found = True
            print_authors(authors)
            print(f"Ar tikrai norite ištrinti autorių: {author['name']}?")
            print("Spauskite 0 - atšaukti, 1 - trinti")
            choice = input().strip()
            if choice == "1":
                authors.remove(author)
                print("Autorius pašalintas!")
            else:
                print("Veiksmas atšauktas.")
            break







        # if not found:
        #     print("Autoriaus su tokiu ID nerasta.")

        # print_authors(authors)
            # if input() == 0:
            #     break
            # authors.remove(author)
            # break