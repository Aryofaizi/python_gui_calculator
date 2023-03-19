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
lbl_result.grid(row=0,column=0,columnspan=4)

# first approach 
# btn_7 = tkinter.Button(
#     master=window,
#     text="7",
# )
# btn_8 = tkinter.Button(
#     master=window,
#     text="8",
# )
# btn_9 = tkinter.Button(
#     master=window,
#     text="9",
# )
# btn_plus = tkinter.Button(
#     master=window,
#     text="+",
# )
# btn_7.grid(row=1,column=0,sticky=(E,W))
# btn_8.grid(row=1,column=1,sticky=(E,W))   
# btn_9.grid(row=1,column=2,sticky=(E,W))
# btn_plus.grid(row=1,column=3,sticky=(E,W))



# second approach 
# btn_dict = {
#     "btn_1" :{
#         "text":"1",
#         "row":2,
#         "column":0,
#     },
#     "btn_2" :{
#         "text":"2",
#         "row":2,
#         "column":1,
#     },
#     "btn_3" :{
#         "text":"3",
#         "row":2,
#         "column":2,
#     },
#     "btn_plus" :{
#         "text":"+",
#         "row":2,
#         "column":3,
#     },
#     "btn_4" :{
#         "text":"4",
#         "row":3,
#         "column":0,
#     },
#     "btn_5" :{
#         "text":"5",
#         "row":3,
#         "column":1,
#     },
#     "btn_6" :{
#         "text":"6",
#         "row":3,
#         "column":2,
#     },
#     "btn_minus" :{
#         "text":"-",
#         "row":3,
#         "column":3,
#     },
#     "btn_7" :{
#         "text":"7",
#         "row":4,
#         "column":0,
#     },
#     "btn_8" :{
#         "text":"8",
#         "row":4,
#         "column":1,
#     },
#     "btn_9" :{
#         "text":"9",
#         "row":4,
#         "column":2,
#     },
#     "btn_multiply" :{
#         "text":"*",
#         "row":4,
#         "column":3,
#     },
#     "btn_dot" :{
#         "text":".",
#         "row":5,
#         "column":0,
#     },
#     "btn_zero" :{
#         "text":"0",
#         "row":5,
#         "column":1,
#     },
#     "btn_clear" :{
#         "text":"C",
#         "row":5,
#         "column":2,
#     },
#     "btn_equal" :{
#         "text":"=",
#         "row":5,
#         "column":3,
#     },
# }

# for btn_name,btn_details in btn_dict.items():
#     btn_name = tkinter.Button(
#         master=window,
#         text=btn_details["text"],
#         height=2,
#     )
#     btn_name.grid(row=btn_details["row"],column=btn_details["column"],sticky=(E,W))


# third approach 



window.mainloop()


