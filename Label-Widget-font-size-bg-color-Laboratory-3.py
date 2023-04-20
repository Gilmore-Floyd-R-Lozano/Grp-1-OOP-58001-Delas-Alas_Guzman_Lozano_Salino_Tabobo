"""Laboratory No. 3     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
from tkinter import*

window = Tk()
window.geometry("400x150")
window.title("Father of Computer")

#Label Widget Font Size & Background Color Change
Label_Widget = Label(window, font=("Arial",20), text="Charles Babbage", bg="cyan")
Label_Widget.place(relx=.5, rely=.5, anchor=CENTER)

window.mainloop()