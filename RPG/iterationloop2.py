userinput=input("type here>")
b =userinput
a = quit()
def iterloop(userinput):
    userinput = ''
    while True:
        if userinput.lower() != "q" or userinput.lower() != "quit":
            userinput=False
        else:
            userinput=True

call=iterloop(userinput)
print(call)
            
            
                    
