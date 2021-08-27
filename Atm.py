class Atm:
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def checkbal(self):
        print("You have a balance of $50000")

    def withdraw(self,amount):
        newamount=50000-amount
        print("You have withdrawn",amount,"and the balance is",newamount)

def main():

 cardnumber= input("Enter the Card Number")
 pinnumber=input("Enter the Pin Number")

 newuser=Atm(cardnumber,pinnumber)
 print("Enter 1 for balance, Enter 2 for withdrawal of money")
 inputinfo=int(input("Enter the number")) 
 print(inputinfo) 
 if (inputinfo == 1): 
     newuser.checkbal() 
     print("bal") 
 elif (inputinfo==2):
    print("with")
    enteramount=int(input("Enter the amount you want to withdraw"))
    newuser.withdraw(enteramount) 
 else: print("It is not a valid entry")

main()

        