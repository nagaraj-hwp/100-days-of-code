from tkinter import *
from tkinter import messagebox
import os
import json

PASSWORD_FILE = "data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    process_site = True
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Details not filled", message="Don't leave website empty")
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
web_entry = Entry(width=50)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "nagaraj___@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# Buttons in App
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)
add_password_button = Button(text="Add Password", width=40, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
