"""Laboratory No. 3     Group 1 - De las Alas, Guzman, Lozano, Salino, Tabobo"""
from tkinter import*

window = Tk()
window.geometry("400x150")
window.title("Text Field")

#Text Field Widget
TextField_Widget =Text(window, pady=25,font=("Arial"),height=1,width=21)
TextField_Widget.place(relx=.5, rely=.5, anchor=CENTER)

window.mainloop()