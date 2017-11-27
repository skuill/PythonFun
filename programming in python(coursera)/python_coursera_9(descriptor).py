class Value:
    def __init__(self):
        print ('__init__')
    def __get__(self, obj, obj_type):
        print ('__get__')
        return self.amount
    def __set__(self, obj, value):
        print ('__set__', value)
        self.amount = value * (1 - obj.commission)
        
    
class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission
        
new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
new_account.amount = 120
print(new_account.amount)