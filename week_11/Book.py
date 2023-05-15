class Book:
    def __init__(self, title, author, num_page):
        self.__title = title
        self.__author = author
        self.__num_page = num_page

    def __str__(self):
        return "Naslov: ", self.__title, "Autor: ", self.__author, "Broj stranica: ", self.__num_page

    def __eq__(self, other):
        if self.__title == other.__title

book1 = Book("Davincijev Kod", "Autor", 200)
book2 = Book("Davincijev KOd", "Autor", 200)
book3 = Book("Zlocin i kazna", "Autor", 800)

print(book1 == book3)
