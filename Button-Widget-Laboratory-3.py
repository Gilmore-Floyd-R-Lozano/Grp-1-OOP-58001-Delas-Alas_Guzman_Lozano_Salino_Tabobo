"""Laboratory No. 3     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
from tkinter import*

window = Tk()
window.geometry("400x150")
window.title("Button")

#Button Widget
def changecolor():
    Button_Widget1.configure(bg="yellow")

Button_Widget1=Button(window, text="Color", fg="red", bg="blue")
Button_Widget1.place(x=50, y=60)

Button_Widget2=Button(window, text="<---Click to change the color of the button",command=changecolor)
Button_Widget2.place(x=100,y=60)

window.mainloop()