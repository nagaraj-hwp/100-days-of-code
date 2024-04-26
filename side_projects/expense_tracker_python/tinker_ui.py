# Creating a simple expense tracker using Python
from tkinter import *
from tkinter import messagebox
import os
import json
from random import randint, choice, shuffle
import pyperclip
import re
import calc_total
import file_update


def initiate_expense_calculation():
    expense_type = input("Enter expense type, whether a complete day expense or single expense: ")
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
    expense_or_total = input("Are you adding expense or want to calculate total: ")
    if expense_or_total == "expense" or expense_or_total == "ex" or expense_or_total == "e":
        initiate_expense_calculation()
    elif expense_or_total == "total" or expense_or_total == "t":
        initiate_total_calculation()


# if __name__ == "__main__":
#     get_user_action()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#164694"
YELLOW = "#ffffaa"
FONT_NAME = "Courier"
CHECKMARK = "🗹"

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("NP's Expense Tracker")
window.config(padx=100, pady=50, bg=BLUE)

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

# Labels in App
expense_or_total_label = Label(text="Adding expense or Total calculation")
expense_or_total_label.grid(column=0, row=1)
user_entry = Entry(width=30)
user_entry.grid(column=1, row=1)
user_entry.focus()
user_choice = user_entry.get()
submit_button = Button(width=20, text="Submit", command=lambda: get_user_action())
submit_button.grid(column=1, row=2)
# email_label = Label(text="Email/Username:")
# email_label.grid(column=0, row=2)
# password_label = Label(text="Password:")
# password_label.grid(column=0, row=3)

# Entries in App
# web_entry = Entry(width=30)
# web_entry.grid(column=1, row=1)
# web_entry.focus()
#
# search_button = Button(width=20, text="Search", command=search_password)
# search_button.grid(column=2, row=1)
#
# email_entry = Entry(width=30)
# email_entry.grid(column=1, row=2)
# email_entry.insert(0, "nagaraj@gmail.com")
#
# clear_button = Button(width=20, text="Clear", command=clear_fields)
# clear_button.grid(column=2, row=2)
#
# password_entry = Entry(width=30)
# password_entry.grid(column=1, row=3)
#
# # Buttons in App
# generate_button = Button(width=20, text="Generate Password", command=generate_password)
# generate_button.grid(column=2, row=3)
# add_password_button = Button(width=45, text="Add Password", command=save_password2)
# add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
