'''
U fajlu link nalaze se dimenzije pravougaonika (svaki red u fajlu je kombinacija stranica pravougaonika a i b, vrijednosti su razdvojene zarezom).
Pretpostaviti da se uvijek radi o prirodnim brojevima. Vaš zadatak je da iz fajla izdvojite sve pravougaonike koji su kvadrati (a = b), i da
štampate površinu najvećeg kvadrata.
Za ovaj primjer output bi trebao da bude 16 (kvadrat sa najdužim stranicama je poslednji, čija je dužina stranica 4).
'''

''' MOJ NACIN '''

# file = open('txtfiles/file1.txt', 'r+')
#
# content = file.read()
#
# lines = content.split('\n')
#
# kvadrati = []
# povrsine = []
# i = 0
# while i < len(lines):
#     vals = lines[i]
#     if vals[0] == vals[2]:
#         kvadrati.append(lines[i])
#
#     i += 1
#
# for x in kvadrati:
#     povrsine.append(int(x[0]) * int(x[2]))
# pov_najv_kvadrata = max(povrsine)
#
# print("Pravougaonici koji su kvadrati: ")
# for x in kvadrati:
#     print("pravougaonik: ", x)
# print("Povrsina najveceg kvadrata: ", pov_najv_kvadrata)



''' CHATGPT '''
file = open('txtfiles/file1.txt', 'r+')

kvadrati = []
max_povrsina = 0

for line in file:

    a, b = line.strip().split(',')
    a = int(a)
    b = int(b)

    if a == b:
        kvadrati.append(str(a) + ',' + str(b))
        povrsina = a * b
        if povrsina > max_povrsina:
            max_povrsina = povrsina

file.close()

print('pravougaonici koji su kvadrati: ', kvadrati)
print('povrsina najveceg kvadrata: ', max_povrsina)






