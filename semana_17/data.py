import csv
import os

class DataManager:
    def __init__(self,filename):
        self.filename = filename
        self.file_headers = ("-CATEGORY-", "-TYPE-", "-DESCRIPTION-", "-AMOUNT-", "-DATE-")

    def save_data(self, expense_list, file_path):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8', newline='') as write_file:
            writer = csv.DictWriter(write_file, fieldnames=self.file_headers)
            writer.writeheader()
            writer.writerows(expense_list)

    def load_data(self,expense_list,category_list):
        if not os.path.exists(self.filename):
            return expense_list
            
        with open(self.filename, "r", encoding='utf-8') as read_file:
            for line in csv.DictReader(read_file):
                expense_list.append(line)
                cat_value = line.get("-CATEGORY-").lower()
                if cat_value not in category_list:
                    category_list.append(cat_value)
        return expense_list