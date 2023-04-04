""" 1 Napisati program kojim se za n-tocifreni broj provjerava da li je zbir prve i posljednje cifre veci od proizvoda dvije srednje cifre... """

num = 34975132

def check_fun(num):

    snum = str(num)

    mid = int(len(snum) / 2)
    first = snum[0]
    last = snum[-1]

    first_last = int(first + last)

    first_mid = int(snum[mid-1])
    last_mid = int(snum[mid])

    mid_product = first_mid * last_mid

    if (num % 2) == 0 and first_last > mid_product:
        return True
    else:
        if int(snum[mid]) > first_last:
            return True
        else:
            return False
        
# print(check_fun(num))


""" 3. zadatak - vrati film koji ima najbolji odnos pozitivnih i negativnih komentara """

movies = [
    {"naziv":"Harry Potter", "br_pozitivnih":500, "br_negativnih":30},
    {"naziv":"A beautiful mind", "br_pozitivnih":600, "br_negativnih":45},
    {"naziv":"The Runner", "br_pozitivnih":380, "br_negativnih":425}
]

odnos = []


for x in movies:
    poz = x["br_pozitivnih"]
    neg = x["br_negativnih"]
    odnos.append(poz)
    odnos.append(neg)

print(odnos)
print(len(odnos))
arr = []

i = 0
while i <= len(odnos) + 1:

    fin_value = odnos[i] + odnos[i+1]
    arr.append(fin_value)
    i += 1

print(fin_value)










