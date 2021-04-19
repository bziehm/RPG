userinput = input("<")
userinput = True
b = "false"
def iterloop(userinput):
    if userinput.lower() == "q" or userinput.lower() == "quit":
        userinput = False
    else:
        userinput = True

while userinput == True:
    print(userinput)
