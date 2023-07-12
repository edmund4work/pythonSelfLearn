class Questions01 :
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer

    def run_test(Questions01):
        score = 0
        for question in Questions01:
            asnwer = input(question.description)
            if(asnwer == question.answer):
                scrore += 1
        
        print ("you get :" + str(score) + ". total questions: " + str(len(Questions01)))

    run_test(questions01)