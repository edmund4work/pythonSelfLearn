# this print some test
print('hellow 生活')

# when make a parameter, not need to give data type.
redBudget = 'agb'
redBudget = '123456'
print(redBudget)
print(type(redBudget))
# del redBudget #delete variable.

print(1 == 3)
print(1 != 3)
print(1 >= 3)
print(1 <= 3)

# if else statement
nunmberA = 999
if (nunmberA < 100):
    print("abcderf")
elif (nunmberA < 300):  # elif is else if
    print("abcderf")
elif (nunmberA < 500):  # elif is else if
    print("abcderf")
else:
    print(nunmberA)

# create function


def printEdmund(newText, newInt):  # define function
    text = 'adfadfads'
    if newText != '':
        text += newText
        for newInt2 in range(newInt):
            print(newInt2, ' ', text)
        else:
            print(newInt, "~ Finally finished!")


printEdmund(' ~edmund ', 2)

# for clear the command in terminal, use clear or cls
