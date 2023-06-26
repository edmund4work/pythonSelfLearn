
no1 = float(input("key in number 1: "))
no2 = float(input("key in number 2: "))
calFunc = input("for?")


print ("you've key in : " + str(no1) + " and "+ str(no2) + ".")
returnValue = ""
if(calFunc == "+") :
    returnValue = ("The + value is: " + str(no1 + no2) + ".")
elif calFunc == "-" :
    returnValue = ("The - value is: " + str(no1 - no2) + ".")
elif calFunc == "/" :
    returnValue = ("The / value is: " + str(no1 / no2) + ".")
elif calFunc == "*" :
    returnValue = ("The * value is: " + str(no1 * no2) + ".")
else:
    returnValue = "tahnks"
print (returnValue)