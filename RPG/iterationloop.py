userinput = True
print(userinput)

userinput = input("Enter Data<")

def iterloop(userinput):
    
    print("enter q or quit to exit")
    while True:
        
        if userinput.lower() == "q" or userinput.lower() == "quit":
            return quit()
           
    
        else:
            return userinput

iloop = iterloop(userinput)

print(iloop)
