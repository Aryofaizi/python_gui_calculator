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

# first approach for handling the lbl conditions of the eval 
# def set_result():
#     lbl_result["text"]+="7"
# def calc():
#     result = lbl_result["text"]
#     print(eval(result+"+5"))

# def set_result(btn_text):
#     operators = ["+","-","*","."]
#     current = lbl_result["text"][-1]
#     if current in operators and btn_text in operators and not current == btn_text:
#         lbl_result["text"] = lbl_result["text"].removesuffix(btn_text)
#         print("both operators")
#     elif lbl_result["text"] == "0" and btn_text in operators:
#         lbl_result["text"] = "0"
#     else:
#         print(current)
#         if lbl_result["text"]=="0":
#             lbl_result["text"] = ""
#         elif current == btn_text and current in operators:
#             lbl_result["text"] = lbl_result["text"].removesuffix(btn_text)
#         lbl_result["text"] += btn_text

# def calc_result():
#     result = lbl_result["text"]
#     lbl_result["text"] = str(eval(result))


# second approach for handling the lbl conditions of the eval 
def is_last_number_decimal(text):
    for char in text[::-1]:
        if char == ".":
            return True
        elif char in ["+","-","*"]:
            return False
    return False





def set_result(btn_text):
    operators = ["+","-","*"]
    current = lbl_result["text"]
    if lbl_result["text"] == "0":
        lbl_result["text"] = btn_text
    elif btn_text == "=":
        lbl_result["text"] = str(eval(lbl_result["text"]))
    else:
        if btn_text in operators and current[-1] in operators:
            lbl_result["text"] = lbl_result["text"][:-1]+btn_text
        elif btn_text == ".":
            if not is_last_number_decimal(current):                
                lbl_result["text"] += btn_text
        else:
            lbl_result["text"] +=btn_text

# third approach 
btn_data = [
    {
        "text":"7",
        "command":lambda:set_result("7"),
    },
    {
        "text":"8",
        "command":lambda:set_result("8"),
    },
    {
        "text":"9",
        "command":lambda:set_result("9"),
    },
    {
        "text":"+",
        "command":lambda:set_result("+"),
    },
    {
        "text":"4",
        "command":lambda:set_result("4"),
    },
    {
        "text":"5",
        "command":lambda:set_result("5"),
    },
    {
        "text":"6",
        "command":lambda:set_result("6"),
    },
    {
        "text":"-",
        "command":lambda:set_result("-"),
    },
    {
        "text":"1",
        "command":lambda:set_result("1"),
    },
    {
        "text":"2",
        "command":lambda:set_result("2"),
    },
    {
        "text":"3",
        "command":lambda:set_result("3"),
    },
    {
        "text":"*",
        "command":lambda:set_result("*"),
    },
    {
        "text":".",
        "command":lambda:set_result("."),
    },
    {
        "text":"0",
        "command":lambda:set_result("0"),
    },
    {
        "text":"C",
        "command":lambda:set_result("C"),
    },
    {
        "text":"=",
        "command":lambda:set_result("="),
    },
]
btn_list = []
for btn_key in btn_data:
    btn = tkinter.Button(
        master=window,
        text=btn_key["text"],
        command=btn_key["command"],
        height=3,
    )
    btn_list.append(btn)
for i,btn in enumerate(btn_list):
    btn.grid(row=(i//4)+1,column=i%4,sticky=(E,W))

#row
#0,1,2,3 --> //4 = 0
#4,5,6,7 --> //4 = 1
#8,9,10,11 -->//4 = 2
#12,13,14,15 -->//4 = 3

#0,4,8,12 --> %4 = 0
#1,5,9,13 --> %4 = 1


window.mainloop()