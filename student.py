import main
import bus
import admin
import teacher
import payment


def student_choice():
    print("Your login is successful!")
    while True:
        print("           Menu")
        ch = input("1. View bus\n2. Check bus fee\n3.payment\n4.logout\nPlease choose an option: ")
        
        if ch == "1":
            bus.bus_detail()
        elif ch == "2":
            bus.bus_fee()
        elif ch == "3":
            payment.payment()
        elif ch == "4":
             print("logging out.......")
             break
            
        else:
            print("Please select a correct option.")


def student():
    print("Student login")
    
    PRN = input("Enter PRN: ")
    
    password = input("Enter the password: ")
    if PRN == "23UAD030":
        if password == "pass@123":
             student_choice()
        else:
            print("Incorrect password")
    else:
        
        print("PRN not recognized.")
        