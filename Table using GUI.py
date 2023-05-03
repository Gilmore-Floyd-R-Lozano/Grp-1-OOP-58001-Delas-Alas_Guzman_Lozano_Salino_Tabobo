"""Laboratory No. 6     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
# using tkinter GUI
import tkinter as tk
window = tk.Tk()
window.title("Power of a")
window.geometry("400x200")

tk.Label(window, text="       a       ", font=("Arial", 10)).grid(column=0, row=0)
tk.Label(window, text="      a^2      ", font=("Arial", 10)).grid(column=1, row=0)
tk.Label(window, text="      a^3      ", font=("Arial", 10)).grid(column=2, row=0)

tk.Label(window, text="1", font=("Arial", 10)).grid(column=0, row=1)
tk.Label(window, text="1", font=("Arial", 10)).grid(column=1, row=1)
tk.Label(window, text="1", font=("Arial", 10)).grid(column=2, row=1)

tk.Label(window, text="2", font=("Arial", 10)).grid(column=0, row=2)
tk.Label(window, text="4", font=("Arial", 10)).grid(column=1, row=2)
tk.Label(window, text="8", font=("Arial", 10)).grid(column=2, row=2)

tk.Label(window, text="3", font=("Arial", 10)).grid(column=0, row=3)
tk.Label(window, text="9", font=("Arial", 10)).grid(column=1, row=3)
tk.Label(window, text="27", font=("Arial", 10)).grid(column=2, row=3)

tk.Label(window, text="4", font=("Arial", 10)).grid(column=0, row=4)
tk.Label(window, text="16", font=("Arial", 10)).grid(column=1, row=4)
tk.Label(window, text="64", font=("Arial", 10)).grid(column=2, row=4)

window.mainloop()