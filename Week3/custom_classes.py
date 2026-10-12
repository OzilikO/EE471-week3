class MediaItem:
    def __init__(self, title, author, is_available=True):
        # Initializes with title, author, and boolean is_available defaulting to True.
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        # If available, sets is_available to False and returns "Successful checkout".
        # If not, returns "Already out".
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        else:
            return "Already out"

    def return_item(self):
        # Sets is_available to True[cite: 1].
        self.is_available = True

    def __str__(self):
        # Overrides string representation to the required format[cite: 1].
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"


    # Part 3 Additions below:

class Book(MediaItem):
    def __init__(self, title, author, page_count, is_available=True):
        super().__init__(title, author, is_available)
        self.page_count = page_count # Adds an attribute of page_count

    def __str__(self):
        # Overrides __str__ to include the page count
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} ({self.page_count} pages) [{status}]"

class DVD(MediaItem):
    def __init__(self, title, author, duration, is_available=True):
        super().__init__(title, author, is_available)
        self.duration = duration # Adds an attribute of duration[cite: 2]

    def checkout(self):
        # Uses super().checkout() to maintain original logic and preserve the return value[cite: 2]
        result = super().checkout()
        
        # Prints a reminder every time it is successfully checked out[cite: 2]
        if result == "Successful checkout":
            print("Handle with care: Do not scratch the disc.")
            
        return result


        #Part 4 Additions below:
# ... (keep your existing MediaItem, Book, and DVD classes above this) ...

class LibraryCollection:
    def __init__(self):
        # Initializes the container with an empty list
        self.items = []

    def add_item(self, item):
        # Adds a MediaItem (or its subclass) to the list
        self.items.append(item)

    def list_available(self):
        # Returns a list of titles that are currently available[cite: 2]
        available_titles = []
        for item in self.items:
            if item.is_available:
                available_titles.append(item.title)
        return available_titles
        
        # Note: You can also write this as a one-liner using list comprehension:
        # return [item.title for item in self.items if item.is_available]