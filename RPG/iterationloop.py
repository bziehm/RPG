userinput = True
print(userinput)

userinput = input("Enter Data<")
print(userinput)
def iterloop(userinput):
    if userinput.lower() == "q" or userinput.lower() == "quit":
        userinput = False
    else:
        userinput = True

while userinput != "q" or "quit":
    userinput
