 Tkinter UI basics understanding

import tkinter

window = tkinter.Tk()

window.title("MY first UI with TK")
window.minsize(width=500, height=600)
label_1 = tkinter.Label(text="This is a sample label", font=("courier", 24))
label_1.pack(side="left")

window.mainloop()

