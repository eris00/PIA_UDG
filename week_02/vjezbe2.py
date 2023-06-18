# Sabrati prvu i posljednju cifru zadatog trocifrenog broja
'''
br = 476
prva = br//100
posljednja = br%10
print(prva + posljednja)
'''
# Napisati program koji na osnovu zadate širine i visine lista papira
# (pravougaonog oblika) u milimetrima određuje njegovu površinu u
# kvadratnim centimetrima.
'''
sirina = int(input("Unesi sirinu: "))
visina = int(input("Unesi visinu: "))

povrsina_cm2 = (sirina*visina) / 100
print(povrsina_cm2)
'''

# Napisati program koji za unijete vrijednosti varijabli a, pre,
# suf i num dodaje prefiks pre i sufiks suf stringu a num puta
# i stampa prosireni string.
'''
a = input("Unesi a: ")
pre = input("Unesi pre: ")
suf = input("Unesi suf: ")
num = int(input("Unesi num: "))

print(num*pre + a + num*suf)
'''

# 14.Ako je cijena taksija za jedan kilometar 0.5e, a početna cijena je 1e,
# napisati kod koji za unijeti broj pređenih kilometara računa cijenu
# vožnje.
'''
pocetna_cijena = 1.0
km_cijena = 0.5

kilometri = int(input("Unesite broj pređenih km: "))

cijena_voznje = pocetna_cijena + (km_cijena * kilometri)
print(cijena_voznje)
'''

#23.Radno vrijeme jedne organizacije je između 9 i 17 časova. Odrediti da li je
#poslati mejl stigao u toku radnog vremena.
'''
start = 9.00
end = 17.00
mail_time = 17.27
if mail_time >= start and mail_time <= end:
    print("Mejl je stigao na vrijeme")
else:
    print("Mejl nije stigao na vrijeme")
'''

#Hleb je prvo poskupio 10%, pa je zatim pojeftinio 10%. Ako je poznata
#početna cijena hleba, napisati program koji određuje cijenu nakon tih
#promjena.
'''
pocetna_cijena = 1.10

cijena1 = pocetna_cijena + (pocetna_cijena*0.10) #10% skuplja
cijena2 = cijena1 - (cijena1*0.10) #10% jeftinija

print("Cijena nakon promjena: ", round(cijena2,2))
'''

#25.Napisati program kojim se proverava da li se može napraviti bašta u obliku
#trougla sa datim dužinama stranica.
'''
a=5
b=3
c=4

if a+b > c and a+c > b and c+b > a:
    print("Moze")
else:
    print("Ne moze")
'''



