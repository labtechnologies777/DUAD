from data import DataManager
from windows import WindowManager

class FinanceApp:
    def __init__(self):
        file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/text.csv"
        self.data_manager = DataManager(file)
        self.window_manager = WindowManager()
        self.expense_list = []
        self.category_list = []
        self.expenses_type = ["credit", "debit"]
        

    def run_category_window(self):
        cat_win = self.window_manager.make_category_window()
        event, values = cat_win.read(close=True)
        
        if event == "Add" and values['-CAT-']:
            new_category = values['-CAT-']
            if new_category.lower() not in self.category_list:
                self.category_list.append(new_category)

    def run_transaction_window(self):
        while True:
            trans_win = self.window_manager.make_transaction_window(self.category_list, self.expenses_type)
            event, values = trans_win.read(close=True)
            
            if event == "Add Category":
                self.run_category_window()
                continue
                
            if event == self.window_manager.close_window() or event == "Exit":
                break
                
            if event == "Done":
                if not values["-CATEGORY-"]:
                    self.window_manager.popup_error("Error: Must add a category!")
                    continue
                
                if "Choose Date" in values:
                    del values["Choose Date"]

                self.expense_list.append(values)
                self.data_manager.save_data(self.expense_list,self.data_manager.filename)
                break

    def run_table_window(self):
        if not self.expense_list:
            self.window_manager.popup_error("ERROR: No data to display")
            return

        table_win = self.window_manager.make_table_window(self.expense_list)
        if table_win:
            table_win.read(close=True)

    def main_loop(self):
        self.data_manager.load_data(self.expense_list,self.category_list)
        while True:
            start_win = self.window_manager.make_start_window()
            event, values = start_win.read(close=True)

            if event == self.window_manager.close_window() or event == "Exit":
                break

            elif event == "Add":
                self.run_transaction_window()

            elif event == "Table":
                self.run_table_window()

            elif event == "Export to CSV":
                folder = self.window_manager.export_csv()
                file = "data.csv"
                full_path = f"{folder}/{file}"
                if folder == None:
                    continue
                else:
                    self.data_manager.save_data(self.expense_list,full_path)

if __name__ == "__main__":
    app = FinanceApp()
    app.main_loop()
