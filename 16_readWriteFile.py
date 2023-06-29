
seperateStr = "--- === *** === ---"
file = open("16_readWriteFile.txt",mode="r")

# mode="r" : read
# mode="w" : write
# mode="a" : read and write
print (file.readline()) #read 1 line
print(seperateStr)
print (file.read()) #read all


file.close()

print(seperateStr)
with open('16_readWriteFile.txt', 'r') as G:
    print(G.read())