
# let user key in the figure and see how many time they can try
userInput = ""
ourFinalAnswer = 77
guessNo = None
tryNo = 0
tryNoEnd = 6

while (guessNo != ourFinalAnswer) and (tryNo <= tryNoEnd):
    guessNo = int(input("guess what is the number."))
    messsageReturn = ""
    if guessNo > ourFinalAnswer:
        messsageReturn = "less a bit"
    elif guessNo < ourFinalAnswer:
        messsageReturn = "more a bit"
    else:
        messsageReturn = "congraz. finally a"

    tryNo += 1
    print("you key in : " + str(guessNo))
    print(messsageReturn + ". you have tried [" + str(tryNo) + "]")
    if tryNo > tryNoEnd and guessNo != ourFinalAnswer:
        print("you use all the try")
    else:
        print("you still can try :" + str(tryNoEnd - tryNo) + " times,")
