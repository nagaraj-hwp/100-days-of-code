# Creating a simple expense tracker using Python
import datetime as dt
from datetime import timedelta
import json
import re

# Can keep an empty json file
WRITEFILE = "../../ignore_dir/expense_log_test.json"

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
    # print(f"\nAdding expense for date: {day_to_date}\n")
    return day_to_date


def total_food_expense(month):
    food_words_list = ["sambar", "curd", "briyani", "biryani", "dosa", "breakfast", "lunch", "dinner", "chicken",
                       "groceries", "rice", "coconut", "banana", "halwa", "water", "mutton", "maavu", "egg"]
    month_pattern = rf'(\d{{4}})-{month}-(0[1-9]|[1-2][0-9]|3[0-1])'
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        for key, values in feeds.items():
            match = re.match(month_pattern, key)
            if match is not None:
                for value in values:
                    for item in food_words_list:
                        if item in value["Description"].lower():
                            print(f'{key} Matched description {value["Description"]}')
                            total_spent += value["Amount"]
                            break
    return f"'Total amount spent on month {months_dict1[month]} for food is {total_spent} Rupees.'"


def calculate_between_dates(start_dt, end_dt):
    start_date = dt.datetime.strptime(start_dt, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end_dt, "%Y-%m-%d")
    if start_date > end_date:
        print("Can't proceed: Start date is after end date")
        return 0
    no_of_days = (end_date - start_date).days
    days_to_calculate = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(no_of_days + 1)]
    print(days_to_calculate)
    with open(WRITEFILE) as data_feeds:
        feeds = json.load(data_feeds)
        total_spent = 0
        for key, values in feeds.items():
            if key in days_to_calculate:
                for value in values:
                    total_spent += value["Amount"]
    # print(f"Total amount spent on this particular {no_of_days + 1} days is '{total_spent}' Rupees.")
    return f"Total amount spent on this particular {no_of_days + 1} days is '{total_spent}' Rupees."


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
    return f"'Total amount spent on month {months_dict1[month]} is {total_spent} Rupees.'"


def calculate_last_n_days_expense(number_of_days=1):
    today = dt.date.today()
    last_days_to_calculate = [str(today - dt.timedelta(days=i)) for i in range(0, number_of_days)]
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        for key, values in feeds.items():
            if key in last_days_to_calculate:
                for value in values:
                    total_spent += value["Amount"]
    return f"Total amount spent on last {number_of_days} days is '{total_spent}' Rupees."


def calculate_day_expense(day_to_calc):
    with open(WRITEFILE) as feeds_json:
        feeds = json.load(feeds_json)
        total_spent = 0
        if day_to_calc in feeds.keys():
            spent_list = feeds[day_to_calc]
            for item in spent_list:
                total_spent += item["Amount"]
        else:
            print(f"No such day exist as {day_to_calc}, check your day.\n")
    # print(f"'Total amount spent on {day_to_calc} is ''{total_spent}'' Rupees.'")
    return f"'Total amount spent on {day_to_calc} is ''{total_spent}'' Rupees.'"


def calculate_total_amount():
    with open(WRITEFILE) as feeds_json:
        expense_data = json.load(feeds_json)
        total_spent = 0
        for key, values in expense_data.items():
            for value in values:
                total_spent += value["Amount"]
    return f"'Total amount spent as per record is {total_spent} Rupees.'"


if __name__ == "__main__":
    print(total_food_expense(input("Enter Month to calculate: ")))
    # print(calculate_month_expense(input("Enter Month to calculate: ")))
