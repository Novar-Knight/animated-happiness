from decorators import log
from time import sleep
from account import get_account_by_id_no,update_account

#think about how we deactivate an account
#Try implementing that
## another way->Instead of recussion: for or while

@log
def login(attempts=0,account_attempts=1,account=None):
   
   if attempts>=3 and account:
      print("Maximum attempts reached")
      print("Account locked.Contact Customer service")
      account["is_locked"]=True
      update_account(account)

      return None
   
   if not account:
      id_no=input("Enter your id no:")
      account=get_account_by_id_no(id_no)
   
   
   #Denial of service
   if not account:
      seconds=account_attempts
      print(f"... Waiting  for next login {seconds} seconds")
      sleep(seconds)
      login(attempts=attempts,account_attempts=account_attempts+2)
      #DOS-> Denial service of service
      return None
   

   if account.get("is_locked"):
      print("Account locked. Contanct service center")
      return
   

   print("Bank login process")
   print("Attempt no",attempts)
   password=input("Enter account password:")

   # if "is_locked" in account and account["is_locked"]==True:
   #    print("Account locked. Contanct service center")
   #    return

   
   if account["password"] != password:
      print("Invalid Password or account")
      new_attempts=attempts+1
      login(attempts=new_attempts,account=account)
      return

   print("---------Welcome----------")
   print(f"{account["name"]}") 
   print("---------Welcome----------")

   return account 
      
#login()

