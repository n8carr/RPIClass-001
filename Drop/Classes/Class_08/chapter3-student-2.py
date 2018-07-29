student_data= [["Luke", {"Math": 82, "English": 78, "Science": 72}],
            ["Mary", {"Math": 79, "Art": 81, "History": 90, "Geography": 65}],
            ["Paul", {"English": 66, "History": 48}]]

grades = ((0, "FAIL"),(60, "D"),(70,"C"),(80, "B"), (90,"A"), (101, "CHEAT!"))


class Student():
    def __init__(self,name, grades):
        self.name = name
        self.grades = grades

    def print_report_card(self):
        print("Report card for student ", self.name)
        for subject, grade in self.grades.items():
            for i in grades:
                if grade < i[0]:
                    print(subject, " : ", prev_grade)
                    break
                prev_grade = i[1]

    def add_grade(self, subject, grade):
        if subject in self.grades.keys():
            print(student_name, " already has a grade for ", subject)
            user_input = input("Overwrite Y/N? ")
            if user_input == "Y" or user_input == "y":
                self.grades[subject] = grade
                return "Student's grade updated"
            else:
                return "Student's grade not updated"
        else:
            self.grades[subject] = grade
            return "Student's grade added"

class Students():
    def __init__(self, all_students):
        self.students = []
        for student, grade in all_students:
            self.add_student(student, grade)

    def add_student(self,student_name, grades = {}):
        if self.exists(student_name):
            return "Student already in database"
        else:
            self.students.append(Student(student_name, grades))
            return "Student added"

    def print_report_cards(self, student_name = None):
        for student in self.students:
            if student_name == None or student_name == student.name:
                student.print_report_card()
            

    def exists(self, student_name):
        for student in self.students:
            if student_name == student.name:
                return True
        return False

    def add_grade(self, student_name, subject, grade):
        for student in self.students:
            if student_name == student.name:
                return student.add_grade(subject, grade)
        return "Student not found"

students = Students(student_data)
print(students.students)
while True:
    print("Welcome the the Raspberry Pi student database")
    print("What can I help you with?")
    print("Enter 1 to view all report cards")
    print("Enter 2 to view the report card for a student")
    print("Enter 3 to add a student")
    print("Enter 4 to add a grade to a student")
    print("Enter 5 to exit")
    
    try:
        user_choice = int(input("Choice: "))
    except ValueError:
        print("That's not a number I recognise")
        user_choice = 0
        
    if user_choice == 1:
        students.print_report_cards()
    elif user_choice == 2:
        enter_student = input("Which student? ")
        students.print_report_cards(enter_student)
    elif user_choice == 3:
        enter_student = input("Student name? ")
        print(students.add_student(enter_student))
    elif user_choice ==4:
        enter_student = input("Student name? ")
        enter_subject = input("Subject? ")
        num_error = True
        while num_error:
            num_error = False
            try:
                enter_grade = int(input("Grade? "))
            except ValueError:
                print("I don't recognise that as a number")
                num_error = True
        print(students.add_grade(enter_student, enter_subject, enter_grade))
    elif user_choice == 5:
        break
    else:
        print("Unknown choice")

    input("Press enter to continue")

print("Goodbye and thank you for using the Raspberry Pi Student database")
