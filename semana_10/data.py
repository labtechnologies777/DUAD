import csv 

def write_csv_file(student_list):
    filepath = "/Users/labtechnologies/Desktop/Progra/semana_10/student_list.csv"
    file_headers = (
        "Name",
        "Section",
        "Spanish",
        "English",
        "Science",
        "History",
        "Average",
    )
    with open(filepath, 'w', encoding='utf-8') as write_file:
        writer = csv.DictWriter(write_file, file_headers)
        writer.writeheader()
        writer.writerows(student_list)
        print("\n")
        print("***************************")
        print("   Changes saved to file   ")
        print("***************************")


def read_csv_file(filepath, student_list):
        temp_student_list = []
        try:
            with open(filepath, 'r') as read_file:
                for line in csv.DictReader(read_file):
                    temp_student_list.append(line)
                for dic in temp_student_list:
                    num_keys = ['Spanish', 'English', 'Science', 'History', 'Average']
                    for key in num_keys:
                        if key in dic:
                            dic[key] = float(dic[key])
                    student_list.append(dic)
                print("\n")
                print("***************************")
                print("Data imported successfully!")
                print("***************************")
                return student_list
        except FileNotFoundError:
             print("WARNING! No file found, you must add students and save subsequent changes.")