from modules.add_student import add_student
from modules.view_students import view_students
from modules.update_student import update_student
from modules.delete_student import delete_student

def menu():
    while True:
        print("\n--- Student Data Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            grade = input("Enter grade: ")
            add_student(name, age, course, grade)
        elif choice == '2':
            view_students()
        elif choice == '3':
            sid = int(input("Enter student ID to update: "))
            grade = input("Enter new grade: ")
            update_student(sid, grade)
        elif choice == '4':
            sid = int(input("Enter student ID to delete: "))
            delete_student(sid)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
