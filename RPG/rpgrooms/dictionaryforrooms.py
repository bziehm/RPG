
Dict4Rooms = {}
data = {"key":"value"}
rooms_data = {
    "Prison Cell": "Description 1",
    "Hallway": "Description 2",
    "guards": "Description 3",
    "unlocked cell": "description 4",
    "room behind toilet": "Description 5",
    "exit to freedom": "Description 6"}
    
import csv
directions="RPGrooms.csv"
 
DictionaryRooms()
with open (directions, 'r') as data:
    
    for line in csv.DictReader(data):
        print(line)
