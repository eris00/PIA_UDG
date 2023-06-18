'''
#2 - 9
def validate_card(card):
    if len(card) != 16 or card.isnumeric() == False:
        return False
    card = card[::-1]
    digits = list(card)
    for i in range(len(digits)):
        if (i + 1) % 2 == 0:
            temp = str(int(digits[i]) * 2)
            if len(temp) == 2:
                temp = int(temp[0]) + int(temp[1])
            digits[i] = str(temp)
    suma = 0
    for digit in digits:
        suma += int(digit)
    if suma % 10 == 0:
        return True
    else:
        return False
    
with open("kartice.txt") as file:
    kartice = file.read().split("\n")

with open("validirane_kartice.txt", "w") as file:
    for kartica in kartice:
        if validate_card(kartica):
            file.write(kartica + ", Valid\n")
        else:
            file.write(kartica + ", Invalid\n")

#CSV zadatak , fajl CSVzadatak.pdf

import csv

def ucitaj_podatke(csv_fajl):
    with open(csv_fajl, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
    return rows

def filter_year(rows, min_year):
    return [row for row in rows if int(row['year']) > min_year]

def prosjecna_cijena_po_marki(rows):
    car_brands = {}
    for row in rows:
        brand = row['brand']
        price = float(row['price'])
        if brand not in car_brands:
            car_brands[brand] = {'sum': price, 'count': 1}
        else:
            car_brands[brand]['sum'] += price
            car_brands[brand]['count'] += 1

    avg_prices = {}
    for brand, data in car_brands.items():
        avg_prices[brand] = data['sum'] / data['count']
    return avg_prices

def top5_boja(rows):
    color_count = {}
    for row in rows:
        color = row['color']
        if color not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1

    sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_colors[:5]

def sacuvaj_top5_boja(top_colors, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['color', 'count'])
        writer.writerows(top_colors)

def sortiraj_po_snazi(rows):
    return sorted(rows, key=lambda x: int(x['horsepower']), reverse=True)


rows = ucitaj_podatke('cars.csv')
min_year = int(input("Unesite minimalnu godinu proizvodnje automobila: "))
filtered_rows = filter_year(rows, min_year)
avg_prices = prosjecna_cijena_po_marki(filtered_rows)

print("\nProsječna cijena automobila po marki:")
for brand, avg_price in avg_prices.items():
    print(f"{brand}: {avg_price}")

top_colors = top5_boja(filtered_rows)
sacuvaj_top5_boja(top_colors, 'top5_colors.csv')

sorted_cars = sortiraj_po_snazi(filtered_rows)
print("\nAutomobili sortirani po snazi motora:")
for car in sorted_cars:
    print(car)

'''


