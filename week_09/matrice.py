
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
A = [[2, 5, 7],
    [3, 9, 12],
    [4, 4, 8]]
suma=0



