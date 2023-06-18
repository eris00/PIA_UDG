
'''
# 1 - 30
broj = int(input("Unesite trocifreni broj: "))
prva_cifra = broj//100
druga_cifra = (broj%100)//10
treca_cifra = broj%10

if druga_cifra>(prva_cifra+treca_cifra):
    print("Druga cifra je veca od zbira prve i trece cifre ")
else:
    print("Nije veca ")

#1 - 68
n = 5
stepen = 3
rezultat = 1
for i in range(stepen):
    rezultat = rezultat * n
print(rezultat)

# 1-73
def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(isprime(5))
print(isprime(8))

a = 1
b = 10
brojac = 0
for i in range(a,b+1):
    if isprime(i):
        brojac = brojac + 1
print(brojac)



# 2 - 12 


def split_string(string, broj):
    brojac=0
    rijec= ""
    lista_rijeci= []
    for karakter in string:
        if brojac< broj:
            rijec= rijec+ karakter
            brojac= brojac+1
        else:
            lista_rijeci.append(rijec)
            rijec=karakter # for petlja ce preci na sledeci karakter i uci u else, taj karakter se mora sacuvati !
            brojac=1 # posto smo sacuvali vec jedan karakter u riject, onda brojac stavljamo da krece od 1, a ne od 0 !
    if rijec != "":
        rijec = rijec + (broj - len(rijec)) * "*"
        lista_rijeci.append(rijec) 
    return lista_rijeci

print(split_string('abcdefg',3))

        
'''

