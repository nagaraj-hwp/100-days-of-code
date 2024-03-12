import smtplib
import datetime as dt
from random import choice, randint
import pandas


my_email = "nagarajdevtest@gmail.com"
with open("../../ignore_dir/mail_app_password.txt") as passcode:
    password = passcode.read()


def send_monday_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                            from_addr=my_email,
                            to_addrs="rishihassans@gmail.com",
                            msg=f"Subject:Happy Monday\n\n{quote}"
        )


def week_start():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    if day_of_week == 0:
        with open("quotes.txt", "r") as quotes:
            quotes_list = quotes.readlines()
            random_quote = choice(quotes_list)
        send_monday_email(random_quote)


def get_email_body(name):
    letter_file = f"letter_{randint(1, 3)}.txt"
    print(letter_file)
    with open(letter_file) as wish:
        content = wish.read()
        email_content = content.replace("[name]", name)
    return email_content


def send_birthday_wish(data):
    content = get_email_body(data.person_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=data.email,
            msg=f"Subject:Happy Birthday\n\n{content}")


def wish_for_birthday():
    today = dt.datetime.today()
    month = today.month
    day = today.day
    birthday_data = pandas.read_csv("birthdays.csv")
    for (index, row) in birthday_data.iterrows():
        if row.month == month and row.day == day:
            send_birthday_wish(row)


wish_for_birthday()
# week_start()
