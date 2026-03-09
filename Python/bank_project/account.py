import json
import os,sys
from decorators import log
#Will handle account logic
#Eg getting,upating accounts
#create an account
#creating account number for your
#-------> 
#------->
#Probles verify if an account exits
#Save the created accoun in the accounts filder

@log
def get_account_by_id_no(id_no):
    filename=f"accounts/{id_no}.json"

    if not os.path.exists(filename):
        #print(f"Account with idno {id_no} doe   s not exist")
        return None
    
    with open(filename,"r") as file:
        account=json.load(file)
        #print(account)
    return account

@log
def update_account(account):
    id_no=account["id_no"]
    filename=f"accounts/{id_no}.json"

    if not os.path.exists(filename):
        #print(f"Account with idno {id_no} doe   s not exist")
        return None
    
    with open(filename,"w") as file:
        json.dump(account,file,indent=4)
    return True


@log
def create_account(id_no,name,password):
   #Validations
    #id_no, name

    if  get_account_by_id_no(id_no):
        #print(f"Account with idno {id_no} already exists")
        return None

    account={
        "account_no":id_no,
        "id_no":id_no,
        "name":name,
        "transaction_history":[],
        "balance":0,
        "password":password
    }

    filename=f"accounts/{id_no}.json"

    with open(filename,"w") as file:
        json.dump(account,file)
    #print(f"Account created")
    return account

# create_account(id_no="223344",name="John",password="123456")
#create_account(id_no="8822122",name="Samson",password="9932342")
#get_account_by_id_no(id_no="2323344")
