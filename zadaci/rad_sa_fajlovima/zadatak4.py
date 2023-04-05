'''
Napisati program koji za unijeti naziv države i zadati fajl population.txt štampa
ukupan broj stanovnika za zadatu državu. Fajl u svakom redu sadrži string
oblika: Drzava,Grad,broj_stanovnika
'''

file = open('txtfiles/population.txt')

# print(file.read())

input_drzava = input("Unesite drzavu: ")
ukupna_populacija = 0

for line in file:
    drzava, grad, populacija = line.strip().split(',')
    populacija = int(populacija)

    if input_drzava == drzava:
        ukupna_populacija += populacija

print(ukupna_populacija)

