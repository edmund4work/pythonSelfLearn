def where2eat(mood, money):
    eatAt = ""
    if mood == "good" and float(money) > 100:
        eatAt = "mamak"
    elif mood == "bad" and float(money) >= 80:
        eatAt = "mcd"
    elif mood == "good" or float(money) < 80:
        eatAt = "steamboat"
    elif mood != "good" and not (float(money) < 100):
        eatAt = "buffet"
    else:
        eatAt = "home"

    return eatAt


a = input("mood good?")
b = input("how much you have?")
print(where2eat(a, b))
