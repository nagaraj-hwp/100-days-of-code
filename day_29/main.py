from tkinter import *
from tkinter import messagebox
import os
import json
from random import randint, choice, shuffle
import pyperclip
import re

PASSWORD_FILE = "data.json"
DATA_FILE = "data2.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 9))]
    password_symbols = [choice(symbols) for _ in range(randint(4, 5))]
    password_numbers = [choice(numbers) for _ in range(randint(4, 5))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password_gen = "".join(password_list)
    # print("Your password is:", password_gen)
    password_entry.delete(0, END)
    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    process_site = True
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    website_regex = re.compile(r'[A-Za-z\d]{4,}')
    email_regex = re.compile(r'([A-Za-z\d]+[.-_])*[A-Za-z\d]+@[A-Za-z\d-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(email_regex, email):
        messagebox.showinfo(title="Email not valid", message="Verify the Email details")
        process_site = False
    if not re.fullmatch(website_regex, website):
        messagebox.showinfo(title="Website not valid", message="Verify the Website name")
        process_site = False
    if len(password) < 6:
        messagebox.showinfo(title="Password Criteria", message="Password should be more than 6 characters")
        process_site = False
    if process_site:
        is_ok = messagebox.askokcancel(title=website, message=f"Verify entered details \nEmail: {email}\n"
                                                              f"Password: {password}\n\nIs it okay to save?\n")
        if is_ok:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            password_dict = {"Website": website, "Email": email, "Password": password}
            # print(password_dict)
            collection_list = []
            if not os.path.isfile(PASSWORD_FILE):
                collection_list.append(password_dict)
                with open(PASSWORD_FILE, mode='w') as f:
                    f.write(json.dumps(collection_list, indent=4))
            else:
                with open(PASSWORD_FILE) as all_data:
                    feeds = json.load(all_data)
                    feeds.append(password_dict)
                with open(PASSWORD_FILE, mode='w') as f:
                    f.write(json.dumps(feeds, indent=4))


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
def search_password():
    website = web_entry.get().title()
    try:
        with open(DATA_FILE) as pass_file:
            complete_data = json.load(pass_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Password File", message="No password file exists in the directory")
    else:
        if website in complete_data:
            email = complete_data[website]["email"]
            password = complete_data[website]["password"]
            messagebox.showinfo(title="INFO", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"Details are not in records for website: '{website}'")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def clear_fields():
    web_entry.delete(0, END)
    # email_entry.delete(0, END)
    password_entry.delete(0, END)
    web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="LOGO.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels in App
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries in App
web_entry = Entry(width=30)
web_entry.grid(column=1, row=1)
web_entry.focus()

search_button = Button(width=20, text="Search", command=search_password)
search_button.grid(column=2, row=1)

email_entry = Entry(width=30)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "nagaraj@gmail.com")

clear_button = Button(width=20, text="Clear", command=clear_fields)
clear_button.grid(column=2, row=2)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# Buttons in App
generate_button = Button(width=20, text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_password_button = Button(width=45, text="Add Password", command=save_password2)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
