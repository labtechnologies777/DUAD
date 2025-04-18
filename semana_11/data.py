import csv 
from actions import Student

def write_csv_file(student_list):
    filepath = "/Users/labtechnologies/Desktop/Progra/semana_11/list.csv"
    file_headers = [
        "student_name",
        "student_section",
        "student_spanish_grade",
        "student_english_grade",
        "student_science_grade",
        "student_history_grade",
        "student_average",
    ]      

    with open(filepath, 'w', encoding='utf-8', newline='') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=file_headers)
        writer.writeheader()
        for student in student_list:
            writer.writerow(student.__dict__)
        print("\n")
        print("***************************")
        print("   Changes saved to file   ")
        print("***************************")
        return student_list


def read_csv_file(filepath, student_list):
        try:
            with open(filepath, 'r') as read_file:
                for line in csv.DictReader(read_file):    
                        student_list.append(Student(**line))
            print(student_list)
            print("\n")
            print("*" * 20)
            print("Data imported successfully!")
            print("*" * 20)
            return student_list
        except FileNotFoundError:
             print("WARNING! No file found, you must add students and save subsequent changes.")