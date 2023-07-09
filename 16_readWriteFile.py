
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

print(seperateStr)
with open('16_readWriteFile.txt', 'w') as G:
    G.write("a new line with mode w") #due to mode is 'w', so only overwrite. 

print(seperateStr)
with open('16_readWriteFile.txt', 'a') as G:
    G.write("\na new line with mode a") #if wanna write append the file, can try this. mode = a

print(seperateStr)
with open('16_readWriteFile.txt', 'a', encoding='utf-8') as G:
    G.write("\na 中文 mode a") #if wanna write chinese or non-english append the file, can try this. mode = a
