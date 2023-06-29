# different data type
# parameter initial is english , neither number nor "_"
name = "edmund"
name1 = 123
name2 = "123"
name3 = True
name4 = False
name5 = 123.546
# print (name + name1  + name2 + name3 + name5 + name4) #errorL: TypeError: can only concatenate str (not "int") to str
combineA = (name + str(name1) + name2 + str(name3) + str(name5) + str(name4))

print(combineA)
print(combineA.lower())
print(combineA.upper())
print(combineA.isupper())
print(combineA.islower())
print(combineA.upper().isupper())
print(combineA.lower().islower())
print(combineA[1])  # always start from 0
print(combineA.index("d"))  # show the index of the word, only show the 1st 1
print(combineA.replace("d", "D"))
