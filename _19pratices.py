# import _19apraticesQuestion #import all file
from _19apraticesQuestion import  Questions01 #import only the function in the file


test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1m = how many cm？\n(a) 10\n(b) 100\n(C) 1080 \n\n",
    "香蕉是什麼顏色？\n(a）黑色\n(b）黃色\n(C）白色\n\n"
]
# print (test[0]) 

questions = [
    Questions01(test[0],"A"),
    Questions01(test[1],"B"),
    Questions01(test[2],"C"),
]

def run_test(questions):
    score = 0
    for question in questions:
        asnwer = input(question.description)
        if(asnwer == question.answer):
            score += 1
        
    print ("you get :" + str(score) + ". total questions: " + str(len(questions)))

run_test(questions)