import csv
directions="directions.csv"
 
with open (directions, 'r') as data:
    
    for line in csv.DictReader(data):
        print(line)


    
