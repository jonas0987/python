class account:
    def  __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass ##  for private __
         

        
        
        
acc1=account(12212,"aaaaa")
print(acc1.acc_no)
print(acc1.__acc_pass)


