from custom_classes import MediaItem, Book, DVD, LibraryCollection


def main():
    my_library = LibraryCollection()

    book1 = Book("1984", "George Orwell", 328)
    movie_dvd = DVD("Recep Ivedik", "Gokhan Sahan", "156 mins")
    generic_item = MediaItem("Monopoly Game", "Hasbro")

    my_library.add_item(book1)
    my_library.add_item(movie_dvd)
    my_library.add_item(generic_item)
    print("Items added to the library.")

    # Put whichever items you want to check out here (1, 2, or more)
    items_to_checkout = [book1, movie_dvd]

    print("\nSimulating checkouts...")
    for item in items_to_checkout:
        status = item.checkout()
        print(f"Checked out '{item.title}' : {status}")

    print("\nAvailable titles remaining:")
    available = my_library.list_available()
    print(available)


if __name__ == "__main__":
    main()