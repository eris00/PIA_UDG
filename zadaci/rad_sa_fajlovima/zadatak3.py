'''
Napisati program koji za unijeti naziv države iz fajla population.txt štampa
grad sa najmanjim brojem stanovnika. Fajl u svakom redu sadrži string oblika:
Drzava,Grad,broj_stanovnika
'''

file = open('txtfiles/population.txt', 'r+')

input_drzava = input("Unesite drzavu: ")
min_populacija = float('inf')

grad_min = ""
trenutna_populacija = 0

for line in file:
    drzava, grad, populacija = line.strip().split(',')
    populacija = int(populacija)

    if input_drzava == drzava:
        trenutna_populacija = populacija
        if trenutna_populacija < min_populacija:
            min_populacija = trenutna_populacija
            grad_min = grad

print(grad_min)
