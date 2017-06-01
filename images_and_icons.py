from tkinter import *

root = Tk()

photo = PhotoImage(file="fortune-room-logo.jpg")
label = Label(root, image=photo)
label.pack()


root.mainloop()