import csv

header = ["Ime", "Prezime", "Godine"]

podaci = [
    ["Eris", "Sutkovic", 23],
    ["Petar", "Markovic", 37],
    ["Marko Petroivc", "Sutkovic", 29]
]

''' Kreiranje novog CSV fajla ako on vec ne postoji '''
with open("csvfiles/exercise.csv", "w", newline="") as csvfile:
    # Kreiranje writer objekta
    writer = csv.writer(csvfile)
    # Upisivanje headera iz niza 'header' u CSV fajl
    writer.writerow(header)
    # Upis podataka iz niza 'podaci' u CSV fajl
    writer.writerows(podaci)

''' Upis u CSV iz input-a '''

fname = input("First name: ")
lname = input("Last name: ")
age = input("Age: ")

with open("csvfiles/exercise.csv", "w", newline="") as csvf2:
    writer = csv.writer(csvf2)
    writer.writerow([fname, lname, age])

