import smtplib

my_email = "nagarajdevtest@gmail.com"
with open("../../ignore_dir/mail_app_password.txt") as passcode:
    password = passcode.read()

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="rishihassans@gmail.com", msg="Subject:Test mail\n\nHello, I am "
                                                                               "sending mail from my python program")
connection.close()

