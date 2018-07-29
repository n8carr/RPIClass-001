students = [["Luke", {"Math": 82, "English": 78, "Science": 72}],
            ["Mary", {"Math": 79, "Art": 81, "History": 90, "Geography": 65}],
            ["Paul", {"English": 66, "History": 48}]]

grades = ((0, "FAIL"),(60, "D"),(70,"C"),(80, "B"), (90,"A"), (101, "CHEAT!"))

def print_report_card(report_student = None):
    for student in students:
        if (student[0] == report_student) or (report_student == None):
            print("Report card for student ", student[0])            
            for subject, grade in student[1].items():
                for grade in grades:
                    if grade < grade[0]:
                        print(subject, " : ", prev_grade)
                        break
                    prev_grade = grade[1]
    


def add_student(student_name):
    global students
    for student in students:
        if student[0] == student_name:
            return "Student already in database"
    students.append([student_name, {}])
    return "Student added sucessfully"

def add_grade(student_name, subject, grade):
    global students
    for student in students:
        if student[0] == student_name:
            if subject in student[1].keys():
                print(student_name, " already has a grade for ", subject)
                user_input = input("Overwrite Y/N? ")
                if user_input == "Y" or user_input == "y":
                    student[1][subject] = grade
                    return "Student's grade updated"
                else:
                    return "Student's grade not updated"
            else:
                student[1][subject] = grade
                return "Student's grade added"
    return "Student not found"

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
        print_report_card()
    elif user_choice == 2:
        enter_student = input("Which student? ")
        print_report_card(enter_student)
    elif user_choice == 3:
        enter_student = input("Student name? ")
        print(add_student(enter_student))
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
        print(add_grade(enter_student, enter_subject, enter_grade))
    elif user_choice == 5:
        break
    else:
        print("Unknown choice")
    print("")
    input("Press enter to continue")
    print("")
print("Goodbye and thank you for using the Raspberry Pi student database")
