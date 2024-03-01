# Creating a simple expense tracker using Python
import datetime
import json
import os

# Can keep an empty json file
WRITEFILE = "../../ignore_dir/expenses_t_file.json"


def add_single_expense(date):
    new_expense = {"Amount": int(input("Enter amount you have spent: ")),
                   "Description": input("Enter what you spent for: ")}
    update_expense_file(date, [new_expense])


def update_expense_file(payment_date, expense_list):
    print("payment_date is", payment_date)
    print("expense list before feeds", expense_list)
    my_day_expense = {payment_date: expense_list}
    a = []
    if not os.path.isfile(WRITEFILE):
        a.append(my_day_expense)
        with open(WRITEFILE, mode='w') as f:
            f.write(json.dumps(a, indent=2))
    else:
        with open(WRITEFILE) as feeds_json:
            feeds = json.load(feeds_json)
            print("existing feeds", feeds)
            if payment_date in feeds.keys():
                exist = feeds[payment_date]
                print("exist: ", exist)
                expense_list.extend(exist)
                print("expense list after feeds", expense_list)
            feeds[payment_date] = expense_list
            print(feeds)
        with open(WRITEFILE, mode='w') as f:
            f.write(json.dumps(feeds, indent=2))


def add_multiple_expense(date):
    expenses = []
    entry = True
    while entry:
        new_expense = {"Amount": int(input("Enter amount you have spent: ")),
                       "Description": input("Enter what you spent for: ")}
        expenses.append(new_expense)
        more = input("Is there any more expense to add: ").lower()
        if more == "true" or more == "y" or more == "yes":
            continue
        else:
            entry = False
    update_expense_file(date, expenses)


def get_expense_date(expense_day):
    if expense_day == "today" or expense_day == "td":
        day_to_date = str(datetime.date.today())
    else:
        # date_match = re.search('((\\d{4})-(\\d{2})-(\\d{2}))', expense_day)
        # expense_date = date_match[0]
        day_to_date = expense_day
    print(day_to_date)
    return day_to_date


def calculate_total_amount():
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        for key, values in feeds.items():
            for value in values:
                total_spent += value["Amount"]
    print(f"'Total amount spent as per record is {total_spent} Rupees.'")


def calculate_day_expense(day_to_calc):
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        if day_to_calc in feeds.keys():
            spent_list = feeds[day_to_calc]
            for item in spent_list:
                total_spent += item["Amount"]
        else:
            print("No such day exist :(\n")
    print(f"'Total amount spent on {day_to_calc} is {total_spent} Rupees.'")


expense_type = input("Enter expense type, whether day or single expense or total: ")
if expense_type == "d" or expense_type == "day":
    input_day = input("Enter date of the expense(YYYY−MM−DD) or just 'today' (careful with your expense date input): ")
    expense_date = get_expense_date(input_day)
    add_multiple_expense(expense_date)
elif expense_type == "single" or expense_type == "s":
    input_day = input("Enter which day it should be added to(careful with your expense date input): ")
    expense_date = get_expense_date(input_day)
    add_single_expense(expense_date)
elif expense_type == "total" or expense_type == "t":
    unique_day_or_all = input("Wanna calculate total expense till now or specific date: (all or one): ")
    if unique_day_or_all == "all":
        calculate_total_amount()
    else:
        day_to_calculate = input("Enter which day you wanted to calculate: ")
        calculate_day_expense(day_to_calculate)
