
var_str = "sutkovic"
# print(var_str)

''' Duzina stringa '''
# print(len(var_str))

''' Stringovi 1 '''
'''
str1 = ' Prvi'
str2 = 'drugi'
str3 = "neki, str"
# print(str1 + str2) # spajanje stringova
# print(str2 * 3) # kopira string 3 puta
# print(str1.lower())
# print(str1.upper())
# print(str1.strip()) # uklanja whitespace sa pocetka i kraja stringa
# print(str3.replace("str","string")) #prvi argument iz stringa nad kojim se poziva funkcija se mijenja sa stringom iz drugog argumenta
# print(str3.split(',')) #razbija string po proslijedjenom separatoru i stavlja ga u listu
'''

''' Stringovi 2 '''
'''
strn = "Ja se zovem Eris. Ja sam developer."
substrn = "Ja"

# print(strn.count(substrn)) #vraca koliko u stringu nad kojim se poziva funkcija ima stringova koji su identicni kao proslijedjeni string - 2
# print(strn.find("zovem")) # vraca index prvog pojavljivanja karaktera od proslijednjenog indeksa
# print(substrn.isalnum()) # provjerava jesu li svi karakteri stringa alfanumericki
# print(substrn.isalpha())
# print(substrn.isnumeric())
# print(strn.islower())
# print(strn.isspace()) # provjerava jesu li svi karakteri stringa whitespace
# print(substrn.istitle()) # Da li je u stringu samo prvo slovo veliko
# print(strn.startswith("Ja")) # Da li string zavrsava na proslijednjeni string
# print(strn.endswith("developer.")) # Da li string zavrsava na proslijedjeni string
'''


''' Stringovi preko indexa '''
'''
print(var_str[0]) # char na prvom indexu
print(var_str[-1]) # zadnji char stringa
print(var_str[2:]) # od drugog indexa do kraja stringa
print(var_str[:5]) # od pocetka stringa do petog indexa
print(var_str[2:-2]) # od drugog indexa do predzadnjeg chara
print(var_str[:-1]) # string bez zadnjeg chara
print(var_str[::2]) # svaki drugi char pocevsi od prvog
print(var_str[2::2]) # pocevsi od drugog indexa vraca svaki drugi char
'''

''' VJEZBANJE  '''



f_name = input("Unesi ime: ")
l_name = input("Unesi prezime: ")
age = int(input("unesite godine: "))
city = input("Grad: ")

def printing(fname, lname, age, city):
    print("INFORMACIJE O KORISNIKU: ")
    print("Ime i prezime: " + fname + " " + lname)
    print("Godine: " + str(age))
    print("Grad: " + city)

def checkAge(age):
    if age < 18:
        print("Maloljetni ste!")
    else:
        printing(f_name, l_name, age, city)

checkAge(age)















