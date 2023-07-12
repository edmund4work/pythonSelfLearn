
class Phone: 
    def __init__(self, os, number, is_waterproof) :
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
        
phone01 = Phone("ios", 123, True)
phone02 = Phone("android", 2345, False)


print(phone01.os)
print(phone02.os)