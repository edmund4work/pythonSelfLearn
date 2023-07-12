class phoneModel :
    def __init__(self, os01, number01, isWaterProof01) :
        self.os = os01
        self.number = number01
        self.isWaterProof = isWaterProof01

    def isIOS (self) : 
        if(self.os == "IOS") : 
            return True
        else : 
            return False
        
    def addNumber (self,number01, number02) : 
        return number01 + number02
    
phone1 = phoneModel("IOS2", 2, True)
print (phone1.isIOS())
print (phone1.addNumber(2,3))