from core.baseapp import BaseApp
from view.view_book import *

class MainApp():
    def __init__(self):
        self.books = []

    def list_book(self):
        self.list_books()


if __name__ == "__main__":
    app = MainApp()
    app.run()

