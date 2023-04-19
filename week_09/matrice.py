# Prolaz kroz matricu
'''
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
#
# # Prolazimo kroz matricu red po red
# for i in range(len(matrix)):
#     # Prolazimo kroz svaki element u redu
#     for j in range(len(matrix[i])):
#         # Ispisujemo svaki element u redu
#         print(matrix[i][j], end=' ')
#     # prelaz u novi red
#     print()
'''

# Sabiranje dvije matrice
'''
# Kreiramo dve matrice
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]
#
# # Sabiramo dve matrice i dodeljujemo rezultat matrici C
# C = [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]]
#
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         C[i][j] = A[i][j] + B[i][j]
#
# # Ispisujemo rezultat
# for row in C:
#     print(row)
'''

# mnozenje dvije matrice
'''
# Kreiramo matricu A
A = [[1, 2, 3],
     [4, 5, 6]]

# Kreiramo matricu B
B = [[7, 8],
     [9, 10],
     [11, 12]]

# Inicijalizujemo matricu C sa nulama
C = [[0, 0],
     [0, 0]]

# Množenje matrica
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

# Ispisujemo rezultat
for row in C:
    print(row)
'''


# Sabrati sve parne vrijednosti sa dijagonale matrice
'''
A = [[2, 5, 7],
    [3, 9, 12],
    [4, 4, 8]]

suma = 0
for i in range(0, len(A)): #prolaz kroz redove
    for j in range(0, len(A[0])): #prolaz kroz kolone
        if i == j and A[i][j] % 2 == 0:
            suma += A[i][j]
print(suma)
'''

# Sabrati sve parne vrijednosti sa SUPROTNE dijagonale matrice
'''
A = [[2, 5, 7],
    [3, 9, 12],
    [4, 4, 8]]

suma = 0
for i in range(0, len(A)): #prolaz kroz redove
    for j in range(0, len(A[0])): #prolaz kroz kolone
        if i+j+1 == len(A) and A[i][j] % 2 == 0:
            suma += A[i][j]
'''

# Sabrati sve vrijednosti sa omotaca matrice
'''
# Kreiramo matricu
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

# Inicijalizujemo sumu na 0
sum = 0

# Sabiramo elemente na omotacu matrice
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0 or i == len(matrix)-1:
            sum += matrix[i][j]
        elif j == 0 or j == len(matrix[i])-1:
            sum += matrix[i][j]

# Ispisujemo sumu
print(sum)
'''



