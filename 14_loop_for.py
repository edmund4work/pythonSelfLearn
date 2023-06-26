

seperateStr = "--- === *** === ---"
for words in "o hai yok":
    print(words)
print (seperateStr)


for words in [0,3,6,78,9]:
    print(words)
print (seperateStr)


for words in range(9):
    print(words)
print (seperateStr)


for words in range(2,9):
    print(words)
print (seperateStr)

#pow(2,6)
def powerFn(baseNo, powNo) :
    result = baseNo
    print ("result now is: " + str(result))
    for index in range(1,powNo) :
        result *= baseNo
        print ("result now is: " + str(result))
    return result



print (powerFn(2,6))