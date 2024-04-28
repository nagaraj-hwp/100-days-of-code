# Creating a simple expense tracker using Python
from tkinter import *
from tkinter import messagebox
import calc_total
import file_update


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#164694"
YELLOW = "#ffffaa"
FONT_NAME = "Courier"
CHECKMARK = "🗹"


def initiate_expense_calculation(expense_type):
    if expense_type == "d" or expense_type == "day":
        input_day = input("Enter date of the expense(YYYY−MM−DD) or just 'today' "
                          "(careful with your expense date input): ")
        expense_date = calc_total.get_expense_date(input_day)
        file_update.add_single_expense(expense_date, new_expense=None)
        file_update.update_back_up_file()
        calc_total.calculate_day_expense(expense_date)
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


def calculate_all(date_field, tk_window):
    exp_day = calc_total.get_expense_date(str(date_field.get()))
    total = calc_total.calculate_day_expense(exp_day)
    messagebox.showinfo(title="Total expense for the day",
                        message=f"'Total amount spent on {exp_day} is ''{total}'' Rupees.'")
    tk_window.destroy()


def take_expense(expense_date, expense_entry, expense_des_entry):
    process = True
    if expense_date.get() == "" or expense_date.get() is None:
        messagebox.showinfo(title="Expense date shouldn't be empty", message="Verify the Expense date field")
        process = False
    if expense_entry.get() == "" or expense_entry.get() is None and isinstance(expense_entry.get(), int):
        messagebox.showinfo(title="Expense Amount shouldn't be empty", message="Verify the Expense Amount field")
        process = False
    if expense_des_entry.get() == "" or expense_des_entry.get() is None:
        messagebox.showinfo(title="Expense Description shouldn't be empty",
                            message="Verify the Expense Description field")
        process = False
    if process:
        expense = {
            "Amount": int(expense_entry.get()),
            "Description": str(expense_des_entry.get())
        }
        exp_day = calc_total.get_expense_date(str(expense_date.get()))
        # expense_date.delete(0, END)
        expense_entry.delete(0, END)
        expense_des_entry.delete(0, END)
        file_update.add_single_expense(exp_day, expense)
    else:
        messagebox.showinfo(title="Error occurred",
                            message="Verify the input fields")


def open_expense_initiation_window(expense_window):
    expense_window.destroy()
    add_window = Tk()
    add_window.title("NP's Expense Tracker: Add expense")
    add_window.config(padx=100, pady=50, bg=BLUE)

    expense_date = Label(add_window, text="Enter expense date ")
    expense_date.grid(row=0, column=0, padx=20, pady=20)

    expense_date_entry = Entry(add_window)
    expense_date_entry.grid(row=0, column=1, padx=20, pady=20)
    expense_date_entry.focus()

    expense_amount = Label(add_window, text="Enter expense amount ")
    expense_amount.grid(row=1, column=0, padx=20, pady=20)

    expense_amount_entry = Entry(add_window)
    expense_amount_entry.grid(row=1, column=1, padx=20, pady=20)

    expense_description = Label(add_window, text="Enter expense description ")
    expense_description.grid(row=2, column=0, padx=20, pady=20)

    expense_description_entry = Entry(add_window)
    expense_description_entry.grid(row=2, column=1, padx=20, pady=20)

    more_expense_button = Button(add_window, width=20, text="Add Expense",
                                 command=lambda: take_expense(expense_date_entry,
                                                              expense_amount_entry, expense_description_entry))
    more_expense_button.grid(padx=20, pady=20, column=1, row=3)

    complete_expense_button = Button(add_window, width=20, text="Complete expense",
                                     command=lambda: calculate_all(expense_date_entry, add_window))
    complete_expense_button.grid(padx=20, pady=20, column=1, row=4)

    expense_window.mainloop()


def open_expense_window():
    main_window.destroy()
    expense_window = Tk()
    expense_window.title("Nagaraj P's Expense Tracker")
    expense_window.config(padx=100, pady=50, bg=BLUE)

    expense_type = Label(expense_window, text="Enter expense type, day or single: ")
    expense_type.grid(row=0, column=0, padx=20, pady=20)

    expense_type_entry = Entry(expense_window)
    expense_type_entry.grid(row=0, column=1, padx=20, pady=20)
    expense_type_entry.focus()

    submit_type_button = Button(expense_window, width=20, text="Submit",
                                command=lambda: open_expense_initiation_window(expense_window))
    submit_type_button.grid(padx=20, pady=20, column=1, row=2)

    expense_window.mainloop()


def open_total_window():
    pass


if __name__ == "__main__":
    # Launcher main_window and elements in App
    main_window = Tk()
    main_window.title("NP's Expense Tracker")
    main_window.config(padx=100, pady=50, bg=BLUE)
    expense_or_total_label = Label(text="Expense or Total ")
    expense_or_total_label.grid(padx=20, pady=20, column=0, row=1)
    user_entry = Entry(width=30)
    user_entry.grid(padx=20, pady=20, column=1, row=1)
    user_entry.focus()
    submit_button = Button(width=20, text="Submit", command=lambda: get_user_action())
    submit_button.grid(padx=20, pady=20, column=1, row=2)

    main_window.mainloop()
