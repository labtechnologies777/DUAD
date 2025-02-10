def add_students(student_list):
        student_info = {}
        student_name = input("Enter a student's name: ")
        student_section = input("Enter the student's section: ")
        student_info["Name"] = student_name
        student_info["Section"] = student_section
        print("Enter a Spanish grade:")
        student_info["Spanish"] = enter_student_grades()
        print("Enter English grade:")
        student_info["English"] = enter_student_grades()
        print("Enter a Science grade:")
        student_info["Science"] = enter_student_grades()
        print("Enter History grade:")
        student_info["History"] = enter_student_grades()
        average = (student_info.get("Spanish") + student_info.get("English") + student_info.get("Science") + student_info.get("History") ) / 4
        student_info["Average"] = average
        student_list.append(student_info)
        return student_list


def enter_student_grades():
    while True:
            try:
                grade = input()
                if grade.strip() == "":
                    print("Need to enter a value, can't be empty")
                elif int(grade) < 0 or int(grade) > 100:
                    print("Invalid number, enter a valid number from 0 to 100")
                else:
                    grade = int(grade)
                    return grade
            except ValueError:
                print("Enter numbers not letters")


def display_student_info(student_list):
    print("This is the info you just entered: \n")
    print("----------------------------------")
    for key in student_list:
        print("----------------------------------")
        print(f"Name: {key.get("Name")}")
        print(f"Section: {key.get("Section")}")
        print(f"Spanish: {key.get("Spanish")}")
        print(f"English: {key.get("English")}")
        print(f"Science: {key.get("Science")}")
        print(f"History: {key.get("History")}")
        print(f"Average: {key.get("Average")}")
    print("----------------------------------")


def edit_student_info(student_list):
    student_name = input("Which student would you like to edit: ")
    signature = input("Enter the signature to correct: ")
    signature = signature.title()
    grade = int(input("Enter the new grade: "))
    for index in range(len(student_list)):
        student = student_list[index]
        if student["Name"] == student_name:
            student[signature] = grade
            student["Average"] = float((student.get("Spanish") + student.get("English") + student.get("Science") + student.get("History"))) / 4
            return student_list


def top_user_grades(student_list):
    name_avg_dict = {}
    for dic in student_list:
        name = dic.get("Name")
        average = float(dic.get("Average"))
        name_avg_dict[name] = average
        top_score_list = sorted(name_avg_dict.values(), reverse=True)
        top_score_dic = {}
        for sortedKey in top_score_list[:3]:
            for key, value in name_avg_dict.items():
                if value == sortedKey:
                    top_score_dic[key]=value
    print("***************************")
    print("*** The best scores are ***")
    print("***************************")
    for student, grade in top_score_dic.items():
        print(f"{student} {grade}")
    print("---------------------------")


def overall_grade(student_list):
    overall_average_list = []
    for dic in student_list:
        student_average = float(dic.get("Average"))
        overall_average_list.append(student_average)
        average = sum(overall_average_list) / len(overall_average_list)
    print(f"The average is {average}")
    

def delete_student(student_list):
    delete_student_name = input("Enter the student name you want to remove: ")
    counter = 0
    index = 0
    while counter < len(student_list):
            if student_list[index]["Name"] == delete_student_name:
                del student_list[index]
            counter = counter + 1
            index = index + 1
    return student_list