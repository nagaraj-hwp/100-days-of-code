# Creating a simple expense tracker using Python for day, week and month level expense calculation.

import datetime as dt
import json
import os
import re
import shutil
import subprocess

# Can keep an empty json file
WRITEFILE = "../../ignore_dir/expenses_t_file.json"

months_dict1 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}
months_dict = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
}


def add_single_expense(date):
    new_expense = {"Amount": float(input("Enter amount spent Rs ₹: ")),
                   "Description": input("Enter what you spent for: Eg: Food")}
    update_expense_file(date, [new_expense])


def update_expense_file(payment_date, expense_list):
    print("payment_date is", payment_date)
    # print("expense list before feeds", expense_list)
    my_day_expense = {payment_date: expense_list}
    a = []
    if not os.path.isfile(WRITEFILE):
        a.append(my_day_expense)
        with open(WRITEFILE, mode='w') as f:
            f.write(json.dumps(a, indent=2))
    else:
        with open(WRITEFILE) as feeds_json:
            feeds = json.load(feeds_json)
            # print("existing feeds", feeds)
            if payment_date in feeds.keys():
                exist = feeds[payment_date]
                # print("exist: ", exist)
                expense_list.extend(exist)
                # print("expense list after feeds", expense_list)
            feeds[payment_date] = expense_list
            # print(feeds)
        with open(WRITEFILE, mode='w') as f:
            f.write(json.dumps(feeds, indent=2))


def add_multiple_expense(date):
    expenses = []
    entry = True
    while entry:
        new_expense = {"Amount": float(input("Enter amount you have spent Rs ₹: ")),
                       "Description": input("Enter what you spent for (string Eg: 'Groceries'): ")}
        expenses.append(new_expense)
        more = input("Is there any more expense to add: ").lower()
        if more == "true" or more == "y" or more == "yes":
            continue
        else:
            entry = False
    update_expense_file(date, expenses)


def get_expense_date(expense_day):
    if expense_day == "today" or expense_day == "td":
        day_to_date = str(dt.date.today())
    elif expense_day == "yesterday" or expense_day == "y":
        today = dt.date.today()
        day_to_date = str(today - dt.timedelta(days=1))
    else:
        # date_match = re.search('((\\d{4})-(\\d{2})-(\\d{2}))', expense_day)
        # expense_date = date_match[0]
        day_to_date = expense_day
    print(f"\nAdding expense for date: {day_to_date}\n")
    return day_to_date


def calculate_month_expense(month):
    month_pattern = rf'(\d{{4}})-{month}-(0[1-9]|[1-2][0-9]|3[0-1])'
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        for key, values in feeds.items():
            match = re.match(month_pattern, key)
            if match is not None:
                for value in values:
                    total_spent += value["Amount"]
    print(f"'Total amount spent on month {months_dict1[month]} is {total_spent} Rupees.'")


# def calculate_week_expense():
#     today = dt.date.today()
#     week_days = [str(today - dt.timedelta(days=i)) for i in range(0, 7)]
#     with open(WRITEFILE) as feeds_json:
#         feeds = json.load(feeds_json)
#         total_spent = 0
#         for key, values in feeds.items():
#             if key in week_days:
#                 for value in values:
#                     total_spent += value["Amount"]
#     print(f"'Total amount spent last week is {total_spent} Rupees.'")

def calculate_last_n_days_expense(number_of_days=7):
    today = dt.date.today()
    last_days_to_calculate = [str(today - dt.timedelta(days=i)) for i in range(0, number_of_days)]
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        for key, values in feeds.items():
            if key in last_days_to_calculate:
                for value in values:
                    total_spent += value["Amount"]
    print(f"Total amount spent on last {number_of_days} days is '{total_spent}' Rupees.")


def calculate_day_expense(day_to_calc):
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        if day_to_calc in feeds.keys():
            spent_list = feeds[day_to_calc]
            for item in spent_list:
                total_spent += item["Amount"]
        else:
            print("No such day exist, check your day.\n")
    print(f"'Total amount spent on {day_to_calc} is ''{total_spent}'' Rupees.'")


def calculate_total_amount():
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        for key, values in feeds.items():
            for value in values:
                total_spent += value["Amount"]
    print(f"'Total amount spent as per record is {total_spent} Rupees.'")


def update_back_up_file():
    shutil.copyfile('../../ignore_dir/expenses_t_file.json', '../../ignore_dir/expense_backup_file.json')
    shutil.copyfile('../../ignore_dir/expenses_t_file.json', '../../ignore_dir/expense_log_test.json')
    shutil.copyfile('../../ignore_dir/expenses_t_file.json', '../../ignore_dir/expense_log_test_bkp.json')
    shutil.copyfile('../../ignore_dir/expenses_t_file.json', '../../../private_data_files/expenses_t_file.json')
    shutil.copyfile('../../ignore_dir/expenses_t_file.json', '../../../private_data_files/expense_backup_file.json')
    print("Updated backup file.")


def update_expense_data_in_git():
    print("**************************************")
    commit_message = input("Enter Commit message: ")
    data_files_repo = "../../../private_data_files"
    os.chdir(data_files_repo)
    subprocess.run(["git", "commit", "-a", "-m", commit_message])
    subprocess.run(["git", "push", "origin", "master"])


def initiate_calculation():
    expense_type = input("Enter expense type, whether day or single expense or total: ")
    if expense_type == "d" or expense_type == "day":
        input_day = input("Enter date of the expense(YYYY−MM−DD) or just 'today' "
                          "(careful with your expense date input): ")
        expense_date = get_expense_date(input_day)
        add_multiple_expense(expense_date)
        update_back_up_file()
        calculate_day_expense(expense_date)
        # update_expense_data_in_git()
    elif expense_type == "single" or expense_type == "s":
        input_day = input("Enter which day it should be added to(careful with your expense date input): ")
        expense_date = get_expense_date(input_day)
        add_single_expense(expense_date)
        update_back_up_file()
        # update_expense_data_in_git()
    elif expense_type == "total" or expense_type == "t":
        unique_day_or_all = input("Wanna calculate total expense till now or specific date or month"
                                  " or week: (all or one): ")
        if unique_day_or_all == "all":
            calculate_total_amount()
        elif unique_day_or_all == "d" or unique_day_or_all == "day":
            day_to_calculate = get_expense_date(input("Enter which day you wants to calculate: "))
            calculate_day_expense(day_to_calculate)
        elif unique_day_or_all == "m" or unique_day_or_all == "month":
            month_to_calculate = input("Enter which month you wants to calculate: ")
            if month_to_calculate in months_dict1:
                calculate_month_expense(month_to_calculate)
            else:
                calculate_month_expense(months_dict[month_to_calculate.title()])
        elif unique_day_or_all == "w" or unique_day_or_all == "week":
            calculate_last_n_days_expense()
        elif unique_day_or_all == "some":
            calculate_last_n_days_expense(int(input("Enter number of days: ")))


if __name__ == "__main__":
    # initiate_calculation()
    update_back_up_file()
    update_expense_data_in_git()
