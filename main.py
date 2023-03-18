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

btn_7 = tkinter.Button(
    master=window,
    text="7",
)
btn_8 = tkinter.Button(
    master=window,
    text="8",
)
btn_9 = tkinter.Button(
    master=window,
    text="9",
)
btn_plus = tkinter.Button(
    master=window,
    text="+",
)
lbl_result.grid(row=0,column=0,columnspan=4)
btn_7.grid(row=1,column=0,sticky=(E,W))
btn_8.grid(row=1,column=1,sticky=(E,W))
btn_9.grid(row=1,column=2,sticky=(E,W))
btn_plus.grid(row=1,column=3,sticky=(E,W))
window.mainloop()


