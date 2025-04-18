from actions import add_students,top_user_grades,overall_grade,display_student_info,delete_student
from data import write_csv_file,read_csv_file

def menu():
    student_list = []
    flag = True
    while flag:
        try:
            menu = input("""
        (1) Add students.
        (2) Find top students.
        (3) Display student information.
        (4) Student overall grades.
        (5) Import student list from file.
        (6) Save changes.
        (7) Delete a student.
        To exit type 'exit':
    Your selection is: """)
            if menu == "exit":
                flag = False
            elif menu.strip() == "":
                print("ERROR: Need to enter a value, can't be empty")
            elif int(menu) < 1 or int(menu) > 8:
                    print("ERROR: Invalid number, enter a valid number from 1 to 8")
            elif int(menu) == 1:
                add_students(student_list)
            elif int(menu) == 2:
                top_user_grades(student_list)
            elif int(menu) == 3:
                display_student_info(student_list)
            elif int(menu) == 4:
                overall_grade(student_list)
            elif int(menu) == 5:
                read_csv_file("/Users/labtechnologies/Desktop/Progra/semana_11/list.csv", student_list)
            elif int(menu) == 6:
                write_csv_file(student_list)
            elif int(menu) == 7:
                delete_student(student_list)
        except ValueError:
            print("ERROR: Enter numbers not letters")

