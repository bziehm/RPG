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
        userinput = str(input("Enter a Room Name to see Description: (Type q or quit to exit)"))
        if userinput.lower() == "q" or userinput.lower() == "quit":
            print ("goodbye")
            break
        else:
            import csv

with open('RPGrooms.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)
call=iterloop(userinput)
print (call)


    		 

            
