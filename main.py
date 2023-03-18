import tkinter
from tkinter import E,W,N,S

window = tkinter.Tk()
window.title("calculator project")

lbl_result = tkinter.Label(
    master=window,
    text="0",
    width=30,
    height=3,
)

lbl_result.grid(row=0,column=0)
window.mainloop()