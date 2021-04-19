userinput = True
print(userinput)

userinput = input("<")
print(userinput)
def iterloop(userinput):
    if userinput.lower() == "q" or userinput.lower() == "quit":
        userinput = False
    else:
        userinput = True

while userinput != "q" or "quit":
    print(userinput)
