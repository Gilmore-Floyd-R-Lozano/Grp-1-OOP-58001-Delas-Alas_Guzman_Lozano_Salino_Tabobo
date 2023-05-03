"""Laboratory No. 6     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
# using GUI with generating list with loop and string formatting
from tkinter import*
window = Tk()
window.title("Power of a")
window.geometry("400x200")

table = [["a", "a^2", "a^3"]]

text1 = Text(window)
text1.pack()

# generating list
for num in range(1, 5):
    table.extend([[str(num), str(num**2), str(num**3)]])
for row in table:
    text1.insert(END, ' {}  {:^20}  {} '.format(*row))
    text1.insert(END, "\n")

window.mainloop()
