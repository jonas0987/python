class account:
    def __init__(self,balance,account_no):
        self.bal=100000
        self.acc=1234567

    def debit(self,amount):
        self.bal=self.bal-amount    
        print("Rs ",amount,"was debited")
        print("remaing balance is",self.bal)


    def credit(self,amount):
        self.bal=self.bal+amount    
        print("Rs ",amount,"was credited")
        print("remaing balance is",self.bal)


acc1=account("balance","acc")

acc1.debit(100)
acc1.credit(20)  

