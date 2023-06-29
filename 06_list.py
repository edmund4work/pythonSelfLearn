scoreList = [90, 123, 12, 34, 56, 78, 99, 123]
print(scoreList)


scoreList.sort()  # sorting, only for number
print(scoreList)
scoreList.reverse()
print(scoreList)

print(scoreList.index(123))
print(scoreList.count(123))

peopleChinese = ["edmund", "爱门", "scorelist", "0.21", "123", 1234]
print(peopleChinese)
print(peopleChinese[2])
print(peopleChinese[-2])  # last 2nd
print(peopleChinese[1:3])  # take from 2nd until 3rd
print(peopleChinese[1:])  # take from 2nd until end
print(peopleChinese[:3])  # take from 3rd until 1st
peopleChinese[2] = "ohaiyok"
print(peopleChinese)

nameEdmund = "Hello Edmund, Welcome to world"
print(nameEdmund[3:9])

peopleChinese.append("爱门")  # append means append 1 more value into list
print(peopleChinese)

# insert means insert 1 more value into list with mention which position
peopleChinese.insert(2, "insert new value")
print(peopleChinese)

peopleChinese.remove("爱门")  # remove means remove the 1st value found from list
print(peopleChinese)

peopleChinese.extend(scoreList)  # combine list
print(peopleChinese)

peopleChinese.pop()  # delete the last record from list
print(peopleChinese)

peopleChinese.clear()  # clear from list
print(peopleChinese)
