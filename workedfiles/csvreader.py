import csv

def readera(file):
    f = open('static/'+file.filename,'r')
    reader = csv.reader(f)
    for row in reader:
        print(row)

    f.close()
