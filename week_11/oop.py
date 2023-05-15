class Post:
    def __init__(self, name, description, author):
        self.__name = name
        self.__description = description
        self.__author = author

    def getName(self):
        return self.__name

    def setName(self, name):
        if name.isalpha():
            self.__name = name

post_a = Post("naziv posta", "neki opis..", "Eris")
print(post_a.getName())
print(post_a.setName("drugi naziv"))
print(post_a.getName())