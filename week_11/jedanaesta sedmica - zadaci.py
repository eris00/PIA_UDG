'''
class Post:
    def __init__(self, name, description, author):
        self.__name = name
        self.__description = description
        self.__author = author
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name


post_a = Post("Vremenska prognoza", "Danas ce biti oblacan dan, do 20 stepeni", "Branko Micev")
print(post_a.get_name())
post_a.set_name("novo ime")
print(post_a.get_name())
import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius

    def obim_kruga(self):
        return 2 * self.get_radius() * math.pi

    def povrsina_kruga(self):
        return self.get_radius()**2 * math.pi

krug = Circle(3)
print(f"Obim: {krug.obim_kruga()}")
print(f"Povrsina: {krug.povrsina_kruga()}")'''

'''
class User:
    def __init__(self, name):
        self.__name = name
    
    def who_am_i(self):
        print("I'm user!")
    
    def login(self):
        print("User login!")

class Admin(User):
    def __init__(self, name, super_admin=False):
        super().__init__(name)
        self.__super_admin = super_admin
    
    def who_am_i(self):
        super().who_am_i()
        print("I'm admin!")
    
    def delete_user(self):
        print("Delete user!")

user1 = User("User 1")
admin1 = Admin("Admin 1")

user1.who_am_i()
admin1.who_am_i()

admin1.login()
admin1.delete_user()
'''

class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
    
    def __str__(self):
        return f"Naslov - {self.__title}, Autor - {self.__author}, Broj stranica - {self.__pages}"

    def __eq__(self, other):
        return self.__title == other.__title
    
    def __gt__(self, other):
        return self.__pages > other.__pages
    
    def __lt__(self, other):
        return self.__pages < other.__pages

book1 = Book("Davincijev Kod", "Autor", 200)
print(book1)
book2 = Book("Davincijev Kod", "Autor", 200)
book3 = Book("Zlocin i kazna", "Dostojevski", 800)
print(book1 == book2)
print(book1 == book3)
print(book1 > book3)
print(book1 < book3)