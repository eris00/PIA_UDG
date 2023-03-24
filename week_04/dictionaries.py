''' Dictionaries '''

'''
my_dict = {'name':'eris', 'lastname':'sutkovic', 'age':22}

# Izmjena preuzetog elementa
name = my_dict['name']
upp_name = name.upper()

print(upp_name)

# Mijenjanje elementa pomocu key-a
my_dict['lastname'] = 'sutkovski'
print(my_dict['lastname'])
'''

vehicles = {
    'brand': 'Audi',
    'models': ['A3', 'A4', 'A6'],
    'year': 2008,
    'engine': '2.7 TDI',
    'horse_power': '190',
    'colors': ['black', 'white', 'blue'],
    'electric': False
}

# Printanje keyeva
# for x in vehicles:
#     print(x)

# Printanje valuea
# for x in vehicles:
#     print(vehicles[x])

#Uklanjanje elementa iz dictionaryja
# print(vehicles)
# vehicles.pop('electric')
# print(vehicles)

# print(len(vehicles))

# Dodavanje novog itema u dict
vehicles['doors']: '5'

# Dodavanje value u key
models = vehicles['models']
# print(models)
models.append('A8')

# for x in models:
#     print('Audi ' + x)

# print(vehicles.items())

# val = input('What model do you want: ')
# if val in models:
#     print('We have that model')
# else:
#     print('Sorry, we dont have ' + val + ' right now.')

# Kopiranje citavog dicta
# veh = vehicles.copy()
# print(veh)

''' Nested dictionaries '''

students = {
    's1': {
        'fname': 'Eris',
        'lname': 'Sutkovic',
        'age': 22,
        'faculty': 'FIST',
        'avg_grade': 7.5
    },
    's2': {
        'fname': 'Lazar',
        'lname': 'Radanovic',
        'age': 23,
        'faculty': 'FIST',
        'avg_grade': 8.2
    },
    's3': {
        'fname': 'Ivan',
        'lname': 'Novakovic',
        'age': 26,
        'faculty': 'FIST',
        'avg_grade': 6.3
    },
    's4': {
        'fname': 'Nikola',
        'lname': 'Popovic',
        'age': 22,
        'faculty': 'FIST',
        'avg_grade': 6.9
    },
    's5': {
        'fname': 'Seid',
        'lname': 'Husovic',
        'age': 24,
        'faculty': 'Politehnika',
        'avg_grade': 9.2
    },

}

# Uzimanje elementa nested dict-a
# print(students['s1']['fname'])

# Ispis nested dicta kroz loop
# for student in students:
#     print(students[student]['fname'])

# def print_students(stud):
#     print('Aktivni studenti: ')
#     for students in stud:
#         print(stud[students]['fname'], end=" ")
#         print(stud[students]['lname'], end=", ")
#         print(stud[students]['age'])
#
# print_students(students)

# def senior_students(students):
#     print('Studenti stariji od 25 godina: ')
#     for s in students:
#         ages = students[s]['age']
#         if ages > 25:
#             print(students[s]['fname'], end=" ")
#             print(students[s]['lname'])
#
# senior_students(students)

def avg_grade(students):
    sum_grades = 0
    num_students = len(students)

    for s in students:
        sum_grades += students[s]['avg_grade']

    sum_avg_grade = sum_grades / num_students
    rounded_avg_grade = round(sum_avg_grade, 2)

    return rounded_avg_grade

print(avg_grade(students))

