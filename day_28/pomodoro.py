# Creating Pomodora app with tkinter
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#ffffaa"
FONT_NAME = "Courier"
CHECKMARK = "🗹"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 32, "bold"), fill="white")
canvas.grid(column=1, row=1)

# count_down(5)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="START", bg=YELLOW, highlightthickness=0, command=start_timer)
# start_button.config()
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text=CHECKMARK, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
checkmark_label.grid(column=1, row=3)












window.mainloop()
