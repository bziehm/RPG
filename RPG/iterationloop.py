userinput = True
print(userinput)

userinput = input("Enter Data<")

def iterloop(userinput):
    result=0
    print("enter q or quit to exit")
    if userinput.lower() == "q" or userinput.lower() == "quit":
        userinput = False
    else:
        userinput = True

while True:
    userinput
else:
    print("end program")
