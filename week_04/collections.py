
''' Liste '''

list = [1,33,5,-16,2,10,5,1]

# print(len(list))

# print(list[2])

#Ispis liste kroz petlju
# for x in list:
#     print(x)

#Izmjena nad elementima niza
# i = 0
# while i < len(list):
#     list[i] = list[i]*2
#     print(list[i])
#     i += 1

#Dodavanje elementa na kraj liste
# list.append(70)
# print(list)

#Vraca zadnji element niza i brise ga iz niza
# print(list.pop())
# print(list)

#Okrece elemente liste u suprotnom poretku
# list.reverse()
# print(list)

#Sortira elemente liste
# list.sort()
# print(list)

#Koliko se puta pojavljuje proslijedjeni element u listi
# print(list.count(1))

#Dodavanje druge liste na prvu
# l2 = [1,2,3,4]
# list.extend(l2)
# print(list)

#Vraca index proslijedjenog elementa
# print(list.index(33))

#Ubacivanje elementa u nizu po indexu
# list.insert(2, 81)
# print(list)

# list.remove(33)
# print(list)

# list.clear()
# print(list)

''' 
    Izdvoji podniz istih brojeva ciji je zbir najveci od svih drugih podnizova
    Pr: input: [1,2,2,2,4,4] output: [4,4] i zbir 8
'''

def izdvoji_podniz(niz):
    najveci_zbir = 0
    najveci_podniz = []

    for i in range(len(niz)):
        zbir = niz[i]
        podniz = [niz[i]]

        for j in range(i + 1, len(niz)):
            if niz[j] == niz[i]:
                zbir += niz[j]
                podniz.append(niz[j])

        if zbir > najveci_zbir:
            najveci_zbir = zbir
            najveci_podniz = podniz

    print(najveci_podniz)
    print(najveci_zbir)

izdvoji_podniz([1,2,2,2,4,4])










