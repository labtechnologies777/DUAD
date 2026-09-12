import FreeSimpleGUI as sg

class WindowManager:
    def __init__(self):
        sg.theme("Light Blue 1")

    def make_start_window(self):
        layout = [
            [sg.Text("Welcome to Finance Manager", font=("Helvetica", 18))],
            [sg.Text("Please add transaction information")],
            [
                sg.Button("Add"),
                sg.Button("Export to CSV", button_color="#5c715e"), 
                sg.Button("Table", button_color="#4D4D4D"),
                sg.Button("Exit", button_color="red")
            ],
        ]
        return sg.Window("Finance Manager", layout)

    def make_category_window(self):
        layout = [
            [sg.Text("Add a category"), sg.Input("", key='-CAT-')],
            [sg.Button("Add"), sg.Button("Cancel")],
        ]
        return sg.Window("Category", layout)

    def make_transaction_window(self, category_list, expenses_type):
        layout = [
            [sg.Text("Category"), sg.Combo(category_list, key='-CATEGORY-', readonly=True), sg.Button("Add Category")],
            [sg.Text("Type of expense:"), sg.Combo(expenses_type, key='-TYPE-', readonly=True)],
            [sg.Text("Add transaction description"), sg.Input("", key='-DESCRIPTION-')],
            [sg.Text("Amount"), sg.Input("", key='-AMOUNT-')],
            [sg.Text("Date"), sg.Input("", key='-DATE-', size=(20, 1)), sg.CalendarButton("Choose Date", target="-DATE-", format="%Y-%m-%d")],
            [sg.Button("Done"), sg.Button("Exit")],
        ]
        return sg.Window("Transaction", layout)

    def make_table_window(self, expense_list):
        headers = ("-CATEGORY-", "-TYPE-", "-DESCRIPTION-", "-AMOUNT-", "-DATE-")
        data_list = [list(dic.values()) for dic in expense_list]  
        
        layout = [
            [sg.Text("Transaction table")],
            [sg.Table(values=data_list, 
                      headings=headers, 
                      display_row_numbers=False,
                      auto_size_columns=True,
                      justification='center',
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button("Exit")],
        ]
        return sg.Window("Transaction table", layout)
    
    def export_csv(self):
        folder = sg.popup_get_folder("Choose where to save the CSV file")
        return folder
    
    def popup_error(self,message):
        popup = sg.popup_error(message)
        return popup
    
    def close_window(self):
        close = sg.WIN_CLOSED
        return close

#