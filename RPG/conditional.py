userinput = input("enter data:")
a= "something arbitrary"
b= "keep trying"
def function1(userinput):
    
    if userinput.lower() == "q" or userinput.lower() == "quit":
        return a
    else:
        return b

test= function1(userinput)
print (test)


