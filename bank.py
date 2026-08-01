Accounts = {}
next_account_id = 12001


#create account 

def Create_account():
    global next_account_id
    name = input("tell us your name ").strip()
    mobile_number = int(input("Tell us your mobile number "))

    Accounts[next_account_id] = {
        "name" : name ,
        "mobile_number" : mobile_number,
        "balance" : 0,
        "transactions": []
    }

    print (f"{name} your account has been created sucessfully! ")
    print (f"your account number is {next_account_id}")

    next_account_id +=1

#Add balance

def add_balance():
    while True:
        Account_number = int(input("enter your account number = ")) 

        if Account_number in Accounts:
            print ("account found sucessfully! ")
            Add_amount = int(input("how much to add = "))
            Date = (input ("enter today date= "))
            Accounts [Account_number]["balance"] += Add_amount
            print (f"new balance= {Accounts [Account_number]['balance']}")
            Accounts[Account_number]["transactions"].append ({"transaction": "Deposit", "Amount" : Add_amount , "Date" : Date })
            break

        else:
            print("account not found")

def Withdraw_balance():
    

    while True:
        Account_number = int(input("enter your account number = ")) 

        if Account_number in Accounts:
            print ("account found sucessfully! ")
            Withdraw_amount = int(input("how much to withdraw = "))
            Date = (input ("enter today date= "))
            Accounts [Account_number]["balance"] -= Withdraw_amount
            print (f"new balance= {Accounts [Account_number]['balance']}")
            Accounts[Account_number]["transactions"].append ({"transaction": "Withdraw", "Amount" : Withdraw_amount , "Date" : Date })
            break

        else:
            print("account not found")

def veiw_transactions():
     

    while True:
        Account_number = int(input("enter your account number = "))

        if Account_number in Accounts:
            print ("account found sucessfully! ")
            transcations = Accounts[Account_number]["transactions"]
            print (transcations)
            break

        else: 
            print("account not found ")

def balance():

    while True:
        Account_number = int(input("enter your account number = "))

        if Account_number in Accounts:
            print ("account found sucessfully! ")
            balance_ = Accounts[Account_number]["balance"]
            print (balance_)
            break

        else: 
            print("account not found ")




while True:
    print ("\nchoose your one choice ")
    print ( "1.create account","2.add amount","3.withdraw amount","4.balance","5.transaction history","6.exit", sep='\n' )
    inputs = int (input("tell the number of your choice "))

    if inputs == 1:
        Create_account()

    elif inputs == 2:
        add_balance()

    elif inputs == 3:
        Withdraw_balance()

    elif inputs == 4:
        balance()

    elif inputs == 5:
        veiw_transactions()

    elif inputs == 6:
        print("thanks for choosing us ")
        break

    else:
        print("invalid choice ")