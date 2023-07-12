
i = 0

while i <=5 :
    print (i)
    i += 1


print("reverse")
while i >=0 :
    print(i)
    i-=1


#pow(2,6)
def powerFn2(baseNo, powNo) :
    result = baseNo
    noLoop = 1
    print ("result now is: " + str(result))
    while powNo > noLoop :
        result *= baseNo
        print ("result now is: " + str(result))
        noLoop+=1
    return result

print (powerFn2(2,6))
