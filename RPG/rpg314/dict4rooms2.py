data = {"key":"value"}
rooms_data = {
    "Prison Cell": "A cold bare cell, A bed with no sheets lays in the corner,",
    "Hallway": "A narrow hallway with a guard room to the East and another prison cell to the west.",
    "guards": "Guard Room watching the Exit.",
    "unlocked cell": "An empty cell with a bed in one corner and a toilet in the North wall.",
    "room behind toilet": "Appears to be a hole behind the toilet that leads to a small plumbing room.",
    "exit to freedom": "There is an exit to the north through the plumbing pipes. "}


userinput=""

def iterloop(userinput):
    
    while True:
        userinput = str(input("type here"))
        if userinput.lower() == "q" or userinput.lower() == "quit":
            print ("goodbye")
            break
        else:
            userinput

call=iterloop(userinput)
print (call)

import csv as cv
required_row=str(input()) 
row_counter=0 
with open('RPGRooms.csv','r') as F0:
    for row in F0:
        row_counter+=1
        if row_counter==required_row:
            print(row)
    		 

            
