filmovi = [
    {"naziv":"Harry Potter", "br_pozitivnih":500, "br_negativnih":30},
    {"naziv":"A beautiful mind", "br_pozitivnih":600, "br_negativnih":45}
]


# print(filmovi[1]["naziv"])

max_poz = 0
for movie in filmovi:
    poz = movie["br_pozitivnih"]
    neg = movie["br_negativnih"]
    max = poz-neg

print(max)
