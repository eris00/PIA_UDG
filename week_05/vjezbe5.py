#77.Napisati program koji provjerava da li je korsnik unio binarni, oktalni, dekadni
#ili heksadecimalni broj. Binarni broj ima prefiks 0b, oktalni 0o, heksadecimalni
#0x, a dekadni nema prefiks.
'''
number = input("Unesi broj: ")

if number.startswith("0b"):
    print("Binarni broj")
elif number.startswith("0o"):
    print("Oktalni broj")
elif number.startswith("0x"):
    print("heksadecimalni broj")
else:
    print("dekadni broj")
'''

#82.Napisati program koji provjerava da li je uneseni string binarni broj (ima samo 0 ili 1).
'''
str = "0100101c"
for x in str:
    if x != "0" and x != "1":
        print("Broj nije binarni")
        break
else:
    print("Binarni broj")
'''

#7. Napisati funkciju second_max(a) koja nalazi drugi najveći element liste a. Npr.
#ako je a = [1, 22, 33] rezultat je 22. Napomena: lista ima bar 2 elementa.
'''
def second_max(a):
    a.sort()
    return a[-2]
print(second_max([1, 22, 33, 12]))
'''

#90.Napisati program encrypt_string(s) koji za unijeti string s (karakteri stringa
#cifre od 0 do 9) enkriptuje na sledeći način: ako je karakter paran broj pretvara
#se u 0, a ako je karakter neparan broj pretvara se u 1. Npr. za s = ‘15023’
#rezultat je 11001.
'''
s = "15023"
new_s = ""
for x in s:
    if int(x) % 2 == 0:
        new_s += '0'
    else:
        new_s += '1'
print(new_s)
'''

#8. Napisati funkciju koja omogućava korisniku da unese n proizvoda (n
#parametar funkcije). Svaki proizvod se predstavlja sa kao dictionary oblika:
#{naziv, opis, cijena, broj_artikala}. Funkcija treba da vrati listu proizvoda.
#Nakon toga, napisati funkciju koja ima dva parametra i to proizvodi,
#search_term, a koja vraća sve proizvode čiji naziv počinje sa vrijednošću
#parametra search_term.
''' 
def add_products(n):
    product_list = []
    for i in range(n):
        naziv = input("Unesi naziv: ")
        opis = input("Unesi opis: ")
        cijena = float(input("Unesi cijenu: "))
        br_artikala = int(input("Unesi broj artikala: "))
        product_list.append({'naziv':naziv, 'opis':opis, 'cijena':cijena, 'br_artikala':br_artikala,})
    return product_list

products = add_products(3)

for x in products:
    print(x)

def search_products(products, search_term):
    prod_list = []
    for x in products:
        if x['naziv'].startswith(search_term):
            prod_list.append(x)
    return prod_list

print("trayebu proizvodi; ", search_products(products, "laptop"))
'''

#Napisati funkciju koja kao parametar prima listu igrica oblika (ime:String,
#izdavac:String, godina_izlaska:Integer, ocjena:Float), a vraća igrice čija je
#ocjena veca od ocjene x (unosi korisnik sa input), a cije je izdavac y (unosi
#korisnik sa input). Koristiti list comprehension pristup.
'''
def games_filter(game_list):

    filtered_games = []

    x = float(input("Unesite ocjenu: "))
    y = input("Unesite izdavača: ")

    for game in game_list:
        ime, izdavac, godina_izlaska, ocjena = game
        if ocjena > x and izdavac == y:
            filtered_games.append(game)
    return filtered_games

game_list = [("Igra 1", "Izdavac 1", 2010, 4.5),
         ("Igra 2", "Izdavac 2", 2015, 3.9),
         ("Igra 3", "Izdavac 1", 2018, 4.8),
         ("Igra 4", "Izdavac 3", 2019, 4.2),
         ("Igra 5", "Izdavac 2", 2012, 4.1)]

print(games_filter(game_list))
'''

#10.Napisati funkciju koja za unijeti string i slovo vraća sve riječi čija je dužina
#paran broj, a ne sadrže zadato slovo (koje korisnik unosi). Primjer:
#get_ewfbyr(“words with even number of letters without character d”, “d”)
#Output: [“with”, “even”, “number”, “of”]
'''
str = "Ovdje su neke riječi i njihove dužine"

letter = "e"
selected_words = []
words = str.split(" ")

for x in words:
    duzina = len(x)
    if duzina % 2 == 0 and letter not in x:
        selected_words.append(x)

print(selected_words)
'''



























