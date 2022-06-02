print("RBI")

class Bank(object):
    def __init__(self,bank,amountToBePaid,cashlimit,Bankbalance):
        self.bank=bank
        self.amountToBePaid=amountToBePaid
        self.cashlimit=cashlimit
        self.Bankbalance=Bankbalance

 
   
    
    def limit (self):
        print("limit is 15000")
    def balance (self):
        print("YOUR BALANCE IS 35000 ")
    def amount (self):
        print("AMOUNT TO BE PAID IS 10000")

        print("YOUR RESPECTIVE BANK DETAILS")   


RBI=Bank("RBI",10000,15000,35000)
print(RBI.limit())
print(RBI.balance())
print(RBI.amount())

