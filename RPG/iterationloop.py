userinput = True
print(userinput)

userinput = input("Enter Data<")

def iterloop(userinput):
    result=0
    print("enter q or quit to exit")
    while True:
        if userinput.lower() == "q" or userinput.lower() == "quit":
            return result
        else:
            result += userinput

iloop = iterloop()
