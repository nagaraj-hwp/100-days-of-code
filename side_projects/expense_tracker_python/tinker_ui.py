# Creating a simple expense tracker using Python
from tkinter import *
from tkinter import messagebox
import json
import re
import calc_total
import file_update


def initiate_expense_calculation(expense_type):
    if expense_type == "d" or expense_type == "day":
        input_day = input("Enter date of the expense(YYYY−MM−DD) or just 'today' "
                          "(careful with your expense date input): ")
        expense_date = calc_total.get_expense_date(input_day)
        file_update.add_multiple_expense(expense_date)
        file_update.update_back_up_file()
        calc_total.calculate_day_expense(expense_date)
    elif expense_type == "single" or expense_type == "s":
        input_day = input("Enter which day it should be added to(careful with your expense date input): ")
        expense_date = calc_total.get_expense_date(input_day)
        file_update.add_single_expense(expense_date)
        file_update.update_back_up_file()
    else:
        print("Your choice is not valid or unavailable here")


def initiate_total_calculation():
    user_notification = """    Enter 'all' to calculate all expense added till date,
        Enter 'day' or 'd' to calculate single day expense,
        Enter 'month' or 'm' to calculate single month expense,
        Enter 'week' or 'w' to calculate last week expense,
        Enter 'last' or 'l' to calculate last few days expense,
        Enter 'dates' or 'dt' to calculate expense between two dates
        """
    unique_day_or_all = input("Specific date expense or month, week or last few days or total expense till date"
                              ": (all / day / month / week / last): ")
    if unique_day_or_all == "all":
        calc_total.calculate_total_amount()
    elif unique_day_or_all == "d" or unique_day_or_all == "day":
        day_to_calculate = calc_total.get_expense_date(input("Enter which day you wants to calculate: "))
        calc_total.calculate_day_expense(day_to_calculate)
    elif unique_day_or_all == "m" or unique_day_or_all == "month":
        month_to_calculate = input("Enter which month you wants to calculate: ")
        if month_to_calculate in calc_total.months_dict1:
            calc_total.calculate_month_expense(month_to_calculate)
        else:
            calc_total.calculate_month_expense(calc_total.months_dict[month_to_calculate.title()])
    elif unique_day_or_all == "w" or unique_day_or_all == "week":
        calc_total.calculate_last_n_days_expense(7)
    elif unique_day_or_all == "l" or unique_day_or_all == "last":
        calc_total.calculate_last_n_days_expense(int(input("Enter number of days wants to calculate: ")))
    else:
        print("Your choice is not valid or unavailable here.")


def get_user_action():
    expense_or_total = user_entry.get()
    if expense_or_total == "expense" or expense_or_total == "ex" or expense_or_total == "e":
        open_expense_window()
    elif expense_or_total == "total" or expense_or_total == "t":
        open_total_window()


def open_expense_window():
    main_window.destroy()
    expense_window = Tk()
    expense_window.title("NP's Expense Tracker")
    expense_window.config(padx=100, pady=50, bg=BLUE)

    expense_type = Label(expense_window, text="Enter expense type, day or single: ")
    expense_type.grid(row=0, column=0, padx=20, pady=20)

    expense_type_entry = Entry(expense_window)
    expense_type_entry.grid(row=0, column=1, padx=20, pady=20)

    submit_type_button = Button(expense_window, width=20, text="Submit",
                                command=lambda: initiate_expense_calculation(expense_type_entry.get()))
    submit_type_button.grid(padx=20, pady=20, column=1, row=2)

    expense_window.mainloop()


def open_total_window():
    pass


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#164694"
YELLOW = "#ffffaa"
FONT_NAME = "Courier"
CHECKMARK = "🗹"

# ---------------------------- UI SETUP ------------------------------- #


main_window = Tk()
main_window.title("NP's Expense Tracker")
main_window.config(padx=100, pady=50, bg=BLUE)

PASSWORD_FILE = "data.json"
DATA_FILE = "data2.json"


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def verify_entries(web, mail, passcode):
    process_site = True
    website_regex = re.compile(r'[A-Za-z\d]{4,}')
    email_regex = re.compile(r'([A-Za-z\d]+[.-_])*[A-Za-z\d]+@[A-Za-z\d-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(email_regex, mail):
        messagebox.showinfo(title="Email not valid", message="Verify the Email details")
        process_site = False
    if not re.fullmatch(website_regex, web):
        messagebox.showinfo(title="Website not valid", message="Verify the Website name")
        process_site = False
    if len(passcode) < 6:
        messagebox.showinfo(title="Password Criteria", message="Password should be more than 6 characters")
        process_site = False

    return process_site


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def save_password2():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    process_site = verify_entries(website, email, password)
    if process_site:
        is_ok = messagebox.askokcancel(title=website, message=f"Verify entered details \nEmail: {email}\n"
                                                              f"Password: {password}\n\nIs it okay to save?\n")
        if is_ok:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            new_web_data = {
                website: {
                    "Email": email,
                    "Password": password
                }
            }
            # print(new_web_data)
            try:
                with open(DATA_FILE, mode='r') as data_file:
                    data = json.load(data_file)
                    data.update(new_web_data)
            except FileNotFoundError:
                with open(DATA_FILE, mode='w') as data_file:
                    json.dump(new_web_data, data_file, indent=4)
            else:
                with open(DATA_FILE, mode='w') as data_file:
                    json.dump(data, data_file, indent=4)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def clear_fields():
    web_entry.delete(0, END)
    # email_entry.delete(0, END)
    password_entry.delete(0, END)
    web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# Launcher main_window and elements in App
expense_or_total_label = Label(text="Expense or Total?: ")
expense_or_total_label.grid(padx=20, pady=20, column=0, row=1)
user_entry = Entry(width=30)
user_entry.grid(padx=20, pady=20, column=1, row=1)
submit_button = Button(width=20, text="Submit", command=lambda: get_user_action())
submit_button.grid(padx=20, pady=20, column=1, row=2)

main_window.mainloop()
