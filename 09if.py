def where2eat(mood) :
    eatAt = ""
    if mood == "good" :
        eatAt = "mamak"
    elif mood=="bad":
        eatAt   = "mcd"
    else :
        eatAt = "home"

    return eatAt


