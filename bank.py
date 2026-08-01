import re

class Accounts:

    Next_account_no = 1200
    Account_list = {}

    def __init__(self):
        print(f"Welcome to Our bank")


    def name_validator():
        while True:
            name = input("Tell us your name ").strip()

            if re.search(r"^[a-zA-Z ]+$",name):
                print("valid name")
                return name
            else:
                print ("enter valid name")


    def mobile_num_validator():
        while True:
            mobile_num = input ("tell us your mobile number ")
            duplicate = False

            for Account_no , accounts_list in Accounts.Account_list.items():
                if mobile_num == accounts_list["Mobile_no"]:
                    duplicate = True
                    break

            if duplicate:
                print("This number already exist in data")

            elif re.search(r"^[0-9]{10}$",mobile_num):
                print("Valid number")
                return mobile_num
            else: 
                print("enter valid number")


    def PIN_validator():
        while True:      
            Pin = input (""" Create you PIN 
            ***RULES***
            1. PIN should be of 4 digits
            2. PIN shold be in numbers  """)
            if re.search(r"^[0-9]{4}$",Pin):
                print("Valid PIN")
                return Pin
            else: 
                print("Create Valid PIN")
                


    @staticmethod
    def create_account():

        name = Accounts.name_validator()
        mobile_num = Accounts.mobile_num_validator()
        Pin = Accounts.PIN_validator()
      

        Accounts.Account_list [Accounts.Next_account_no] = { 
            "Name" : name,
            "Mobile_no" : mobile_num,
            "Balance" : 0,
            "Bank_pin" : Pin,
            "Transactions":[]
        }

        print(f"Account created successfull \n {Accounts.Next_account_no}")

        Accounts.Next_account_no += 1


class Validation:

    def acc_num():
        while True:
                try:
                    ac_no = int(input("enter you account number "))
                    return ac_no
                except ValueError:
                    print("please enter correct ac num ")


    def validator(): 
            
            while True:
                ac_no = Validation.acc_num()
                
                if ac_no in Accounts.Account_list:
                    print ("Account found")
                    pin = input ("tell us your pin ")
                    if pin == Accounts.Account_list[ac_no]["Bank_pin"]:
                        return ac_no , True
                    
                    else:
                        print("enter valid pin  ")
                else:
                    print ("enter valid ac number ")


class Banking(Validation):


    def deposit_money():
        ac_no , validate = Banking.validator()
        while True:
            if validate:
                deposit_Amount = input("Give me amount you want to deposit ")
                if re.search(r"^[0-9]+$", deposit_Amount):
                    deposit_Amount = int (deposit_Amount)
                    if deposit_Amount > 0:
                        Accounts.Account_list[ac_no]["Balance"] += deposit_Amount
                        print(f"{deposit_Amount}deposit successfull!!!!\n {Accounts.Account_list[ac_no]['Balance']} ")
                        Accounts.Account_list[ac_no]["Transactions"].append({"Type" : "Deposit" , "Amount" : deposit_Amount })
                        break
                    else:
                        print("amount should be  more than 0 ")
                else:
                    print("enter valid amount ")


    def Withdraw_money():

        ac_no , validate = Banking.validator()

        while True:
            if validate:
                Withdraw_Amount = input("Give me amount you want to Withdraw ")
                if re.search(r"^[0-9]+$", Withdraw_Amount):
                    Withdraw_Amount = int (Withdraw_Amount)

                    if Withdraw_Amount > Accounts.Account_list[ac_no]["Balance"]:
                        print(f"Don't have enough balance \n {Accounts.Account_list[ac_no]['Balance']} is your current balance ")
                        continue

                    if Withdraw_Amount > 0:
                        Accounts.Account_list[ac_no]["Balance"] -= Withdraw_Amount
                        print(f"{Withdraw_Amount}withdraw successfull!!!!\n {Accounts.Account_list[ac_no]['Balance']} ")
                        Accounts.Account_list[ac_no]["Transactions"].append({"Type" : "Withdraw" , "Amount" : Withdraw_Amount })
                        break
                    else:
                        print("amount should be  more than 0 ")
                else:
                    print("enter valid amount ")


    def Transaction_history():
        ac_no , validate = Banking.validator()
        print ("account found sucessfully! ")
        for transaction in Accounts.Account_list[ac_no]["Transactions"]:
            print(transaction)


    def Balance():
        ac_no , validate = Banking.validator()
        print ("account found sucessfully!\n Your balance is ")
        print (Accounts.Account_list[ac_no]["Balance"])


    def Change_pin():
        ac_no , validate = Banking.validator()
        print ("account found sucessfully! ")
        while True:
            
            new_pin = input ("Give us your new pin")
            if re.search(r"^[0-9]{4}$", new_pin):
                print("Valid PIN")
                Accounts.Account_list[ac_no]["Bank_pin"] = new_pin
                print("PIN Changes sucessfully")
                break
            else: 
                print("Create Valid PIN")
            


    def transfer_money():
        senders_ac , validate = Banking.validator()
        print ("account found sucessfully!\n Your balance is ")
        print (Accounts.Account_list[senders_ac]["Balance"])


        
        while True:
            try:
                Receiver_ac = int(input ("enter account number you want to transfer your money to  "))
            except ValueError:
                print ("enter correct account number")
                continue


            if Receiver_ac in Accounts.Account_list and senders_ac != Receiver_ac:
                print("account found ")
                break
            else:
                print ("enter vaild Receiver ac num")
        

        while True:
            Transfer_Amount = input("Give me amount you want to Transfer ")
            if re.search(r"^[0-9]+$", Transfer_Amount):
                Transfer_Amount = int (Transfer_Amount)

                if Transfer_Amount > Accounts.Account_list[senders_ac]["Balance"]:
                    print(f"Don't have enough balance \n {Accounts.Account_list[senders_ac]['Balance']} is your current balance ")
                    break

                if Transfer_Amount > 0:
                    Accounts.Account_list[senders_ac]['Balance'] -= Transfer_Amount
                    print (f"your current balance is {Accounts.Account_list[senders_ac]['Balance']}")

                    Accounts.Account_list[senders_ac]["Transactions"].append({
                        "Type" : f"Money sent to { Accounts.Account_list[Receiver_ac]['Name'] }" ,
                        "Amount" : Transfer_Amount })

                    Accounts.Account_list[Receiver_ac]['Balance'] += Transfer_Amount

                    Accounts.Account_list[Receiver_ac]["Transactions"].append({
                        "Type" : f"Money received from { Accounts.Account_list[senders_ac]['Name']}",
                        "Amount" : Transfer_Amount 
                        })
                            
                    break
            else: 
                print ("enter valid amount ")


    def delete_acc():
        ac_no , validator = Banking.validator()
        while True:
            Response = input ("Type 'DELETE' to delete your account")
            if Response == 'DELETE':
                del Accounts.Account_list [ac_no]
                print ("Account deleted successfully")
                break
            else:
                print("match exact 'DELETE' ")

    def ac_detail():
        ac_no , validator = Banking.validator()
        account_details = Accounts.Account_list[ac_no]
        print(f"Account Number : {ac_no}")
        print(f"Name           : {account_details['Name']}")
        print(f"Mobile         : {account_details['Mobile_no']}")
        print(f"Balance        : {account_details['Balance']}")




class Menu(Banking , Accounts):


    def menu():
        while True:
            print(
                "Give your input as numbers:",
                "1. Create account",
                "2. Deposit money",
                "3. Withdraw money",
                "4. Check balance",
                "5. Transaction history",
                "6. Account details",
                "7. Change pin",
                "8. Transfer money",
                "9. Delete account",
                "10.Exit",
                sep="\n"
            )

            while True:
                try:
                    Task = int(input ("Give us your input "))
                except ValueError:
                    print ("enter a number ")
                else:
                    break
                



            if Task == 1:
                Accounts.create_account()



            elif Task == 2:
                Banking.deposit_money()


            elif Task == 3:
                Banking.Withdraw_money()


            elif Task == 4:
                Banking.Balance()


            elif Task == 5:
                Banking.Transaction_history()


            elif Task == 6:
                Banking.ac_detail()


            elif Task == 7:
                Banking.Change_pin()


            elif Task == 8:
                Banking.transfer_money()


            elif Task == 9:
                Banking.delete_acc()


            elif Task == 10:
                break

            else:
                print("invalid input!!!! ")


Bank = Menu.menu()