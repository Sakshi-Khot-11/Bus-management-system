import admin
import teacher
import student

def main_menu():
    while True:
        print("Welcome to DKTE")
        print("        Menu")
        print("1. Login as student")
        print("2. Login as admin")
        print("3. Login as teacher")
        print("4. Exit")
        
        user_option = input("Option: ")

        if user_option == "1":
            student.student()  # Ensure you have a function named `student_login` in the student module
        elif user_option == "2":
            admin.admin_session()  # Ensure you have a function named `admin` in the admin module
        elif user_option == "3":
            teacher.teacher_choice()  # Ensure you have a function named `teacher_login` in the teacher module
        elif user_option == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Not a valid option. Please try again.")

if __name__ == "__main__":
    main_menu()
