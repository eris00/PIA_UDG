import csv

'''
with open('vgsales.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Preskakanje headera

    # Ukupna prodaja za svaki region
    na_sales = 0
    eu_sales = 0
    jp_sales = 0
    other_sales = 0

    for row in reader:
        na_sales += float(row[6])
        eu_sales += float(row[7])
        jp_sales += float(row[8])
        other_sales += float(row[9])

    print("NA Sales:", na_sales)
    print("EU Sales:", eu_sales)
    print("JP Sales:", jp_sales)
    print("Other Sales:", other_sales) 
'''

'''
genre_counts = {}
with open('vgsales.csv', 'r') as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        genre = row[4]
        if genre not in genre_counts:
            genre_counts[genre] = 1
        else:
            genre_counts[genre] += 1

print(genre_counts)
'''

'''
with open('vgsales.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    latest_year = 0
    earlier_year = 0

    years = []

    for row in reader:
        year = int(row[3])
        years.append(year)

    earlier_year = min(years)
    latest_year = max(years)



    print(latest_year)
    print(earlier_year)
'''

'''
# Broj objavljenih igara po platformi
with open('vgsales.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    platforms = {}
    for row in reader:
        platform = row[2]
        if platform not in platforms:
            platforms[platform] = 1
        else:
            platforms[platform] += 1

    print(platforms)
'''