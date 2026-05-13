# ----- DATABASE -----
students = {}   # key: (first_name, last_name)
teachers = {}
homeroom_teachers = {}


# ----- CREATE USERS -----
def create_user():
    while True:
        print("\nCreate: student, teacher, homeroom teacher, end")
        choice = input("Choose type: ").lower()

        if choice == "student":
            first = input("First name: ")
            last = input("Last name: ")
            class_name = input("Class (e.g. 3C): ")

            key = (first, last)
            if key in students:
                print("Student already exists!")
            else:
                students[key] = {"class": class_name}
                print("Student created!")

        elif choice == "teacher":
            first = input("First name: ")
            last = input("Last name: ")
            subject = input("Subject: ")

            classes = []
            print("Enter classes (press Enter on empty line to stop):")
            while True:
                c = input()
                if c == "":
                    break
                classes.append(c)

            key = (first, last)
            if key in teachers:
                print("Teacher already exists!")
            else:
                teachers[key] = {
                    "subject": subject,
                    "classes": classes
                }
                print("Teacher created!")

        elif choice == "homeroom teacher":
            first = input("First name: ")
            last = input("Last name: ")
            class_name = input("Class: ")

            key = (first, last)
            if key in homeroom_teachers:
                print("Homeroom teacher already exists!")
            else:
                homeroom_teachers[key] = {"class": class_name}
                print("Homeroom teacher created!")

        elif choice == "end":
            break

        else:
            print("Invalid option!")


# ----- DELETE USERS -----
def delete_user():
    print("\nDelete: student, teacher, homeroom teacher")
    choice = input("Choose type: ").lower()

    first = input("First name: ")
    last = input("Last name: ")
    key = (first, last)

    if choice == "student":
        if key in students:
            del students[key]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == "teacher":
        if key in teachers:
            del teachers[key]
            print("Teacher deleted.")
        else:
            print("Teacher not found.")

    elif choice == "homeroom teacher":
        if key in homeroom_teachers:
            del homeroom_teachers[key]
            print("Homeroom teacher deleted.")
        else:
            print("Not found.")

    else:
        print("Invalid option.")


# ----- MANAGE USERS -----
def manage_user():
    while True:
        print("\nManage: class, student, teacher, homeroom teacher, end")
        choice = input("Choose option: ").lower()

        if choice == "class":
            class_name = input("Class: ")

            print("\nStudents:")
            found = False
            for (f, l), data in students.items():
                if data["class"] == class_name:
                    print("-", f, l)
                    found = True

            if not found:
                print("No students found.")

            print("\nHomeroom teacher:")
            homeroom_found = False
            for (f, l), data in homeroom_teachers.items():
                if data["class"] == class_name:
                    print("-", f, l)
                    homeroom_found = True

            if not homeroom_found:
                print("No homeroom teacher found.")

        elif choice == "student":
            first = input("First name: ")
            last = input("Last name: ")
            key = (first, last)

            if key in students:
                class_name = students[key]["class"]
                print("Class:", class_name)

                print("\nTeachers:")
                teacher_found = False
                for (f, l), data in teachers.items():
                    if class_name in data["classes"]:
                        print("-", f, l, "(", data["subject"], ")")
                        teacher_found = True

                if not teacher_found:
                    print("No teachers found for this class.")
            else:
                print("Student not found.")

        elif choice == "teacher":
            first = input("First name: ")
            last = input("Last name: ")
            key = (first, last)

            if key in teachers:
                print("Classes:")
                for c in teachers[key]["classes"]:
                    print("-", c)
            else:
                print("Teacher not found.")

        elif choice == "homeroom teacher":
            first = input("First name: ")
            last = input("Last name: ")
            key = (first, last)

            if key in homeroom_teachers:
                class_name = homeroom_teachers[key]["class"]
                print("Students in class", class_name)

                for (f, l), data in students.items():
                    if data["class"] == class_name:
                        print("-", f, l)
            else:
                print("Not found.")

        elif choice == "end":
            break

        else:
            print("Invalid option!")


# ----- MAIN PROGRAM -----
def main():
    while True:
        print("\nCommands: create, manage, end")
        command = input("Enter command: ").lower()

        if command == "create":
            create_user()

        elif command == "manage":
            manage_user()

        elif command == "end":
            print("Program ended.")
            break

        else:
            print("Invalid command!")


# RUN
main()