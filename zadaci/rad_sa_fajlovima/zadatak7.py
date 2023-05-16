import csv

def append_to_file(list_of_products):
    header = ['naziv', 'opis', 'godina', 'kolicina', 'cijena']
    with open("csvfiles/products.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        if file.tell() == 0:  # Provera da li fajl već ima sadržaj
            writer.writeheader()  # Upisivanje zaglavlja samo ako fajl ne sadrži podatke
        for product in list_of_products:
            writer.writerow(product)

list_of_products = [
    {'naziv': 'Televizor', 'opis': 'Samsung SmartTV', 'godina': 2022, 'kolicina': 10, 'cijena': 300},
    {'naziv': 'Televizor', 'opis': 'LG SmartTV', 'godina': 2021, 'kolicina': 23, 'cijena': 290},
    {'naziv': 'Televizor', 'opis': 'Tesla', 'godina': 2019, 'kolicina': 31, 'cijena': 240},
    {'naziv': 'Televizor', 'opis': 'Samsung SmartTV', 'godina': 2023, 'kolicina': 15, 'cijena': 810}
]

# append_to_file(list_of_products)


def get_products_older_than(year):
    products = []
    with open("csvfiles/products.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            year_data = int(row[2])
            if year_data <= year:
                products.append(row)
    for x in products:
        print(x)

# get_products_older_than(2021)
def max_possible_revenue():
    ukupan_prihod = 0
    with open("csvfiles/products.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            kolicina = int(row[3])
            cijena = int(row[4])
            prihod = cijena * kolicina
            ukupan_prihod += prihod
    print(ukupan_prihod)

max_possible_revenue()