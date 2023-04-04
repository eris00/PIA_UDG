num = 2365

str = str(num)

# for x in str:
#     print(x)

prva_cif = str[0]
posljednja_cif = str[-1]

zbir_prva_posljednja = prva_cif + posljednja_cif

arr = []
for x in str:
    arr.append(x)

print(arr)
druga_srednja = int(len(arr)/2)
prva_srednja = int(len(arr)/2) - 1
proizvod_prva_druga = prva_srednja * druga_srednja

if zbir_prva_posljednja > proizvod_prva_druga:
    print("Veci")
else:
    print("Manji")


