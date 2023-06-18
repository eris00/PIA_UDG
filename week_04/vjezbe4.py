#66.Napisati program koji unijeti string s (karakteri string alfabetski karakteri, mala
#slova) enkriptuje na sledeći način: ako je karakter suglasnik pretvara ga u 0, a
#ako je karakter samoglasnik pretvara ga u 1. Npr. za s = ‘abaae’ rezultat je
#10111.
'''
str = input("Unesi string: ")
encripted_str = ""
for x in str:
    if x in "aeiou":
        encripted_str += "1"
    else:
        encripted_str += "0"
print(encripted_str)
'''

#71.Napisati program koji za unijeti parametar a, koji je string sastavljen od cifara,
#vraća srednju vrijednost.
#Input: “122136” Output: 2.5
''' 
str = "122136"
strlen = len(str)
sum = 0
for x in str:
    sum += int(x)

mean = sum/strlen
print(mean)
'''

#1. Napisati funkciju absolute_of_even_sum koja ima jedan parametar, niz
#cijelih brojeva, a koja računa apsolutnu sumu svih negativnih parnih
#elemenata za unijeti niz. Štampati sumu.
#Input: [-2, 7, -5, 3, 1, -4] Output: 6 (|-2| + |-4|)
''' 
def absolute_of_even_sum(list):
    sum = 0
    for x in list:
        if x<0 and x%2 == 0:
            sum += x
    return sum

print(absolute_of_even_sum([-2, 7, -5, 3, 1, -4]))
'''

#2. Dječakov put od škole do kuće je dug. Da bi mu bilo interesantnije, odlučio je
#da sabira sve brojeve kuća (na svakoj kući piše adresa, tj. broj) pored kojih
#prođe dok ide do kuće. Nažalost, nemaju sve kuće brojeve na njima, a osim
#toga dječak redovno mijenja ulice, tako da se brojevi ne pojavljuju u nekom
#definisanom redosledu. U jednom momentu tokom šetnje, dječak naiđe na
#kuću na kojoj piše 0, što ga je iznenadilo toliko da je zaboravio (prestao) da
#sabira brojeve nakon što je naišao na ovu kuću. Za zadati niz kuća (svaka
#identifikovana sa brojem) odrediti zbir koji je dječak dobio. Primjer:
#Za input = [5, 1, 2, 3, 0, 1, 5, 0, 2], output treba da bude 11 (5+1+2+3 = 11)
'''
def home_way(arr):
    sum = 0
    for x in arr:
        if x == 0:
            break
        sum += x
    return sum

print(home_way([5, 1, 2, 3, 0, 1, 5, 0, 2]))
'''

#3. Napisati funkciju presjek (a, b) koja za unijete liste a i b vraća listu zajedničkih
#elementa liste a i liste b. Elementi liste a i liste b su brojevi ili stringovi.
#Input 1: a = [1,2, ’a’], b = [‘a’, 2] Output 1: [2, ‘a’]
#Input 2: a = [2, 3, 4], b = [1, 1, 7] Output 2: []
'''
def intersection(a, b):
    list = []
    for x in a:
        for y in b:
            if y == x:
                list.append(y)
    return list

print(intersection([1,2, 'a',99], [7,'a', 2,4,99]))
'''

#6. Napisati funkciju: update_list(a, x) koja za unijetu listu elemenata (cijeli
#brojevi) a uvećava svaki parni element za vrijednost x. Parametar x je
#prirodan broj.
#Input 1: [1, 2, -1, 3, -4], 3 Output: [1, 5, -1, 3, -1]
#Input 2: [21, 10, -10, 100], 5 Output: [21, 15, -5, 105]
'''
def update_list(a, x):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] += x
    return a

print(update_list([1, 2, -1, 3, -4], 3))
'''














