students = []

# Add Student
def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    department = input("Enter Department: ")

    student = {
        "name": name,
        "roll": roll,
        "department": department
    }

    students.append(student)
    print("Student Added Successfully!\n")


# View Students
def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        print("\nStudent List:")
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Department: {s['department']}")
        print()


# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    for s in students:
        if s["roll"] == roll:
            print("Student Found:")
            print(s)
            return

    print("Student Not Found.\n")


# Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["department"] = input("Enter New Department: ")
            print("Student Updated Successfully!\n")
            return

    print("Student Not Found.\n")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found.\n")


# Main Menu
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!\n")