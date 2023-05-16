import csv

header = ["Ime", "Prezime", "Godine"]

podaci = [
    ["Eris", "Sutkovic", 23],
    ["Petar", "Markovic", 37],
    ["Marko", "Petroivc", 29]
]

''' Kreiranje novog CSV fajla ako on vec ne postoji '''
# with open("csvfiles/exercise.csv", "w", newline="") as csvfile:
#     # Kreiranje writer objekta
#     writer = csv.writer(csvfile)
#     # Upisivanje headera iz niza 'header' u CSV fajl
#     writer.writerow(header)
#     # Upis podataka iz niza 'podaci' u CSV fajl
#     writer.writerows(podaci)

''' Upis u CSV iz input-a  '''

# fname = input("First name: ")
# lname = input("Last name: ")
# age = input("Age: ")
# #(a-ppend mode)
# with open("csvfiles/exercise.csv", "a", newline="") as csvf2:
#     writer = csv.writer(csvf2)
#     writer.writerow([fname, lname, age])

''' Citanje CSV fajla: '''
sum_god = 0
c=0
with open("csvfiles/exercise.csv") as csvf3:
    reader = csv.reader(csvf3)
    next(reader) #Preskoci header
    for row in reader:
        godine = row[2]
        godine = int(godine)
        sum_god += godine
        c += 1

pros_god = sum_god / c
print('prosjecno godina: ', pros_god)
print('ukupne godine:', sum_god)

