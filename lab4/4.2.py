class Bank_ac:
    
    def __init__(self,ac_no,ac_name,type_ac):
        
        self.ac_no=ac_no
        self.ac_name=ac_name
        self.type_ac=type_ac
        self.balance=0
    def deposite(self):
        amt=float(input("enter the amount to deposit:"))
        self.balance=self.balance+amt

    def withdrawal(self):
         amt=float(input("enter the amount to withdraw:"))
         if amt > self.balance:
             print("Balance not sufficient")
         else:
             self.balance=self.balance-amt

    def check_balance(self):
        print("balance is :",self.balance)

ac_no=int(input("enter the ac number:"))
ac_name=input("enter the ac holder name:")
ac_type=input("enter the ac type:")

obj=Bank_ac(ac_no,ac_name,ac_type)

print("1.DEPOSIT")
print("2.WITHDRAWAL")
print("3.CHECK BALANCE")



while(True):
	c=int(input("Enter the choice:"))
	if c==1:
	      obj.deposite()
	elif c==2:
	      obj.withdrawal()
	elif c==3:
	      obj.check_balance()
	else:
	      break

