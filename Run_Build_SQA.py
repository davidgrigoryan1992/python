from tkinter import *

root = Tk()
root.title("SQA Run Tool...")
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(400, 200))

var = StringVar(root)
var.set("N2017.12")

def grab_and_assign(event):
    chosen_option = var.get()
    label_chosen_variable= Label(root, text=chosen_option)
    label_chosen_variable.grid(row=7, column=1)
    print (chosen_option)

label_select_build= Label(root, text="Select Build: ")
label_select_build.grid(row=1, column=0)

drop_menu = OptionMenu(root, var,  "N2017.12", "M2017.03-SP1", "M2017.03", "K2016.06-SP2", command=grab_and_assign)
drop_menu.grid(row=1, column=1)

label_1 = Label(root, text="TC path:")
label_2 = Label(root, text="TC log path:")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=5, sticky=W)
label_2.grid(row=6, sticky=W)

entry_1.grid(row=5, column=1)
entry_2.grid(row=6, column=1)


label_left=Label(root, text="Run build : ", anchor=W)
label_left.grid(row=7, column=0)

root.mainloop()