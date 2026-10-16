# Student Manager - OOP version
# Uses only: class, self, __init__, methods, return, dictionary, if, whilepPPP


class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, sid, name, grade):
        if sid in self.students:
            return "This ID already exists"
        self.students[sid] = Student(sid, name, grade)
        return "Student added"

    def edit_student(self, sid, name, grade):
        if sid not in self.students:
            return "Student not found"
        self.students[sid].name = name
        self.students[sid].grade = grade
        return "Student updated"

    def delete_student(self, sid):
        if sid not in self.students:
            return "Student not found"
        del self.students[sid]
        return "Student deleted"

    def show_all(self):
        if len(self.students) == 0:
            print("No students yet")
        for sid in self.students:
            s = self.students[sid]
            print("ID:", s.sid, "| Name:", s.name, "| Quiz Grade:", s.grade)


manager = StudentManager()
choice = ""

while choice != "5":
    print("")
    print("1. Add   2. Edit   3. Delete   4. Show all   5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        grade = int(input("Quiz Grade: "))
        print(manager.add_student(sid, name, grade))
    elif choice == "2":
        sid = input("ID of the student to edit: ")
        name = input("New name: ")
        grade = int(input("New quiz grade: "))
        print(manager.edit_student(sid, name, grade))
    elif choice == "3":
        sid = input("ID of the student to delete: ")
        print(manager.delete_student(sid))
    elif choice == "4":
        manager.show_all()
    elif choice == "5":
        print("Goodbye")
    else:
        print("Wrong choice")
        
# Student Manager - Functions version (no OOP)
# Uses only: def, return, dictionary, if, while

students = {}


def add_student(sid, name, grade):
    if sid in students:
        return "This ID already exists"
    students[sid] = [name, grade]
    return "Student added"


def edit_student(sid, name, grade):
    if sid not in students:
        return "Student not found"
    students[sid] = [name, grade]
    return "Student updated"


def delete_student(sid):
    if sid not in students:
        return "Student not found"
    del students[sid]
    return "Student deleted"


def show_all():
    if len(students) == 0:
        print("No students yet")
    for sid in students:
        print("ID:", sid, "| Name:", students[sid][0], "| Quiz Grade:", students[sid][1])


choice = ""

while choice != "5":
    print("")
    print("1. Add   2. Edit   3. Delete   4. Show all   5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        grade = int(input("Quiz Grade: "))
        print(add_student(sid, name, grade))
    elif choice == "2":
        sid = input("ID of the student to edit: ")
        name = input("New name: ")
        grade = int(input("New quiz grade: "))
        print(edit_student(sid, name, grade))
    elif choice == "3":
        sid = input("ID of the student to delete: ")
        print(delete_student(sid))
    elif choice == "4":
        show_all()
    elif choice == "5":
        print("Goodbye")
    else:
        print("Wrong choice")