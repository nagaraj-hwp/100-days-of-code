#  Tkinter UI basics understanding

# import tkinter
#
# window = tkinter.Tk()
#
# window.title("MY first UI with TK")
# window.minsize(width=500, height=600)
# label_1 = tkinter.Label(text="This is a sample label", font=("courier", 24))
# label_1.pack(side="left")
#
# window.mainloop()


def fun(a=1, b=2, c=3):
    print(a, b, c)


fun()  # 1 2 3
fun(4, 5)  # 4 5 3
fun(4, c=9)  # 4 2 9
fun(b=10)  # 1 10 3
