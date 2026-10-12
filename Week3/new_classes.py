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