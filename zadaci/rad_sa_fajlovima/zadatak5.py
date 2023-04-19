'''
Napisati program koji iz fajla (kreirajte txt fajl) izvlaci sve heksadecimalne
brojeve (pocinju sa 0x), konvertuje ih ih brojeve sa osnovom 10(int) i ako se
nakon konverzije u int zavrsavaju sa cifrom 3, dodati ih u sumu.
Pomoc: za pretvaranje heksadecimalnog broja (koji je string formata), u int,
koristiti int(heksa_broj, 16), heksa_broj je string heksadecimalnog
formata(pocinje sa 0x).
'''

# Otvaranje fajla za čitanje
with open('txtfiles/hexa.txt', 'r') as file:
    # Inicijalizacija sume
    total_sum = 0
    # Čitanje linija iz fajla
    for line in file:
        # Uklanjanje belina sa početka i kraja linije
        line = line.strip()
        # Provera da li linija počinje sa '0x' što ukazuje na heksadecimalni broj
        if line.startswith('0x'):
            try:
                # Pretvaranje heksadecimalnog broja u decimalni format
                decimal_num = int(line, 16)
                # Provera da li se decimalni broj završava cifrom 3
                if str(decimal_num)[-1] == '3':
                    # Dodavanje broja u sumu
                    total_sum += decimal_num
            except ValueError:
                # Ignorisanje linije ako heksadecimalni broj nije validan
                pass

# Ispis rezultata
print(f'Suma heksadecimalnih brojeva koji se završavaju sa cifrom 3: {total_sum}')


