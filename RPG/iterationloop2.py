userinput=""

def iterloop(userinput):
    
    while True:
        userinput=input("type here")
        if userinput.lower() == "q" or userinput.lower() == "quit":
            print ("goodbye")
            break
        else:
            userinput

call=iterloop(userinput)
print (call)

            
                    
