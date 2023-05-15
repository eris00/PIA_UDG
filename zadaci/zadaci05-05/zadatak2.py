import csv

with open('2019.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    # svi djelovi:
    arr = []
    healty_life_expec = []
    avg = 0
    score_higher_7 = 0
    for row in reader:
        score = float(row[2])
        arr.append(score)
        avg = sum(arr) / len(arr)


        if score > 7:
            score_higher_7 += 1


        if score < 5:
            h_l_e = row[6]
            healty_life_expec.append(h_l_e)

            avg_hle = sum(healty_life_expec) / len(healty_life_expec)













    #print(avg)
    #print(score_higher_7)

