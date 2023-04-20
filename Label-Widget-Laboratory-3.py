"""Laboratory No. 3     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
from tkinter import*

window = Tk()
window.geometry("400x150")
window.title("Label")

#Label Widget
Label_Widget = Label(window, text="Laboratory Activity 5\nSubmitted to: Mam Sayo")
Label_Widget.place(relx=.5, rely=.5, anchor=CENTER)

window.mainloop()