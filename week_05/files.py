import os

# Otvaranje fajla
# file1 = open("txtfiles/text.txt", "r")

''' Citanje fajla funkcijom read '''
# content = file1.read()
# print(content)

''' Citanje iz fajla kroz petlju '''
# for line in file1:
#     print(line)
# file1.close()

''' Append mod '''
# file2 = open("txtfiles/file.txt", "a")
# file2.write("Podaci koji ce biti unijeti u fajl")
# file2.write("Novi podaci koji ce biti unijeti, opet")
# file2.close()

''' Read mod '''
# file3 = open("txtfiles/file3.txt", "w")
# file3.write("Unesen upis u file3")
# file3.close()
# # kada isti fajl zelimo da procitamo, otvaramo ga ponovo u drugom modu:
# file3 = open("txtfiles/file3.txt", "r")
# content = file3.read()
# print(content)
# file3.close()

''' With block i parametar u read() '''
# with open('txtfiles/file4.txt', 'r') as f4:
#     content = f4.read(5) #ispise prvih 5 karaktera
# print(content)

''' Seek metod '''
# with open('txtfiles/file4.txt', 'r') as fl4:
#     fl4.seek(150) # pozicioniramo se na 150-om karakteru u fajlu
#     content = fl4.read(15) # citamo 15 karaktera od 150-og karaktera u fajlu
#     print(content)

# Kada zelimo da unesemo neki tekst na odredjenoj poziciji karaktera:
# with open('txtfiles/file5.txt', 'r+') as fl5: #r+ mod je read i write mod ujedno
#     fl5.seek(50)
#     fl5.write('UNOSIM OVAJ TEXT OD 50og KARAKTERA!')

''' Preskakanje redova readline metodom '''
# with open('txtfiles/file5.txt', 'r+') as f5:
#     # f5.readline() #izdvajanje jedne linije
#     for i in range(13): #preskakanje vise linija
#         f5.readline()
#     print(f5.read())

''' Izdvajanje odredjene linije iz fajla '''
# with open('txtfiles/file5.txt') as splitfl:
#     content = splitfl.read()
#     all_lines = content.split('\n')
#     line2 = all_lines[1]
# print(line2)

''' brisanje fajla '''
# os.remove('txtfiles/remov.txt')

with open("txtfiles/file5.txt", "r") as f:
    print(f.readlines())






