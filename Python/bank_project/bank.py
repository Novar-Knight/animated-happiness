#Bank will handle all
#Required items
#Deposit
#Withdrwal
#Open Account

from account import create_account,get_account_by_id_no,update_account
from decorators import log
from time import  sleep
from datetime import datetime


@log
def new_account(trials=0):
    
    if trials>3:
        print("Maximum retry met exiting.")
        return None
    
    print("Welcome to soft bank")
    print("Create Account")
    id_no=input("Enter id no:")
    account=get_account_by_id_no(id_no)
    if account:
        seconds=trials+2
        print(f"Id number already in use. Try again in  {seconds} s")
        sleep(seconds)
        new_account(trials=trials+1)
        return
    
    name=input("Enter name:")
    password=input("Enter your password:")
    account=create_account(name=name,password=password,id_no=id_no)
    
    if account:
        print(f"Welcome {account["name"]}. Account created")
    return account

@log    
def deposit(account):
    transaction_history=account["transaction_history"]
    balance=account["balance"]
    print(f"Account Balance is {balance}")
    amount=float(input("Deposit Amount"))

    #bug try except: enters a string.
    #Additional chek if amount >0
    if amount<0:
        print("To deposit enter amount greater than 0")
        return None

    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_balance=balance+amount
    transaction_history.append({"transaction_type":"Deposit","timestamp":timestamp,"amount":amount,"balance":balance,"new_balance":new_balance})
    account["balance"]=new_balance
    account["transaction_history"]=transaction_history
    
    account_update=update_account(account=account)
    return account_update

@log    
def withdrwal(account):
    transaction_history=account["transaction_history"]
    balance=account["balance"]
    print(f"Account Balance is {balance}")
    amount=float(input("Withdrwal Amount"))

    #bug try except: enters a string.
    #Additional chek if amount >0
    if amount<0:
        print("To witdwal enter amount greater than 0")
        return None

    if amount>balance:
        print(f"Cant withdraw more than the {balance}")
        return None

    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_balance=balance-amount
    transaction_history.append({"transaction_type":"Withdrwal",
                                "timestamp":timestamp,
                                "amount":amount,
                                "balance":balance,
                                "new_balance":new_balance})
    account["balance"]=new_balance
    account["transaction_history"]=transaction_history
    
    account_update=update_account(account=account)
    return account_update

# account=get_account_by_id_no("8822122")
# withdrwal(account)