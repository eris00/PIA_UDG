from datetime import datetime

#Uzimanje trenutne godine
trenutni_datum = datetime.now()
trenutna_godina = trenutni_datum.year

igrice = []

while True:

    naziv = input("Unesite naziv igrice: ")
    if len(naziv) < 2 or len(naziv) > 50:
        print("Mora sadrzati min 2 i max 50 karaktera")
        continue

    ocjena = input("Unesite ocjenu: ")
    ocjena = float(ocjena)
    if ocjena < 1 or ocjena > 10:
        print("Ocjena mora biti od 1 do 10")
        continue

    godina = input("Unesite godinu: ")
    godina = int(godina)
    if godina < 1950 or godina > trenutna_godina:
        print("Godina mora biti izmedju '950 i trenutne godine")
        continue

    izdavac = input("Izdavac")
    if len(izdavac) < 2 or len(izdavac) > 50:
        print("Izdavac mora sadrzati min 2 i max 50 karaktera")
        continue

    zanrovi = input("zanrovi igre")
    niz_zanrova = zanrovi.split()
    if len(niz_zanrova) > 3:
        print("Ne mozete unijeti vise od 3 zanra!")
        continue

    igrice.append(naziv)
    igrice.append(ocjena)
    igrice.append(godina)
    igrice.append(izdavac)
    igrice.append(zanrovi)

    break

with open("txtfiles/igrice.txt", "w") as file:
    file.writelines('\n'.join(igrice))



