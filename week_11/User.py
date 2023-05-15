class User:
    def __init__(self, name):
        self.__name = name

    def who_am_i(self):
        print("I am user")

    def login(self):
        print("User login")


class Admin(User):
    def __init__(self, name, super_admin):
        User.__init__(self, name)
        self.__super_admin = super_admin

    def who_am_i(self):
        print("Im admin")

    def delete_user(self):
        print("User deleted")


