# Understanding Function with outputs

# def format_name(f_name, l_name):
#     # f_name = "Nagaraj"
#     # l_name = "Palpandi"
#     return f"{f_name.title()} {l_name.title()}"
    

# print(format_name("nagaraj", "NaGaraJ"))

# -----------------------------------------------------------------------------------------------------
# LESSON 24 DAY 10 - DAYS IN MONTH
# Convert the is_leap() functtion
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                    return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days_for_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    month_days_for_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    leap = is_leap(year)
    if leap:
        return(month_days_for_leap[month-1])
    else:
        return(month_days_for_non_leap[month-1])
    # if leap and month == 2:
    #     return 29
    # else:
    #     return month_days_for_non_leap[month-1]
    

year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

# -----------------------------------------------------------------------------------------------------
