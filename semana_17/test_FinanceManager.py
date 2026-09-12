import os
import csv
import pytest
from data import DataManager


# # --- TEST 1: Test saving data ---

def test_save_data():
    temp_file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/test_saving_data.csv"
    manager = DataManager(temp_file)
    
    sample_data = [
        {
            "-CATEGORY-": "Food",
            "-TYPE-": "debit",
            "-DESCRIPTION-": "Groceries",
            "-AMOUNT-": "45.00",
            "-DATE-": "2026-08-20"
        }
    ]

    manager.save_data(sample_data,temp_file)

    # Assert: Check if the file was created and is not empty
    assert os.path.exists(temp_file)
    assert os.path.getsize(temp_file) > 0


# --- TEST 2: Test loading data back ---

def test_load_data():
    temp_file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/test_load_data.csv"
    manager = DataManager(temp_file)
    
    sample_data = [
        {
            "-CATEGORY-": "Utilities",
            "-TYPE-": "credit",
            "-DESCRIPTION-": "Electric Bill",
            "-AMOUNT-": "120.00",
            "-DATE-": "2026-08-20"
        }
    ]

    temp_expense_list = []
    temp_category_list = []

    # Save the data first
    manager.save_data(sample_data,temp_file)

    # Load the data back
    loaded_data = manager.load_data(temp_expense_list,temp_category_list)

    # Check if the loaded data matches what we saved
    assert len(loaded_data) == 1
    assert loaded_data[0]["-CATEGORY-"] == "Utilities"
    assert loaded_data[0]["-AMOUNT-"] == "120.00"


# --- TEST 3: Loading a non-existent file returns an empty list without crashing.  ---

def test_load_data_when_file_does_not_exist():
    non_existent_file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/test_does_not_exist.csv"
    manager = DataManager(non_existent_file)
    temp_expense_list = []
    temp_category_list = []

    # Try to load from it
    result = manager.load_data(temp_expense_list,temp_category_list)

    # Return an empty list []
    assert result == []


# --- TEST 4: Testing cleaning extra keys ---

def test_save_data_filters_extra_gui_keys():
    temp_file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/test_extra_keys.csv"
    manager = DataManager(temp_file)

    dirty_data = [
        {
            "-CATEGORY-": "Food",
            "-TYPE-": "debit",
            "-DESCRIPTION-": "Lunch",
            "-AMOUNT-": "15.00",
            "-DATE-": "2026-09-03",
            "Choose Date": "2026-09-03"  # Unwanted key from GUI
        }
    ]

    with pytest.raises(ValueError) as error:
        manager.save_data(dirty_data,temp_file)


# # --- TEST 5: Passing a non-dictionary inside the list causes an AttributeError

def test_save_data_raises_error_on_invalid_item_type():
    
    temp_file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/test_invalid_type.csv"
    data_mgr = DataManager(temp_file)

    # List containing a string instead of a dictionary
    bad_expense_list = ["Not a dictionary!"]

    # Expect AttributeError
    with pytest.raises(AttributeError):
        data_mgr.save_data(bad_expense_list,temp_file)

# --- TEST 6: Checks that multiple expense records are saved and retrieved in order.

def test_save_and_load_multiple_transactions():
    temp_file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/test_multiple_transactions.csv"
    manager = DataManager(temp_file)

    sample_expenses = [
        {"-CATEGORY-": "Food", "-TYPE-": "debit", "-DESCRIPTION-": "Groceries", "-AMOUNT-": "50", "-DATE-": "2026-09-01"},
        {"-CATEGORY-": "Transport", "-TYPE-": "debit", "-DESCRIPTION-": "Gas", "-AMOUNT-": "30", "-DATE-": "2026-09-02"},
        {"-CATEGORY-": "Salary", "-TYPE-": "credit", "-DESCRIPTION-": "Paycheck", "-AMOUNT-": "1000", "-DATE-": "2026-09-03"}
    ]

    temp_expense_list = []
    temp_category_list = []

    # Save all 3 items
    manager.save_data(sample_expenses,temp_file)
    
    # Load them back
    loaded_expenses = manager.load_data(temp_expense_list,temp_category_list)

    assert len(loaded_expenses) == 3
    assert loaded_expenses[0]["-DESCRIPTION-"] == "Groceries"
    assert loaded_expenses[2]["-AMOUNT-"] == "1000"


#-- TEST 7 Make sure filename name is correct. ---

def test_data_manager_default_filename():

    file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/text.csv"
    data_mgr = DataManager(file)

    # Verify default file path string ends with text.csv
    assert data_mgr.filename.endswith("text.csv")

# -- TEST 8 Checks the number of file headers. ---

def test_data_manager_file_headers_count():    

    file = "/Users/labtechnologies/Desktop/Progra/vcs_repo/DUAD/semana_17/text.csv"
    manager = DataManager(file)

    # verify the header count is 5
    assert len(manager.file_headers) == 5