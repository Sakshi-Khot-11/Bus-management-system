import main
import bus
import admin
import teacher
import student

def  card_detail():
    

    p=input("Enter card number:")
    PIN = input("Enter PIN: ")
    if p=="123456789012":
      if PIN=="1234":
         print("payment successful")    
      else:
         print("please enter correct details.")
    
    

def  cash_fee():
      print("thanku for succesfull payment") 
def  bank_details(): 
      print("Name of the bank:SBI")
      print("Bank account numberL:00002536975")
      print("IFSC Code:SBIN0000384")
      print("Thanku your amount is received")
      
def payment():
        print("welcome")
        print("Menu")
        ch = input("1.card\n2.cash\n3.bank account\nPlease choose an option: ")
            
        if ch == "1":
            card_detail()
        elif ch == "2":
            cash_fee()
        elif ch == "3":
            bank_details()
        else:
            print("Please select a correct option.")

       