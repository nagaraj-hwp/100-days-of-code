# tkinter module miles to kilometer converter

from tkinter import *


window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=400, height=400)
window.config(padx=100, pady=100)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

mile_label = Label()
mile_label.config(text="Miles")
mile_label.grid(column=2, row=0)

km_label = Label()
km_label.config(text="KM")
km_label.grid(column=2, row=1)

label_1 = Label()
label_1.config(text="is equal to ")
label_1.grid(column=0, row=1)


convert_label = Label()
# convert_label.config(text="is equal to ")
convert_label.grid(column=1, row=1)
convert_label.config(padx=50, pady=50)


def convert():
    miles = miles_input.get()
    km = float(miles) * 1.60934
    convert_label.config(text=f"{km}")


calculate = Button()
calculate.config(text="Calculate", command=convert)

calculate.grid(column=1, row=2)

window.mainloop()

