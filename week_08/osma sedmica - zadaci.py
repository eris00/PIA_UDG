'''
import datetime
import csv

datum = datetime.date(1995, 2, 25)
print(datum)

#print(datum.day)

dt = datetime.timedelta(100)

#print(datum - dt)

print(datum.strftime("%B %A-%d, %Y"))

datum_prosiren = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(datum_prosiren)

# Izracunati koliko dana je proslo od upisa na vase studije.

now = datetime.datetime.now()
print(now)

danasnji_dan = datetime.date.today()
datum_upisa = datetime.date(2012, 9, 10)

print((danasnji_dan - datum_upisa).days)

max_procenat = 0
datumi = ""
with open("google_stocks.csv", "r") as file:
    reader = csv.DictReader(file)
    lista = [row for row in reader]
    for i in range(len(lista) - 1):
        procentualna_razlika = (float(lista[i]["Open"]) - float(lista[i+1]["Open"])) / float(lista[i+1]["Open"]) * 100
        if procentualna_razlika > max_procenat:
            max_procenat = procentualna_razlika
            datumi = lista[i]["Date"] + " " + lista[i + 1]["Date"]

print(round(max_procenat, 0))
print(datumi)

with open('google_stocks.csv','r') as f:
    with open('razlika.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(["Datum","Razlika"])
        csv_reader = csv.reader(f,delimiter=',')
        header=next(csv_reader)
        lista = [row for row in csv_reader]
        i=0
        j=0
        while i<len(lista)-1:
            j=i+1
            razlika = 100*(float(lista[i][1])-float(lista[j][1]))/float(lista[j][1])
            writer.writerow([lista[i][0],str(razlika)])
            i+=1

'''
'''
import json
x = '{"name":"John", "age":30, "city":"New York"}'

y = json.loads(x) # pretvara string u json 
print(y)
print(type(y))

z = json.dumps(y)
print(z)
print(type(z))

with open("test.json", "r") as json_file:
    content = json.load(json_file)
    print(content)
    print(type(content))
    print(content["data"][0]["children"][0]["firstName"])

with open("new_test.json", "w") as json_file:
    json.dump("neki string", json_file)
'''
from urllib import request

resp = request.urlopen("https://en.wikipedia.org/wiki/Supercomputer")

data = resp.read()
print(data)