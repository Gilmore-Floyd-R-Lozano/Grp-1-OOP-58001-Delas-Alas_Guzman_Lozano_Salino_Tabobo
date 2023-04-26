"""             Laboratory No. 4     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo           """
import tkinter
from tkinter import *


class MyWindow:
    def __init__(self, win):
        #       variable for holding the pressed buttons
        self.val = ""

        #       variable for displayed equation
        self.equation = tkinter.StringVar()

        # ENTRY WIDGET for displaying the equation
        self.txt1 = Entry(win, textvariable=self.equation, font=("Century Gothic", 25), insertwidth=4, width=11,
                          justify=RIGHT, bd=0, bg="#000000", fg="white")
        self.txt1.insert(0, "0")
        self.txt1.grid(row=0, columnspan=10, sticky=N, padx=10, pady=10)

        # LABEL WIDGET
        self.lbl1 = Label(win, text="L Company", bg="#000000", fg="white", height=1, font=("Digital tech", 15),
                          justify=CENTER)
        self.lbl1.grid(column=0, row=1, columnspan=2)

        # BUTTON WIDGET for addition
        self.btnadd = Button(win, text="+", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white",
                             bg="#ff9501")
        self.btnadd.grid(row=5, column=3, pady=1)
        self.btnadd.bind('<Button-1>', self.add)

        # BUTTON WIDGET for subtraction
        self.btnsub = Button(win, text="-", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white",
                             bg="#ff9501")
        self.btnsub.grid(row=4, column=3, pady=1)
        self.btnsub.bind('<Button-1>', self.sub)

        # BUTTON WIDGET for multiplication
        self.btnmul = Button(win, text="*", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white",
                             bg="#ff9501")
        self.btnmul.grid(row=3, column=3)
        self.btnmul.bind('<Button-1>', self.mul)

        # BUTTON WIDGET for division
        self.btndiv = Button(win, text="/", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white",
                             bg="#ff9501")
        self.btndiv.grid(row=2, column=3)
        self.btndiv.bind('<Button-1>', self.div)

        # BUTTON WIDGET for equal sign
        self.btneql = Button(win, text="=", width=6, font=("Century Gothic", 18, "bold"), bd=0, fg="white",
                             bg="#ff9501")
        self.btneql.grid(row=6, column=2, columnspan=2, padx=11)
        self.btneql.bind('<Button-1>', self.eql)

        # BUTTON WIDGET for clear
        self.btnclr = Button(win, text="C", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="black",
                             bg="#a9a9a9")
        self.btnclr.grid(column=3, row=1)
        self.btnclr.bind('<Button-1>', self.clr)

        # BUTTON WIDGET for decimal point
        self.btndec = Button(win, text=".", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="black",
                             bg="#a9a9a9")
        self.btndec.grid(row=6, column=1)
        self.btndec.bind('<Button-1>', self.dec)

        # BUTTON WIDGET for Number 1
        self.btnN1 = Button(win, text="1", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN1.grid(row=5, column=0)
        self.btnN1.bind('<Button-1>', self.N1)

        # BUTTON WIDGET for Number 2
        self.btnN2 = Button(win, text="2", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN2.grid(row=5, column=1)
        self.btnN2.bind('<Button-1>', self.N2)

        # BUTTON WIDGET for Number 3
        self.btnN3 = Button(win, text="3", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN3.grid(row=5, column=2)
        self.btnN3.bind('<Button-1>', self.N3)

        # BUTTON WIDGET for Number 4
        self.btnN4 = Button(win, text="4", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN4.grid(row=4, column=0, padx=5, pady=5)
        self.btnN4.bind('<Button-1>', self.N4)

        # BUTTON WIDGET for Number 5
        self.btnN5 = Button(win, text="5", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN5.grid(row=4, column=1)
        self.btnN5.bind('<Button-1>', self.N5)

        # BUTTON WIDGET for Number 6
        self.btnN6 = Button(win, text="6", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN6.grid(row=4, column=2)
        self.btnN6.bind('<Button-1>', self.N6)

        # BUTTON WIDGET for Number 7
        self.btnN7 = Button(win, text="7", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN7.grid(row=3, column=0)
        self.btnN7.bind('<Button-1>', self.N7)

        # BUTTON WIDGET for Number 8
        self.btnN8 = Button(win, text="8", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN8.grid(row=3, column=1)
        self.btnN8.bind('<Button-1>', self.N8)

        # BUTTON WIDGET for Number 9
        self.btnN9 = Button(win, text="9", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN9.grid(row=3, column=2)
        self.btnN9.bind('<Button-1>', self.N9)

        # BUTTON WIDGET for Number 0
        self.btnN0 = Button(win, text="0", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="white", bg="#333333")
        self.btnN0.grid(row=6, column=0, padx=5, pady=5)
        self.btnN0.bind('<Button-1>', self.N0)

        # BUTTON WIDGET for exponent
        self.btnpwr = Button(win, text="^", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="black",
                             bg="#a9a9a9")
        self.btnpwr.grid(row=2, column=2, padx=5, pady=5)
        self.btnpwr.bind('<Button-1>', self.pwr)

        # BUTTON WIDGET for delete/backspace
        self.btnbck = Button(win, text="←", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="black",
                             bg="#a9a9a9")
        self.btnbck.bind('<Button-1>', self.bck)
        self.btnbck.grid(row=1, column=2)

        # BUTTON WIDGET for open parenthesis
        self.btnoph = Button(win, text="(", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="black",
                             bg="#a9a9a9")
        self.btnoph.grid(row=2, column=0, padx=5, pady=5)
        self.btnoph.bind('<Button-1>', self.oph)

        # BUTTON WIDGET for close parenthesis
        self.btncph = Button(win, text=")", width=3, font=("Century Gothic", 18, "bold"), bd=0, fg="black",
                             bg="#a9a9a9")
        self.btncph.grid(row=2, column=1)
        self.btncph.bind('<Button-1>', self.cph)

    # -----------------------------------------------------------------------------------------------------------------------
    #                   ---- FUNCTION FOR ADDING PRESSED BUTTONS TO THE EQUATION ----
    def press(self, num):
        self.val = self.val + str(num)
        self.equation.set(self.val)

    #                   ---- FUNCTION FOR EQUAL SIGN ----
    def eql(self, eql):
        try:
            self.val = self.val.replace("^", "**")
            total = str(eval(self.val))
            self.equation.set(total)
            self.val = total

        # if the entered equation is invalid
        except:
            self.equation.set(" error ")
            self.val = ""

    #                   ---- FUNCTION FOR CLEAR ----
    def clr(self, clr):
        self.val = ""
        self.equation.set("0")

    #                   ---- FUNCTION FOR DELETE ----
    def bck(self, bck):
        self.val = self.val.rstrip(self.val[-1])
        self.equation.set(self.val)

    #                   ---- FUNCTIONS FOR BASIC OPERATIONS ----
    def add(self, add):
        self.press("+")

    def sub(self, sub):
        self.press("-")

    def mul(self, mul):
        self.press("*")

    def div(self, div):
        self.press("/")

    def dec(self, dec):
        self.press(".")

    #                   ---- FUNCTIONS FOR OTHER OPERATIONS ----
    def pwr(self, pwr):
        self.val = self.val + str("^")
        self.equation.set(self.val)

    def oph(self, oph):
        self.press("(")

    def cph(self, cph):
        self.press(")")

    #                   ---- FUNCTIONS FOR NUMBERS ----
    def N0(self, N0):
        self.press(0)

    def N1(self, N1):
        self.press(1)

    def N2(self, N2):
        self.press(2)

    def N3(self, N3):
        self.press(3)

    def N4(self, N4):
        self.press(4)

    def N5(self, N5):
        self.press(5)

    def N6(self, N6):
        self.press(6)

    def N7(self, N7):
        self.press(7)

    def N8(self, N8):
        self.press(8)

    def N9(self, N9):
        self.press(9)


window = Tk()
mywin = MyWindow(window)

#                   ---- WINDOW CONFIGURATIONS ----
window.geometry("222x370")
window.title("Calculator")
window.eval('tk::PlaceWindow . center')
window.configure(bg="#000000")

window.mainloop()
