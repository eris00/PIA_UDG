'''
# 1 - 77

broj = input("Unesite broj:")

if broj[0:2] == "0b":
    print("Binarni broj.")
elif broj[0:2] == "0x":
    print("Heksadecimalni broj.")
elif broj[0:2] == "0o":
    print("Oktalni broj.")
else:
    print("Dekadni broj.")

# 1 - 82

number = input("Unesite broj:")
is_binary = False
for i in number:
    if i == '0' or i == '1':
        is_binary = True
    else:
        is_binary = False
        break
if is_binary:
    print("Broj je binarni")
else:
    print("Broj nije binarni")

# 2 - 7

lista = [10, 10, 5, 7]
lista = list(set(lista))
lista.sort()
print(f"Drugi najveci element je {lista[-2]}")

# Ucitavanje sadrzaja iz fajla
f = open("/home/stevan/Desktop/Programiranje 1/fajl.txt")
print(f.read())
f.seek(0)
print(f.read())

# 1 - 88
def points(string):
    points = 0
    for letter in string:
        if letter == "1":
            points += 1
        if letter == "*":
            points -= 1
    print(points)
print("*****************")
points("1100**")

# 1 - 90

string = '12345'
string2 = ''
for char in string:
    if int(char)%2==0:
        string2=string2+'0'
    else:
        string2=string2+'1'
print(string2)

# 2 - 8
def dodaj_proizvode(n):
    lista_proizvoda = []
    for i in range(n):
        naziv = input("Unesite naziv proizvoda:")
        opis = input("Unesite opis proizvoda:")
        cijena = float(input("Unesite cijenu proizvoda:"))
        br_artikala = int(input("Unesite broj artikala:"))
        lista_proizvoda.append({'naziv':naziv,'opis':opis,'cijena':cijena, 'br_artikala':br_artikala})
    return lista_proizvoda

# proizvodi = dodaj_proizvode(3)
proizvodi = [{'naziv': 'tv', 'opis': 'lg', 'cijena': 350.0, 'br_artikala': 3}, 
{'naziv': 'pc', 'opis': 'dell', 'cijena': 600.0, 'br_artikala': 5}, 
{'naziv': 'jabuka', 'opis': 'crvena', 'cijena': 0.1, 'br_artikala': 100}]
for proizvod in proizvodi:
    print(proizvod)

def pretraga_proizvoda(proizvodi, searh_term):
    nadjeni_proizvodi = []
    for proizvod in proizvodi:
        if proizvod['naziv'].startswith(searh_term):
            nadjeni_proizvodi.append(proizvod)
    return nadjeni_proizvodi

print(pretraga_proizvoda(proizvodi, "j"))

#2 - 9

def filter(igrice):
    filtriraneigrice = []
    x=float(input("Unesite zeljenu ocjenu"))
    y=input("Unesite zeljenog izdavaca")
    for igrica in igrice:
        ime, izdavac, godina, ocjena = igrica
        if izdavac == y  and ocjena > x:
            filtriraneigrice.append(igrica)
    return filtriraneigrice

igrice = [("Igra 1", "Izdavac 1", 2010, 4.5),
         ("Igra 2", "Izdavac 2", 2015, 3.9),
         ("Igra 3", "Izdavac 1", 2018, 4.8),
         ("Igra 4", "Izdavac 3", 2019, 4.2),
         ("Igra 5", "Izdavac 2", 2012, 4.1)]

print(filter(igrice))

#2 - 9 - list comperhension
def izdvoj_igricu2(lista):
    x = float(input("Unesite ocjenu: "))
    y = input("Unesite izdavaca: ")
    new_list = [igrica for igrica in lista if igrica[1] == y and igrica[3] > x]
    print(new_list)

izdvoj_igricu2(igrice)

#2 - 10
def words_with_even_len(string, letter):
    array = []
    words = string.split()
    for word in words:
        if len(word) % 2 == 0 and letter not in word:
            array.append(word)
    return array

print(words_with_even_len("words with even number of character d", "d"))

# 2 - 13
def olaksaj_brokeru(zahtjev):
    zahtjevi = zahtjev.split(",")
    b = 0
    s = 0
    for x in zahtjevi:
        elements = x.split()
        if elements[3] == "B":
            b += int(elements[1]) * float(elements[2])
        else:
            s += int(elements[1]) * float(elements[2])
    return f"Buy: {b}, Sell: {s}"

print(olaksaj_brokeru("GOOG 300 542.0 B"))

# 3 - 1

f = open('C:/Users/PC/Desktop/Vjezbe17032023/fajl1.txt')
max = 0
for element in f:
    a, b = element.strip().split(',')
    a = int(a)
    b = int(b)
    if a == b:
        povrsina = a*b
        if povrsina>max:
            max = povrsina
f.close()
print(max)
'''
