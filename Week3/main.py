from custom_classes import MediaItem, Book, DVD, LibraryCollection


def main():
    my_library = LibraryCollection()

    book1 = Book("1984", "George Orwell", 328)
    movie_dvd1 = DVD("Recep Ivedik", "Gokhan Sahan", "156 mins")
    generic_item1 = MediaItem("Monopoly Game", "Hasbro")
    book2 = Book("Nutuk", "Mustafa Kemal Ataturk", 500)
    movie_dvd2 = DVD("The Matrix", "Wachowskis", "136 mins")
    generic_item2 = MediaItem("Chess Set", "Classic Games Inc.")


    my_library.add_item(book1)
    my_library.add_item(movie_dvd1)
    my_library.add_item(generic_item1)
    my_library.add_item(book2)
    my_library.add_item(movie_dvd2)
    my_library.add_item(generic_item2)
    print("Items added to the library.")

    # Put whichever items you want to check out here (1, 2, or more)
    items_to_checkout = [book1, movie_dvd1, book2, movie_dvd2]

    print("\nSimulating checkouts...")
    for item in items_to_checkout:
        status = item.checkout()
        print(f"Checked out '{item.title}' : {status}")

    print("\nAvailable titles remaining:")
    available = my_library.list_available()
    print(available)


if __name__ == "__main__":
    main()