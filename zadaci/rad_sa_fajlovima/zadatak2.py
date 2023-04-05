'''
Napisati program koji za unijeti naziv grada iz fajla cities.txt štampa naziv naselja sa najvećim brojem stanovnika. Fajl u svakom redu sadrži string oblika grad, naziv_naselja, broj_stanovnika.
Input: Podgorica  Output: Zabjelo
'''

file = open('txtfiles/cities.txt', 'r+')

naselje = ""
arr = []

input_grad = input("Unesite grad: ")

max_naselje = ""
max_br_stanovnika = 0

for lines in file:
    grad, naselje, br_stanovnika = lines.strip().split(',')
    br_stanovnika = int(br_stanovnika)

    if input_grad == grad:
        if br_stanovnika > max_br_stanovnika:
            max_br_stanovnika = br_stanovnika
            max_naselje = naselje

print(max_naselje)

file.close()

