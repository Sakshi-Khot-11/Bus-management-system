import main
import bus
import student
import teacher
import payment

def issue_fee():
    print("Issuing fee...")



def add_bus():
    print("adding bus")
    
def delete_bus():
    print("delete bus")



def admin_session():
    while True: 
        print("      Menu:")
        print("1. Register new student")
        print("2. Register teacher")  
        print("3. Delete student")  
        print("4. Delete teacher")  
        print("5. View bus\n6. add bus \n7. delete bus ") 
        print("8. Logout")
        user_option = input("Option: ")

        if user_option == "1":
            print("\nRegistering student")
            username = input("Username: ")
            password = input("Password: ")
            
            print(f"{username} has been registered as succesfully!!!.") 
        
        if user_option == "2":
            print("\nRegistering student")
            username = input("Username: ")
            password = input("Password: ")
            department = input("Department: ")
            print(f"{username} has been registered as succesfully!!!.") 

        if user_option == "3":
            print("\ndelete  student")
            username = input("PRN: ")
            password = input("Password: ")
            print(f"{username} has been deleted as succesfully!!!.") 

        if user_option == "4":
            print("\ndelete  teacher")
            username = input("username: ")
            password = input("Password: ")
            department = input("Department: ")
            print(f"{username} has been deleted as succesfully!!!.")

        if user_option == "5":
           bus.bus_detail()


        if user_option == "6":
            add_bus()


        if user_option == "7":
           delete_bus()

        if user_option == "8":
           print("Logging out...")
           break

        else:
          print("Please select a correct option.")
        

def admin():
    print("\nAdmin login")
    username = input("Username: ")
    password = input("Password: ")
    admin_choice()  
    if username == "admin":
        if password == "pass@123":
            admin_session()
        else:
            print("Incorrect password")
    else:
        print("Username not recognized")

