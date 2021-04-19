

rooms_data = {
    "Prison Cell": "Description 1",
    "Hallway": "Description 2",
    "guards": "Description 3",
    "unlocked cell": "description 4",
    "room behind toilet": "Description 5",
    "exit to freedom": "Description 6"}
    
import csv

with open('rpgrooms.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)

