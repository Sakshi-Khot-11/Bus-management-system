import main
import bus
import admin
import payment
import student


def teacher():
    print("teacher login")
    
    teacher_choice()
    username = input("Enter username: ")
    
    
    password = input("Enter the password: ")
    if username == "teacher":
        if password == "pass@123":
             teacher_choice()
        else:
            print("Incorrect password")
    else:
        
        print("user not recognized.")
           
    




def teacher_choice():
    print("Your login is successful!")
    while True:
        print("           Menu")
        ch = input("1. View bus\n2. Check bus fee\n3.logout\nPlease choose an option: ")
        
        if ch == "1":
            bus.bus_detail()
        if ch == "2":
            bus.bus_fee()
        if ch == "3":
            print("logging out.........")
            break
        else:
            print("Please select a correct option.")

