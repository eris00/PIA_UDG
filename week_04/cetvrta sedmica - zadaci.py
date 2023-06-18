'''
# 1 - 66

string = 'abaae'
enk_string = ''
for char in string:
    if char in "aeiouAEIOU":
        enk_string = enk_string + '1'
    else:
        enk_string = enk_string + '0'
print(enk_string)

# 1 - 69
# prvi nacin
n= "12111"

a= int(n[0])
b= int(n[1])
c= int(n[2])
d= int(n[3])
e= int(n[4])

if (a*c+2)==(b+d*e):
    print("Uslov je zadovoljen")
else:
    print("Uslov nije zadovoljen.")

#drugi nacin

n=12345
a=n//10000 %10
b=n//1000 %10
c=n//100%10
d=n//10%10
e=n%10
if a*c+2==b+d*e:
    print("Uslov je zadovoljen")
else:
    print("Uslov nije zadovoljen")


# 1 - 71

s = '1234'
suma = 0
for i in s:
    suma = suma + int(i)
srednja_vr = suma/len(s)
print(srednja_vr)


# 2 - 1

def absolute_of_even_sum(niz):
    suma = 0
    for i in niz:
        if i < 0 and i % 2 == 0:
            suma += abs(i)

    return suma
niz=[-2, 1, -4, 3]
print(absolute_of_even_sum(niz))

# 2 - 2
def suma_kuca(kuce):
    suma = 0
    for kuca in kuce:
        if kuca == 0:
            break
        suma += kuca
    return suma

kuce=[5,1,2,3,0,1,5,0,2]
print(suma_kuca(kuce))

# 2 - 3

def presjek(a,b):
    novi_niz = []
    for i in a:
        if i in b:
            novi_niz.append(i)
    return novi_niz

a = [2, 4, 'j']
b = [4, 7, 'j']

print(presjek(a,b))

# 2 -6

def update_list(a, x):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] += x
    return a

a = [1, 2, 3, -4]
print(update_list(a, 1))

'''