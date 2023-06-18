#9. Dobili ste zadatak da pomognete profesoru Milošu. Trebate da napišete
#program koji za 5 unešenih ocjena u sistem računa i štampa srednju
#vrijednost.
'''
o1 = 4
o2 = 5
o3 = 2
o4 = 3
o5 = 4

sum = o1+o2+o3+o4+o5
print(sum / 5)
'''

#26.Provjeriti da li je broj paran i stampati odgovarajucu poruku.
'''
num = 4

if num%2 == 0:
    print("Paran")
else:
    print("Nije")
'''

#50.Ako tekst ima više od 30 karaktera skratiti ga tako da ostane tačno 30
#karaktera, a na kraj skraćenog teksta dodati …
'''
text = "50.Ako tekst ima više od 30 karaktera skratiti ga tako da ostane tačno 30 karaktera, a na kraj skraćenog teksta dodati"
end="..."
short_text = ""
if len(text) > 30:
    short_text = text[:30] + end

print(short_text)
'''

#6.Napisati program koji iz zadatog stringa izdvaja samo samoglasnike i štampa ih na izlazu.
#Input: “String koji sadrzi samoglasnike”
#Output: “ioiaiaoaie”
'''
string = "String koji sadrzi samoglasnike"
samoglasnici=""
for x in string:
    if x.lower() in "aeiou":
        samoglasnici += x

print(samoglasnici)
'''

#11. Poznata su tri trocifrena broja x, y i z. Provjeriti da li je zbir cifara sa prve
#pozicije (stotine) veći od proizvoda cifara sa poslednje pozicije (jedinice).
'''
br1 = 675
br2 = 673
br3 = 362

prve_cif = br1//100 + br2//100 + br3//100
zadnje_cif = br1 % 10 * br2 % 10 * br3 % 10

if prve_cif > zadnje_cif:
    print("Jeste")
else:
    print("Nije")
'''

#34.Iz zadatog teksta izdvojiti i na izlazu štampati sva velika slova iz tog teksta.
'''
txt = "Neki tekst sa Velikim SloviMa."
for x in txt:
    if x.isupper():
        print(x)
'''

#57.Napisati program koji računa i štampa zbir parnih i proizvod neparnih brojeva
#od 1 do n. Broj n unosi korisnik
'''
n=15
parni = 0
neparni = 1
for i in range(1,n+1):
    if i % 2 == 0:
        parni+=i
    else:
        neparni*=i

print(parni)
print(neparni)
'''