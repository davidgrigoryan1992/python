from tkinter import *

root = Tk()

def printName(event):
    print("Hello,my name is Davit")

button1 = Button(root, text="Print Name", bg="red")
button1.bind("<Button-1>", printName)
button1.pack()


root.mainloop()