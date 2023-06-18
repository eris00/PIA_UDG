class Company:
    def __init__(self, name, area, balance, employees, max_num_of_employees):
        self.__name = name
        self.__area = area
        self.__employees = []
        self.__balance = max(0, balance)
        self.__max_num_of_employees = max(0, max_num_of_employees)

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_area(self):
        return self.__area
    def set_area(self, area):
        self.__area = area
    
    def get_employees(self):
        return self.__employees
    
    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        if balance>0:
            self.__balance = balance
 
    def get_max_num_of_employees(self):
        return self.__max_num_of_employees
    def set_max_num_of_employees(self, max_num_of_employees):
        if max_num_of_employees>0:
            self.__max_num_of_employees = max_num_of_employees

    def add_employee(self, employee):
        if self.get_max_num_of_employees() <= len(self.__employees) + 1:
            self.__employees.append(employee)
        else:
            print("Kompanija je dostigla maksimalni kapacitet zaposlenih")
    
    def remove_employee(self, name, surname):
        for employee in self.__employees:
            if employee['name'] == name and employee['surname'] == surname:
                self.__employees.remove(employee)

    def __str__(self):
        return (f"name {self.get_name()}, area: {self.get_area()}, balance: {self.get_balance()}")
    
    def can_pay_employees(self):
        total = 0
        for row in self.get_employees():
            total += row["salary"]
        if self.get_balance > total:
            return True
        else:
            return False
        
    def __gt__(self, other):
        return len(self.__employees) > len(other.__employees)
