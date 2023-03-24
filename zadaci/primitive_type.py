
''' 1. Napisati program koji računa zbir prve i poslednje cifre trocifrenog broja. '''
num = 236

prva_cif = num // 100
druga_cif = num % 10

suma = prva_cif + druga_cif

# print(suma)


''' 2. Napisati program koji računa površinu i obim pravougaonika. '''
duzina = 6
sirina = 3

Povrsina = duzina * sirina
# print(Povrsina)

Obim = 2 * (duzina * sirina)
# print(Obim)

''' 3. Napisati program koji računa razliku kvadrata '''
broj1 = 5
broj2 = 9
razlika_kvadrata = broj1**2 - broj2**2
# print(razlika_kvadrata)




''' 6. Napisati program koji na osnovu zadate širine i visine lista papira
(pravougaonog oblika) u milimetrima, određuje njegovu površinu u kvadratnim
centimetrima.
 '''
visina_mm = 700
sirina_mm = 400

povrsina_mm = sirina_mm * visina_mm

povrsina_cm = povrsina_mm * 10000

# print(povrsina_cm)


''' Sportista se na početku treninga zagrijeva tako što trči po ivicama
pravougaonog terena dužine d i širine s. Napisati program kojim se određuje
koliko metara pretrči sportista dok obiđe teren 4 puta. '''
d = 100
s = 40

#ukupna duzina terena
L = 2*d + 2*s

res = 4 * L
# print(res)

''' 10.Za tri placa pravouganog oblika poznate su dimenzije (dužina i širina).
Štampati dimenzije placa koji ima najveću površinu.
 '''

d1 = 6
s1 = 4

d2 = 7
s2 = 3

d3 = 12
s3 = 5

p1 = d1 * s1
p2 = d2 * s2
p3 = d3 * s3

# if p1 > p2 and p1 > p3:
#     print(p1)
# elif p2 > p1 and p2 > p3:
#     print(p2)
# else:
#     print(p3)


''' 11. Poznata su tri trocifrena broja x, y i z. Provjeriti da li je zbir cifara sa prve
pozicije (stotine) veći od proizvoda cifara sa poslednje pozicije (jedinice).
'''

x = 321
y = 572
z = 425

x_stotina = x // 100
y_stotina = y // 100
z_stotina = z // 100
stotina_sum = x_stotina + y_stotina + z_stotina

x_pos = x % 10
y_pos = y % 10
z_pos = z % 10
pos_pro = x_pos * y_pos * z_pos

# if stotina_sum > pos_pro:
#     print('veci je')
# else:
#     print('nije')

''' 14.Ako je cijena taksija za jedan kilometar 0.5e, a početna cijena je 1e,
napisati kod koji za unijeti broj pređenih kilometara računa cijenu
vožnje '''

# pocetna_cijena = 1
# cijena = 0.5
# predjeni_km = int(input('Predjeni KM: '))
#
# cijena_voznje = pocetna_cijena + (predjeni_km * cijena)
# print(cijena_voznje)


''' Provjeriti da li je broj paran i stampati odgovarajucu poruku. '''

# num = 4
# if num % 2 == 0:
#     print('paran')
# else:
#     print('nije')

''' 90.Napisati program encrypt_string(s) koji za unijeti string s (karakteri stringa
cifre od 0 do 9) enkriptuje na sledeći način: ako je karakter paran broj pretvara
se u 0, a ako je karakter neparan broj pretvara se u 1. Npr. za s = ‘15023’
rezultat je 11001.
 '''
res = ""
str = '15023'

for x in str:
    if int(x) % 2 == 0:
        res += '0'
    else:
        res += '1'

# print(res)

''' Napisati program koji iz teksta izvlači cifre i računa njihov proizvod. '''

# res = []
# text = 'Danas1 je dobar dan. Datum 24.3.2023.godine.'
# for x in text:
#     if x.isnumeric():
#         res.append(x)
#
# lista_int = []
# for x in res:
#     x_num = int(x)
#     lista_int.append(x_num)
#
# print(lista_int)
#
# sum = 0
# for x in lista_int:
#     sum += x
#
# print(sum)






