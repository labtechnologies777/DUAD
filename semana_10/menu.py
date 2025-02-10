from actions import add_students,edit_student_info,top_user_grades,overall_grade,display_student_info,delete_student
from data import write_csv_file,read_csv_file

def menu():
    student_list = []
    flag = True
    while flag:
        try:
            menu = input("""
        (1) Add students.
        (2) Edit students.
        (3) Find top students.
        (4) Display student information.
        (5) Student overall grades.
        (6) Import student list from file.
        (7) Save changes.
        (8) Delete a student.
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
                edit_student_info(student_list)
            elif int(menu) == 3:
                top_user_grades(student_list)
            elif int(menu) == 4:
                display_student_info(student_list)
            elif int(menu) == 5:
                overall_grade(student_list)
            elif int(menu) == 6:
                read_csv_file("/Users/labtechnologies/Desktop/Progra/semana_10/student_list.csv", student_list)
            elif int(menu) == 7:
                write_csv_file(student_list)
            elif int(menu) == 8:
                delete_student(student_list)
        except ValueError:
            print("ERROR: Enter numbers not letters")

