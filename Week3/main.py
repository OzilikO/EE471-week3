from custom_classes import MediaItem

def main():
    
    book = MediaItem("1984", "George Orwell")
    movie = MediaItem("Interstellar", "Christopher Nolan")

    print("Initial Library Status:")
    print(book)
    print(movie)

    print("\nSimulating checkout...")
    
    checkout_message = book.checkout()
    print(checkout_message)

    print("\nUpdated Library Status:")
    print(book)
    print(movie)

if __name__ == "__main__":
    main()