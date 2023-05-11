"""Laboratory No. 3     Group 1 - De las Alas, Guzman, Lozano, Salino, Tabobo"""
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

class ListBoxTest :
    def __init__(self) :
        self.root = Tk()
        self.list_box_1 = Listbox(self.root, selectmode=EXTENDED)
        self.list_box_1.pack()
        self.delete_button = Button(self.root, text="Delete", command=self.DeleteSelection)
        self.delete_button.pack()
        self.insert_button = Button(self.root, text="Insert", command=self.InsertSelection)
        self.insert_button.pack(pady=5)
        self.list_box_1.insert(1, "C++")
        self.list_box_1.insert(2, "Python")
        self.list_box_1.insert(3, "HTML")
        self.list_box_1.insert(4, "Java")
        self.data_entry = Entry(self.root)
        self.root.mainloop()

    def DeleteSelection(self):
        items = self.list_box_1.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.list_box_1.delete(idx, idx)
            pos = pos + 1
    def InsertSelection(self):
        new_item = askstring('new_item', "Type below the item you want to insert")
        showinfo(
            title="Insert Selection",
            message="{}".format(new_item + " is inserted to the list"))
        self.list_box_1.insert(END, new_item)

lbt=ListBoxTest()