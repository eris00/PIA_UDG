'''
# Zadatak 3 - 4
drzava = 'Poljska'
suma = 0
with open('population.txt') as f:
    line = f.read().split('\n')
    for i in line:
        element=i.split(',')
        if element[0]==drzava:
            suma = suma + int(element[2])
print(suma)

# Zadatak 3- 7
import csv

def append_to_file(list_of_products):
    with open("products.csv", "a", newline="") as file:
        reader = csv.DictWriter(file, fieldnames=list_of_products[0].keys())
        reader.writeheader()
        for product in list_of_products:
            reader.writerow(product)

lista=[{"naziv": "Televizor", "opis": "LG televizor 43inc", "godina": 2019, "kolicina": 10, "cijena": 300}, {"naziv": "Televizor", "opis":"Samsung televizor 39inc", "godina": 2017, "kolicina": 5, "cijena": 250}]
# append_to_file(lista)

def products_older_than(year):
    products = []
    with open("products.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["godina"]) >= year:
                products.append(row)
    return products

print(products_older_than(2018))

def max_possible_revenue():
    suma = 0
    with open("products.csv") as file:
        reader = csv.DictReader(file)
        for product in reader:
            suma += int(product["cijena"]) * int(product["kolicina"])

    return suma

print(max_possible_revenue())
"""
# Zadatak 3 - 8

def append_to_file(lista):
    with open('students.txt','w') as f:
        for element in lista:
            f.writelines(element['ime']+","+element['prezime']+","+str(element['godina'])+","+str(element['prosjek'])+"\n")

list_students = [{"ime":"Marko","prezime":"Markovic","godina":2,"prosjek":8.6},{"ime":"Boris","prezime":"Boricic","godina":3,"prosjek":7.9},{"ime":"Novak","prezime":"Novovic","godina":3,"prosjek":6.9}]

append_to_file(list_students)

def get_students_with_grater_grade(year,grade):
    with open('students.txt') as f:
        result = []
        for row in f:
            ime,prezime,godina,prosjek = row.strip().split(',')
            godina = int(godina)
            prosjek = float(prosjek)
            if godina == year:
                if grade =='A':
                    if 9.5<=prosjek<=10:
                        result.append({"ime":ime,"prezime":prezime,"godina":godina,"prosjek":prosjek})
                elif grade =='B':
                    if 8.5<=prosjek<=9.5:
                        result.append({"ime":ime,"prezime":prezime,"godina":godina,"prosjek":prosjek})
                elif grade =='C':
                    if 7.5<=prosjek<=8.5:
                        result.append({"ime":ime,"prezime":prezime,"godina":godina,"prosjek":prosjek})
                elif grade == 'D':
                    if 6.5<=prosjek<=7.5:
                        result.append({"ime":ime,"prezime":prezime,"godina":godina,"prosjek":prosjek})
                elif grade == 'E':
                    if 6<=prosjek<=6.5:
                        result.append({"ime":ime,"prezime":prezime,"godina":godina,"prosjek":prosjek})
        return result

print(get_students_with_grater_grade(3,'C'))
'''