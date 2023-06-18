# Zadaci sa fajlovima - 3. zadatak
grad = ''

with open('population.txt') as f:
    line = f.read().split('\n')
    #print(line)
    for i in line:
        #print(i)
        splitted = i.split(',')
        #print(splitted)
        if splitted[0] == 'Poljska':
            current_min = splitted[2]
            if int(current_min) >= int(splitted[2]):
                current_min=splitted[2]
                #print(current_min)
                grad = splitted[1]

print(grad)