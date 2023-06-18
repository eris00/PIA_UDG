

with open("zaposleni.txt", "r+") as f:
    next(f)
    potrosnja_firme = 0
    br_zaposlenih = 0
    svi_zaposleni = []
    junior_plata = 0
    senior_plata = 0
    br_juniora = 0
    br_seniora = 0
    najmanja_plata = float('inf')
    najveca_plata = 0

    for x in f:
        ime,prezime,pozicija,plata = x.strip().split(",")
        plata = int(plata)
        br_zaposlenih += 1
        potrosnja_firme += plata
        svi_zaposleni.append(x)


        if pozicija == "Junior":
            br_juniora += 1
            junior_plata += plata

        if pozicija == "Senior":
            br_seniora += 1
            senior_plata += plata

        if plata < najmanja_plata:
            najmanja_plata = plata
        if plata > najveca_plata:
            najveca_plata = plata


# a)
for x in svi_zaposleni:
    print(x)

# b)
print("Potrosnja firme: ", potrosnja_firme)

# c)
zarade_mean = potrosnja_firme / br_zaposlenih
print("zarade svih zaposlenih: ", round(zarade_mean, 2))

# d)
junior_plata_mean = junior_plata / br_juniora
print("Prosjecna plata juniora: ", junior_plata_mean)

# e)
senior_plata_mean = senior_plata / br_seniora
print("Razlika izmedju prosjecnih plata juniora i seniora: ", junior_plata_mean - senior_plata_mean)

# d)
print("Odstupanje najmanje od prosjecne: ", round(zarade_mean - najmanja_plata,2))
print("Odstupanje najvece od prosjecne: ", round(zarade_mean - najveca_plata,2))

