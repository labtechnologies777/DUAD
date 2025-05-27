class Student:
    def __init__(self,student_name,student_section,student_spanish_grade,student_english_grade,student_science_grade,student_history_grade,student_average):
        self.student_name = student_name
        self.student_section = student_section
        self.student_spanish_grade = student_spanish_grade
        self.student_english_grade = student_english_grade
        self.student_science_grade = student_science_grade
        self.student_history_grade = student_history_grade
        self.student_average = student_average


    def __repr__(self):
        return f"Student(student_name={self.student_name}, student_section={self.student_section}, student_spanish_grade={self.student_spanish_grade}, student_english_grade={self.student_english_grade}, student_science_grade={self.student_science_grade}, student_history_grade={self.student_history_grade}, student_average={self.student_average})"


def add_students(student_list):
    student_name = input("Enter a student's name: ")
    student_section = input("Enter the student's section: ")
    student_spanish_grade = int(input("Enter the student's Spanish grade: "))
    student_english_grade = int(input("Enter the student's English grade: "))
    student_science_grade = int(input("Enter the student's Science grade: "))
    student_history_grade = int(input("Enter the student's History grade: "))
    student_average = (student_spanish_grade + student_english_grade + student_science_grade + student_history_grade) / 4
    student_list.append(Student(
        student_name,
        student_section,
        student_spanish_grade,
        student_english_grade,
        student_science_grade,
        student_history_grade,
        student_average,))
    return student_list


def display_student_info(student_list):
    print("This is the info you just entered: \n")
    print("-" * 20)
    for student in student_list:
        print("-" * 20)
        print(f"Name: {student.student_name}")
        print(f"Section: {student.student_section}")
        print(f"Spanish: {student.student_section}")
        print(f"English: {student.student_spanish_grade}")
        print(f"Science: {student.student_english_grade}")
        print(f"History: {student.student_science_grade}")
        print(f"Average: {student.student_average}")
    print("-" * 20)


def top_user_grades(student_list):
    sorted_list = sorted(student_list, key=lambda x: x.student_average, reverse=True)
    print("*" * 20)
    print("*** The best scores are ***")
    for student in sorted_list[:3]:
        print(student.student_name, student.student_average)
    print("*" * 20)


def overall_grade(student_list):
    overall_average_list = []
    for student in student_list:
        student_average = float(student.student_average)
        overall_average_list.append(student_average)
        average = sum(overall_average_list) / len(overall_average_list)
    print(f"The average is {average}")


def delete_student(student_list):
    delete_student_name = input("Enter the student name you want to remove: ")
    for student in student_list:
            if delete_student_name == student.student_name:
                student_list.remove(student)
    return student_list