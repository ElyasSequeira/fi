class Account():

    def __init__(self,idepo):
        self.idepo = idepo



    def deposit(x):
        print("DEPOSIT AMOUNT:", x)
        Account.balance
        return

    def withdrawal(y):
        print ("WITHDRAWAL AMOUNT:", y)
        
        return


    def balance(idepo,x,y):
        print ("Current Balance Balance:", (idepo + x - y))
        return
        


idepo = float(input("Hello! Please Enter in the initial deposit amount: "))
print("Depositing amount of:", idepo)

path = input("\nPlease select one of the following: \n1. Deposit\n2. Withdrawal\n 3.Exit(ENTER)\n")
x = float(input("\nPlease Enter in the amount you would like to deposit: "))
y = float(input("Please Enter in the amount you would like to withdraw: "))


if path == "1":
    print("Deposit Selected")
    Account.deposit(x)
    Account.balance(idepo,x,y)
elif path == "2":
    print("\nWithdraw selected.")
    Account.withdrawal(y)
    Account.balance(idepo,x,y)
else:
    pass