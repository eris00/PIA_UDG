class Company:
    def __init__(self, name, area, employees, balance, max_num_of_employees):
        self.__name = name
        self.__area == area
        self.__employees == employees
        self.__balance == balance
        self.__max_num_of_employees == max_num_of_employees

    def get_name(self):
        return self.__name

    def set_name(self, val):
        self.__name = val

    def get_area(self):
        return self.__area

    def set_area(self, val):
        self.__area = val

    def get_employees(self):
        return self.__area

    def set_employees(self, val):
        self.__employees = val

    def get_balance(self):
        return self.__balance

    def set_balance(self, val):
        self.__balance = val

    def get_max_num_of_employees(self):
        return self.__max_num_of_employees

    def set__max_num_of_employees(self, val):
        self.__max_num_of_employees = val

    def add_employee(self, new_employee):
        if self.get_max_num_of_employees() <= len(self.get_employees() + 1):
            self.__employees.append(new_employee)
        else:
            print("Nije moguce izvesti operaciju")

    def remove_employee(self, name, surname):
        for employee in self.__employees:
            if employee["name"] == name and employee["surname"] == surname:
                self.__employees.remove(employee)

    def __str__(self):
        return f'Name: {self.get_name()}, Area: {self.get_area()}, employees: {self.get_employees()}, balance: {self.get_balance()}'

    def can_pay_employees(self):

