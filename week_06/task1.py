# Rad sa fajlovima - 2. zadatak
current_max = 0
city_area = ""

city = input("Unesite grad: ")

with open('cities.txt') as f:
    line = f.read().split("\n")
    #print(line)
    for row in line:
        #print(row)
        splitted = row.split(',')
        #print(splitted)
        if splitted[0] == city:
            if current_max < int(splitted[2]):
                current_max = int(splitted[2])
                city_area = splitted[1]

print("Naselje sa najvecim brojem stanovnika za unijeti grad je: ", city_area)




