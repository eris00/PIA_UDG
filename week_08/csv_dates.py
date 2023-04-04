import os
import csv

max_procenat = 0

path = os.path.join(os.path.dirname(__file__), 'google_stock_data.csv')
with open(path, newline='') as file:
    reader = csv.reader(file)
    lista = [row for row in reader]
    for i in range(len(lista) - 1):
        procentualna_razlika = (float(lista[i]["Open"]) - float(lista[i]["Open"]))
        if procentualna_razlika > max_procenat:
            max_procenat = procentualna_razlika
            datumi = lista[i]["Date"] + " " + lista[i + 1]["Date"]

print(round(max_procenat, 0))
print(datumi)
