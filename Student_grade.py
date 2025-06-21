class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return 'A+'
        elif self.marks >= 75:
            return 'A'
        elif self.marks >= 60:
            return 'B'
        elif self.marks >= 50:
            return 'C'
        else:
            return 'F'

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}, Grade: {self.get_grade()}")


def add_student(students):
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks (out of 100): "))
    student = Student(roll, name, marks)
    students.append(student)
    print("1Student added successfully!\n")


def show_all_students(students):
    print("\n--- Student List ---")
    for student in students:
        student.display()


def search_student(students):
    roll = int(input("Enter Roll Number to search: "))
    for student in students:
        if student.roll == roll:
            student.display()
            return
    print("Student not found.\n")


def main():
    students = []
    while True:
        print("\n Student Management Menu")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            show_all_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
