class Bank:
    
    name_bank="State Bank Of India"
    count=0
    
    def __init__(self):
        self.name=input("Enter Name of client(first and last name):")
        self.balance=int(input("Enter deposit amt:"))
        self.type=input("Enter type of account:")
        Bank.count=Bank.count+1
        self.Account_Number=Bank.count
        self.password=self.Account_Number*1000 + 1
        
        
    def withdraw(self,amt):
        pwd=int(input("Enter Password:")) # if password entered wrong then money can't be withdraw
        if(pwd==self.password):
            if(amt < self.balance):
                self.balance=self.balance-amt
                print("After Withdraw Balance is:",self.balance)
                if(self.balance < 250):
                    print("Current Balance is less than minimum balance which is 250")
            else:
                print("Funds are insufficient")
        else:
            print("wrong password,Can't withdraw money from",self.name,"account")
            
                     
    def deposit(self,amt):
            self.balance=self.balance + amt
            self.Balance()
     
    def Balance(self):
        print("Current Balance is:",self.balance)
        if(self.balance < 250):
            print("Current Balance is less than minimum balance which is 250")
        
    def details(self):
        print("Account Holder Name is:",self.name)
        print("Account Number is",self.Account_Number)
        print("Account Type is:",self.type)
        self.Balance() # gets the current balance.
    
#creating Client class and inherit it with Bank class
       
class Client(Bank):
    pass


#creating objects of client class
c1=Client()
print(c1.name_bank)
c1.details()

print() #for new line printing only

c2=Client()
c2.details()

print() #for new line printing only

c3=Client()
c3.details()

print()

c1.withdraw(1800)

print()

c2.withdraw(200)
c2.deposit(600)

print()
c3.withdraw(200)
c3.deposit(300)

