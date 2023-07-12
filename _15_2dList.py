
textSeperate = "--- === *** === ---"

# 1 layer list
list1layer = [1, 2, 3, 4, 5, 6]
# 2d (multi layer) list
list2layer = [[1, 2],
              [2, 3],
              [3, 4],
              [4, 5, 6]]

print (list2layer[2][1])
print (textSeperate)
print (list2layer[3][1])
print (textSeperate)

#nested loop

for list1 in list2layer:
    for detail in list1:
        print(detail)
print (textSeperate)
