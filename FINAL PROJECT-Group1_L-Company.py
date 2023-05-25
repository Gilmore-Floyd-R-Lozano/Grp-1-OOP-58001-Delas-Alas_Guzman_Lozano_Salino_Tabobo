"""FINAL PROJECT     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
from tkinter import *
from PIL import ImageTk, Image  # use this to import more image file type like jpeg, etc.
from tkinter.messagebox import showinfo
import statistics
from collections import Counter
import datetime
import math

#                   ----   HOME WINDOW CONFIGURATION   -----
Win = Tk()
Win.title("CPE BUDDY")

# Setting window size
Window_Width = 900
Window_Height = 600

# calculate coordination of screen and window form
positionRight = int(Win.winfo_screenwidth() / 2 - Window_Width / 2)
positionDown = int(Win.winfo_screenheight() / 2 - Window_Height / 2)

# Set window in center screen.          --> resulting to    HomeWin.geometry("900x600,+n+n")
Win.geometry(str(Window_Width) + "x" + str(Window_Height) + "+" + str(positionRight) + "+" + str(positionDown))
# -----------------------------------------------------------------------------------------
# Just put r before your normal string. It converts a normal string to a raw string:
# place the images in the same folder as the python file
home_icon = Image.open(r"Home_Icon.png")
mmw_icon = Image.open(r"MMW_ICON.png")
pfe_icon = Image.open(r"PFE_ICON.png")
back_icon = Image.open(r"BACK_ICON.svg.png")
questionMark_icon = Image.open(r"QuestionMark_Icon.png")
lozano_pic = Image.open(r"LOZANO.png")
tabobo_pic = Image.open(r"TABOBO.png")
delasalas_pic = Image.open(r"DELASALAS.jpg")
guzman_pic = Image.open(r"GUZMAN.png")
background = Image.open(r"BACKGROUND.png")
mmw_icon2 = Image.open(r"MMW_ICON2.png")
salino_pic = Image.open(r"SALINO.png")

# to resize image
# ANTI-ALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use LANCZOS or Resampling.LANCZOS instead.
resized_home_icon = home_icon.resize((50, 50), Image.LANCZOS)
resized_mmw_icon = mmw_icon.resize((200, 200), Image.LANCZOS)
resized_pfe_icon = pfe_icon.resize((500, 200), Image.LANCZOS)
resized_back_icon = back_icon.resize((50, 50), Image.LANCZOS)
resized_questionMark_Icon = questionMark_icon.resize((50, 50), Image.LANCZOS)
resized_lozano_pic = lozano_pic.resize((125, 125), Image.LANCZOS)
resized_tabobo_pic = tabobo_pic.resize((125, 125), Image.LANCZOS)
resized_delasalas_pic = delasalas_pic.resize((125, 125), Image.LANCZOS)
resized_guzman_pic = guzman_pic.resize((125, 125), Image.LANCZOS)
resized_background = background.resize((900, 600), Image.LANCZOS)
resized_mmw_icon2 = mmw_icon2.resize((500, 200), Image.LANCZOS)
resized_salino_pic = salino_pic.resize((125, 125), Image.LANCZOS)

HOME_ICON = ImageTk.PhotoImage(resized_home_icon)
MMW_ICON = ImageTk.PhotoImage(resized_mmw_icon)
PFE_ICON = ImageTk.PhotoImage(resized_pfe_icon)
BACK_ICON = ImageTk.PhotoImage(resized_back_icon)
INST_ICON = ImageTk.PhotoImage(resized_questionMark_Icon)
LOZANO_PIC = ImageTk.PhotoImage(resized_lozano_pic)
TABOBO_PIC = ImageTk.PhotoImage(resized_tabobo_pic)
DELASALAS_PIC = ImageTk.PhotoImage(resized_delasalas_pic)
GUZMAN_PIC = ImageTk.PhotoImage(resized_guzman_pic)
BACKGROUND = ImageTk.PhotoImage(resized_background)
MMW_ICON2 = ImageTk.PhotoImage(resized_mmw_icon2)
SALINO_PIC = ImageTk.PhotoImage(resized_salino_pic)


def Home():
    frame = Frame(Win, width=900, height=600)
    frame.place(x=0, y=0)

    canvas = Canvas(frame, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnPFE = Button(frame, image=PFE_ICON, text="PHYSICS FOR ENGINEERS", command=PFE, bg="white")
    btnPFE.place(x=200, y=100)
    btnMMW = Button(frame, image=MMW_ICON2, text="MATHEMATICS IN THE MODERN WORLD", command=MMW)
    btnMMW.place(x=200, y=350)
    btnAbout = Button(frame, text="ABOUT", command=ABT)
    btnAbout.place(x=840, y=560)


def PFE():
    frame_PFE = Frame(Win, width=900, height=600)
    frame_PFE.place(x=0, y=0)

    canvas = Canvas(frame_PFE, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnHome = Button(frame_PFE, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    btnLinear_Motion = Button(frame_PFE, text="Linear Motion Calculator", width=40, height=6, command=Linear_Motion)
    btnLinear_Motion.place(x=120, y=225)
    btnProjectile_Motion = Button(frame_PFE, text="Projectile Motion Calculator", width=40, height=6,
                                  command=Projectile_Motion)
    btnProjectile_Motion.place(x=500, y=225)


def Linear_Motion():
    frame_Linear_Motion = Frame(Win, width=900, height=600)
    frame_Linear_Motion.place(x=0, y=0)

    canvas = Canvas(frame_Linear_Motion, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnBack = Button(frame_Linear_Motion, image=BACK_ICON, command=PFE, bd=0, bg="white")
    btnBack.place(x=785, y=545)

    btnHome = Button(frame_Linear_Motion, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    lblTitle = Label(frame_Linear_Motion, text="Linear Motion Calculator", font=("Helvetica", 30), bg='#8DD7FE',
                     justify=RIGHT)
    lblDisplacement = Label(frame_Linear_Motion, text="Displacement:", font=("Helvetica", 20), bg='#8DD7FE',
                            justify=RIGHT)
    lblFinalVelocity = Label(frame_Linear_Motion, text="Final Velocity:", font=("Helvetica", 20), bg='#8DD7FE',
                             justify=RIGHT)
    lblTime = Label(frame_Linear_Motion, text="Time Elapsed:", font=("Helvetica", 20), bg='#8DD7FE', justify=RIGHT)
    lblAcceleration = Label(frame_Linear_Motion, text="Acceleration:", font=("Helvetica", 20), bg='#8DD7FE',
                            justify=RIGHT)
    lblInitialVelocity = Label(frame_Linear_Motion, text="Initial Velocity:", font=("Helvetica", 20), bg='#8DD7FE',
                               justify=RIGHT)
    entDisplacement = Entry(frame_Linear_Motion, width=16, font=("Helvetica", 20))
    entFinalVelocity = Entry(frame_Linear_Motion, width=16, font=("Helvetica", 20))
    entTime = Entry(frame_Linear_Motion, width=16, font=("Helvetica", 20))
    entAcceleration = Entry(frame_Linear_Motion, width=16, font=("Helvetica", 20))
    entInitialVelocity = Entry(frame_Linear_Motion, width=16, font=("Helvetica", 20))

    lblTitle.place(x=250, y=50)
    lblDisplacement.place(x=200, y=110)
    entDisplacement.place(x=450, y=120)
    lblFinalVelocity.place(x=200, y=190)
    entFinalVelocity.place(x=450, y=200)
    lblTime.place(x=200, y=270)
    entTime.place(x=450, y=280)
    lblAcceleration.place(x=200, y=350)
    entAcceleration.place(x=450, y=360)
    lblInitialVelocity.place(x=200, y=430)
    entInitialVelocity.place(x=450, y=440)

    def Instructions():
        showinfo(title="INSTRUCTIONS",
                 message="Please enter proper values. \nOnly use numbers and decimal point \nEnter the values in SI "
                         "unit: \n\tvelocity: meters per second (m/s)\n\ttime: seconds (s)\n\tdisplacement: meters ("
                         "m)\n\tacceleration: meters per second squared (m/s\u00B2)")

    def clear():
        entDisplacement.delete(0, END)
        entFinalVelocity.delete(0, END)
        entTime.delete(0, END)
        entAcceleration.delete(0, END)
        entInitialVelocity.delete(0, END)

    def calculate():
        Displacement = entDisplacement.get()
        FinalVelocity = entFinalVelocity.get()
        Time = entTime.get()
        Acceleration = entAcceleration.get()
        InitialVelocity = entInitialVelocity.get()

        try:
            if FinalVelocity != "" and InitialVelocity != "" and Displacement != "" and Time != "" and Acceleration != "":
                showinfo(message="Nothing is to be solved. PLease leave an empty field")
            elif FinalVelocity == "" and InitialVelocity == "" and Displacement == "" and Time == "" and Acceleration == "":
                showinfo(message="All fields are empty")
            if FinalVelocity == "":
                if InitialVelocity != "" and Acceleration != "" and Time != "" and Time != "x":
                    FinalVelocity = round(float(InitialVelocity) + float(Acceleration) * float(Time), 2)

                elif InitialVelocity != "" and Acceleration != "" and Displacement != "":
                    FinalVelocity = round(
                        math.sqrt(float(InitialVelocity) ** 2 + 2 * float(Acceleration) * float(Displacement)), 2)

                elif InitialVelocity != "" and Displacement != "" and Time != "":
                    FinalVelocity = round(float(Displacement) / float(Time) * 2 - float(InitialVelocity), 2)

                entFinalVelocity.insert(0, (str(FinalVelocity) + " m/s"))

            if InitialVelocity == "":
                if FinalVelocity != "" and Acceleration != "" and Time != "":
                    InitialVelocity = round(float(FinalVelocity) - float(Acceleration) * float(Time), 2)

                elif Displacement != "" and Acceleration != "" and Time != "":
                    InitialVelocity = round(
                        (float(Displacement) - 0.5 * float(Acceleration) * float(Time) ** 2) / float(Time), 2)

                elif FinalVelocity != "" and Acceleration != "" and Displacement != "":
                    try:
                        InitialVelocity = round(
                            math.sqrt((float(FinalVelocity) ** 2) - 2 * float(Acceleration) * float(Displacement)), 2)
                    except:
                        showinfo(message="The given data is not solvable.")
                        # the result is an imaginary number
                elif FinalVelocity != "" and Displacement != "" and Time != "":
                    InitialVelocity = round(float(Displacement) / float(Time) * 2 - float(FinalVelocity), 2)

                entInitialVelocity.insert(0, (str(InitialVelocity) + " m/s"))

            if Displacement == "":
                if InitialVelocity != "" and Time != "" and Acceleration != "":
                    Displacement = round(
                        float(InitialVelocity) * float(Time) + 0.5 * float(Acceleration) * (float(Time) ** 2), 2)

                elif FinalVelocity != "" and InitialVelocity != "" and Acceleration != "":
                    Displacement = round(
                        (float(FinalVelocity) ** 2 - float(InitialVelocity) ** 2) / (2 * float(Acceleration)), 2)

                elif FinalVelocity != "" and InitialVelocity != "" and Time != "":
                    Displacement = round((float(Time) * (float(FinalVelocity) + float(InitialVelocity))) / 2, 2)

                entDisplacement.insert(0, (str(Displacement) + " m"))

            if Acceleration == "":
                if FinalVelocity != "" and InitialVelocity != "" and Time != "" and Displacement == "x":
                    Acceleration = round((float(FinalVelocity) - float(InitialVelocity)) / float(Time), 2)

                elif InitialVelocity != "" and Displacement != "" and Time != "" and Acceleration != "x":
                    Acceleration = round(
                        2 * ((float(Displacement)) / float(Time) ** 2) - (float(InitialVelocity) / float(Time)), 2)

                elif FinalVelocity != "" and InitialVelocity != "" and Displacement != "":
                    Acceleration = round(
                        (float(FinalVelocity) ** 2 - float(InitialVelocity) ** 2) / (2 * float(Displacement)), 2)

                entAcceleration.insert(0, (str(Acceleration) + " m/s\u00B2 "))  # unicode for superscript of number 2

            if Time == "":
                if FinalVelocity != "" and InitialVelocity != "" and Acceleration != "" and Acceleration != "x":
                    Time = round((float(FinalVelocity) - float(InitialVelocity)) / float(Acceleration), 2)

                elif InitialVelocity != "" and Acceleration != "" and Displacement != "" and Acceleration != "x":
                    try:
                        Time = round((-float(InitialVelocity) + math.sqrt(
                            (2 * float(Displacement) * float(Acceleration)) + float(InitialVelocity) ** 2)) / float(
                            Acceleration), 2)
                    except:
                        Time = round((-float(InitialVelocity) - math.sqrt(
                            (2 * float(Displacement) * float(Acceleration)) + float(InitialVelocity) ** 2)) / float(
                            Acceleration), 2)
                elif FinalVelocity != "" and InitialVelocity != "" and Displacement != "":
                    Time = round(2 * float(Displacement) / (float(FinalVelocity) + float(InitialVelocity)), 2)

                entTime.insert(0, (str(Time) + " s"))

        except:
            showinfo(message="Please enter proper values")

    instructions_button = Button(frame_Linear_Motion, image=INST_ICON, command=Instructions)
    instructions_button.place(x=5, y=540)
    clear_button = Button(frame_Linear_Motion, text="Clear", width=25, height=2, command=clear)
    clear_button.place(x=200, y=490)
    calculate_button = Button(frame_Linear_Motion, text="Calculate", width=34, height=2, command=calculate)
    calculate_button.place(x=450, y=490)

    Instructions()


def Projectile_Motion():
    frame_Projectile_Motion = Frame(Win, width=900, height=600)
    frame_Projectile_Motion.place(x=0, y=0)

    canvas = Canvas(frame_Projectile_Motion, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnBack = Button(frame_Projectile_Motion, image=BACK_ICON, command=PFE, bd=0, bg="white")
    btnBack.place(x=785, y=545)

    btnHome = Button(frame_Projectile_Motion, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    lblTitle = Label(frame_Projectile_Motion, text="Projectile Motion Calculator", font=("Helvetica", 30), bg='#8DD7FE',
                     justify=RIGHT)
    lblInitialVelocity = Label(frame_Projectile_Motion, text="Initial Velocity:", bg='#8DD7FE', font=("Helvetica", 20),
                               justify=RIGHT)
    lblAngle = Label(frame_Projectile_Motion, text="Angle:", bg='#8DD7FE', font=("Helvetica", 20), justify=RIGHT)
    lblRange = Label(frame_Projectile_Motion, text="Range:", bg='#8DD7FE', font=("Helvetica", 20), justify=RIGHT)
    lblTime = Label(frame_Projectile_Motion, text="Time of flight:", bg='#8DD7FE', font=("Helvetica", 20),
                    justify=RIGHT)
    lblMaxHeight = Label(frame_Projectile_Motion, text="Max Height:", bg='#8DD7FE', font=("Helvetica", 20),
                         justify=RIGHT)
    entInitialVelocity = Entry(frame_Projectile_Motion, width=16, font=("Helvetica", 20))
    entAngle = Entry(frame_Projectile_Motion, width=16, font=("Helvetica", 20))
    entRange = Entry(frame_Projectile_Motion, width=16, font=("Helvetica", 20))
    entTime = Entry(frame_Projectile_Motion, width=16, font=("Helvetica", 20))
    entMaxHeight = Entry(frame_Projectile_Motion, width=16, font=("Helvetica", 20))

    lblTitle.place(x=220, y=50)
    lblInitialVelocity.place(x=230, y=120)
    entInitialVelocity.place(x=450, y=120)
    lblAngle.place(x=230, y=200)
    entAngle.place(x=450, y=200)
    lblRange.place(x=230, y=280)
    entRange.place(x=450, y=280)
    lblTime.place(x=230, y=360)
    entTime.place(x=450, y=360)
    lblMaxHeight.place(x=230, y=440)
    entMaxHeight.place(x=450, y=440)

    def Instructions():
        showinfo(title="INSTRUCTIONS",
                 message="Please enter proper values. \nOnly use numbers and decimal point \nEnter the values in SI "
                         "unit: \n\tInitial Velocity: meters per second (m/s)\n\tAngle: degrees (\u00B0)")

    def calculate():
        entTime.delete(0, END)
        entRange.delete(0, END)
        entMaxHeight.delete(0, END)
        InitialVelocity = entInitialVelocity.get()
        Angle = entAngle.get()

        try:
            Range = round((float(InitialVelocity) ** 2 * math.sin(math.radians(2 * float(Angle)))) / 9.8, 2)
            entRange.insert(0, (str(Range) + " m"))

            Time = round(2 * float(InitialVelocity) * math.sin(math.radians(float(Angle))) / 9.8, 2)
            entTime.insert(0, (str(Time) + " s"))

            MaxHeight = round(((float(InitialVelocity) ** 2) * (math.sin(math.radians(float(Angle)))) ** 2) / (2 * 9.8),
                              2)
            entMaxHeight.insert(0, (str(MaxHeight) + " m"))

        except:
            showinfo(message="Please enter proper values for initial velocity and angle")

    instructions_button = Button(frame_Projectile_Motion, image=INST_ICON, command=Instructions)
    instructions_button.place(x=5, y=540)
    calculate_button = Button(frame_Projectile_Motion, text="Calculate", width=34, height=2, command=calculate)
    calculate_button.place(x=450, y=500)

    Instructions()


def MMW():
    frame_MMW = Frame(Win, width=900, height=600)
    frame_MMW.place(x=0, y=0)

    canvas = Canvas(frame_MMW, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnHome = Button(frame_MMW, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    btnEO_Time = Button(frame_MMW, text="Exact Time Calculator", width=40, height=6, command=Ext_Time_Calc)
    btnEO_Time.place(x=120, y=125)
    btnSimp_Interest = Button(frame_MMW, text="Simple Interest Calculator", width=40, height=6, command=Simp_Int)
    btnSimp_Interest.place(x=120, y=325)
    btnCentral_Tendencies = Button(frame_MMW, text="Central Tendencies Calculator", width=40, height=6,
                                   command=Cent_Tend)
    btnCentral_Tendencies.place(x=500, y=125)
    btnComp_Interest = Button(frame_MMW, text="Compound Interest Calculator", width=40, height=6, command=Comp_Int)
    btnComp_Interest.place(x=500, y=325)

# ----------------------------------------------------------------------------------------------------------------
def Ext_Time_Calc():
    frame_Ext_Time = Frame(Win, width=900, height=600)
    frame_Ext_Time.place(x=0, y=0)

    canvas = Canvas(frame_Ext_Time, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnBack = Button(frame_Ext_Time, image=BACK_ICON, command=MMW, bd=0, bg="white")
    btnBack.place(x=785, y=545)

    btnHome = Button(frame_Ext_Time, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    lblTitle = Label(frame_Ext_Time, text="Exact Time Calculator", bg='#8DD7FE', font=("Helvetica", 30))
    lblTitle.place(x=275, y=50)
    lblDay = Label(frame_Ext_Time, text="DAY:", bg='#8DD7FE', font=("Helvetica", 20))
    lblDay.place(x=100, y=130)
    lblMonth = Label(frame_Ext_Time, text="MONTH:", bg='#8DD7FE', font=("Helvetica", 20))
    lblMonth.place(x=100, y=230)
    lblYear = Label(frame_Ext_Time, text="YEAR:", bg='#8DD7FE', font=("Helvetica", 20))
    lblYear.place(x=100, y=330)

    start_day_entry = Entry(frame_Ext_Time, width=16, font=("Helvetica", 20))
    start_day_entry.place(x=250, y=130)
    start_month_entry = Entry(frame_Ext_Time, width=16, font=("Helvetica", 20))
    start_month_entry.place(x=250, y=230)
    start_year_entry = Entry(frame_Ext_Time, width=16, font=("Helvetica", 20))
    start_year_entry.place(x=250, y=330)

    end_day_entry = Entry(frame_Ext_Time, width=16, font=("Helvetica", 20))
    end_day_entry.place(x=550, y=130)
    end_month_entry = Entry(frame_Ext_Time, width=16, font=("Helvetica", 20))
    end_month_entry.place(x=550, y=230)
    end_year_entry = Entry(frame_Ext_Time, width=16, font=("Helvetica", 20))
    end_year_entry.place(x=550, y=330)

    def clear():
        start_day_entry.delete(0, END)
        start_month_entry.delete(0, END)
        start_year_entry.delete(0, END)
        end_day_entry.delete(0, END)
        end_month_entry.delete(0, END)
        end_year_entry.delete(0, END)

    def Instructions():
        showinfo(title="Instructions",
                 message="Enter the months and days in numbers.\n\nMonths:\n\t1 (January) - 12 ("
                         "December)\n\nDays:\n\t1 - 31 (Jan, Mar, May, Jul, Aug, Oct, Dec)\n\t1 - 30 (Apr, Jun, Sep, "
                         "Nov)\n\t1 - 28 or 1 - 29 (Feb)")

    def calculate_days():
        try:
            startDate = start_month_entry.get() + "/" + start_day_entry.get() + "/" + start_year_entry.get()
            start_date = datetime.datetime.strptime(startDate, "%m/%d/%Y")

            endDate = end_month_entry.get() + "/" + end_day_entry.get() + "/" + end_year_entry.get()
            end_date = datetime.datetime.strptime(endDate, "%m/%d/%Y")

            days = (end_date - start_date).days
            days_label.config(text=f"Number of days: {days}")

        except:
            showinfo(title="error!", message="Please enter proper values.\nCheck if the values are within the range.")

    days_label = Label(frame_Ext_Time, text="Number of days:", bg='#8DD7FE', font=("Helvetica", 20))
    days_label.place(x=360, y=400)

    instructions_button = Button(frame_Ext_Time, image=INST_ICON, command=Instructions)
    instructions_button.place(x=5, y=540)

    calculate_button = Button(frame_Ext_Time, text="Calculate", width=34, height=3, command=calculate_days)
    calculate_button.place(x=250, y=470)

    clear_button = Button(frame_Ext_Time, text="Clear", width=34, height=3, command=clear)
    clear_button.place(x=550, y=470)

    Instructions()


# -------------------------------------------------------------------------------
def Simp_Int():
    frame_Simp_Int = Frame(Win, width=900, height=600)
    frame_Simp_Int.place(x=0, y=0)

    canvas = Canvas(frame_Simp_Int, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnBack = Button(frame_Simp_Int, image=BACK_ICON, command=MMW, bd=0, bg="white")
    btnBack.place(x=785, y=545)

    btnHome = Button(frame_Simp_Int, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    lblTitle = Label(frame_Simp_Int, text="Simple Interest Calculator", bg='#8DD7FE', font=("Helvetica", 30))
    lblPrincipalAmt = Label(frame_Simp_Int, text="Principal Amount:", bg='#8DD7FE', font=("Helvetica", 20))
    lblRate = Label(frame_Simp_Int, text="Rate of Interest:", bg='#8DD7FE', font=("Helvetica", 20))
    lblTime = Label(frame_Simp_Int, text="Time Period:", bg='#8DD7FE', font=("Helvetica", 20))
    lblInterest = Label(frame_Simp_Int, text="Interest:", bg='#8DD7FE', font=("Helvetica", 20))
    txtPrincipal = Entry(frame_Simp_Int, width=16, font=("Helvetica", 20))
    txtRate = Entry(frame_Simp_Int, width=16, font=("Helvetica", 20))
    txtTime = Entry(frame_Simp_Int, width=16, font=("Helvetica", 20))
    txtInterest = Entry(frame_Simp_Int, width=16, font=("Helvetica", 20))

    lblTitle.place(x=250, y=50)
    lblPrincipalAmt.place(x=230, y=150)
    txtPrincipal.place(x=450, y=150)
    lblRate.place(x=230, y=250)
    txtRate.place(x=450, y=250)
    lblTime.place(x=230, y=350)
    txtTime.place(x=450, y=350)
    lblInterest.place(x=230, y=450)
    txtInterest.place(x=450, y=450)

    def Instructions():
        showinfo(title="Instructions", message="Enter values in three fields to get the result of the empty field")

    def calculate_Interest():
        Principal = txtPrincipal.get()
        Rate = txtRate.get()
        Time = txtTime.get()
        Interest = txtInterest.get()

        if Interest == "" and Principal != "" and Rate != "" and Time != "":
            Interest = round(float(Principal) * (float(Rate) / 100) * float(Time), 2)

            txtInterest.insert(0, str(Interest))

        elif Principal == "" and Interest != "" and Rate != "" and Time != "":
            Principal = round(float(Interest) / ((float(Rate) / 100) * float(Time)), 2)

            txtPrincipal.insert(0, str(Principal))

        elif Rate == "" and Interest != "" and Principal != "" and Time != "":
            Rate = round(100 * float(Interest) / (float(Principal) * float(Time)), 2)

            txtRate.insert(0, str(Rate))

        elif Time == "" and Interest != "" and Principal != "" and Rate != "":
            Time = round(float(Interest) / (float(Principal) * float(Rate) / 100), 2)

            txtTime.insert(0, str(Time))

        elif Interest and Principal and Rate and Time != "":
            showinfo(message="Nothing is to be solved")

        else:
            showinfo(message="Please enter proper values")

    instructions_button = Button(frame_Simp_Int, image=INST_ICON, command=Instructions)
    instructions_button.place(x=5, y=540)

    calculate_button = Button(frame_Simp_Int, text="Calculate", width=33, height=3, command=calculate_Interest)
    calculate_button.place(x=450, y=520)

    Instructions()


# -------------------------------------------------------------------------------
def Comp_Int():
    frame_Comp_Int = Frame(Win, width=900, height=600)
    frame_Comp_Int.place(x=0, y=0)

    canvas = Canvas(frame_Comp_Int, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnBack = Button(frame_Comp_Int, image=BACK_ICON, command=MMW, bd=0, bg="white")
    btnBack.place(x=785, y=545)

    btnHome = Button(frame_Comp_Int, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)
    global compound
    compound = None

    def Instructions():
        showinfo(title="Instructions",
                 message="Enter the principal amount, rate, time and select how many times the interest will be "
                         "compounded in a year to get the amount and interest")

    def Compounding_Time():
        global compound
        compound = str(cmpdTime.get())

    cmpdTime = IntVar()
    rbtQuarterly = Radiobutton(frame_Comp_Int, text="Quarterly", variable=cmpdTime, value=4, bg='#8DD7FE',
                               command=Compounding_Time)
    rbtAnnually = Radiobutton(frame_Comp_Int, text="Annually", variable=cmpdTime, value=1, bg='#8DD7FE',
                              command=Compounding_Time)
    rbtSemiAnnually = Radiobutton(frame_Comp_Int, text="Semi-Annually", variable=cmpdTime, value=2, bg='#8DD7FE',
                                  command=Compounding_Time)
    rbtMonthly = Radiobutton(frame_Comp_Int, text="Monthly", variable=cmpdTime, value=12, bg='#8DD7FE',
                             command=Compounding_Time)
    lblCompounded = Label(frame_Comp_Int, text="Compounded:", bg='#8DD7FE', font=("Helvetica", 20))
    lblTitle = Label(frame_Comp_Int, text="Compound Interest Calculator", bg='#8DD7FE', font=("Helvetica", 30))
    lblPrincipalAmt = Label(frame_Comp_Int, text="Principal Amount:", bg='#8DD7FE', font=("Helvetica", 20))
    lblRate = Label(frame_Comp_Int, text="Rate of Interest:", bg='#8DD7FE', font=("Helvetica", 20))
    lblTime = Label(frame_Comp_Int, text="Time Period:", bg='#8DD7FE', font=("Helvetica", 20))
    lblInterest = Label(frame_Comp_Int, text="Interest:", bg='#8DD7FE', font=("Helvetica", 20))
    lblAmount = Label(frame_Comp_Int, text="Amount:", bg='#8DD7FE', font=("Helvetica", 20))
    txtPrincipal = Entry(frame_Comp_Int, width=16, font=("Helvetica", 20))
    txtRate = Entry(frame_Comp_Int, width=16, font=("Helvetica", 20))
    txtTime = Entry(frame_Comp_Int, width=16, font=("Helvetica", 20))
    txtInterest = Entry(frame_Comp_Int, width=16, font=("Helvetica", 20))
    txtAmount = Entry(frame_Comp_Int, width=16, font=("Helvetica", 20))

    lblTitle.place(x=200, y=50)
    lblPrincipalAmt.place(x=200, y=150)
    txtPrincipal.place(x=480, y=150)
    lblRate.place(x=200, y=200)
    txtRate.place(x=480, y=200)
    lblTime.place(x=200, y=250)
    txtTime.place(x=480, y=250)
    lblInterest.place(x=200, y=450)
    txtInterest.place(x=480, y=450)
    lblAmount.place(x=200, y=500)
    txtAmount.place(x=480, y=500)

    lblCompounded.place(x=200, y=320)
    rbtAnnually.place(x=400, y=320)
    rbtSemiAnnually.place(x=470, y=320)
    rbtQuarterly.place(x=570, y=320)
    rbtMonthly.place(x=650, y=320)

    def calculate_Interest():
        txtAmount.delete(0, END)
        txtInterest.delete(0, END)
        Principal = txtPrincipal.get()
        Rate = txtRate.get()
        Time = txtTime.get()

        if Principal and Rate and Time != "":
            try:
                Amount = float(Principal) * (1 + ((float(Rate) / 100) / float(compound))) ** (
                            float(compound) * float(Time))
                txtAmount.insert(0, str(round(Amount, 2)))
                Interest = Amount - float(Principal)
                txtInterest.insert(0, str(round(Interest, 2)))

            except:
                showinfo(message="Please enter proper values")
                if compound == None:
                    showinfo(message="Select how many times the interest is compounded")

        else:
            showinfo(message="Please enter the values required")

    instructions_button = Button(frame_Comp_Int, image=INST_ICON, command=Instructions)
    instructions_button.place(x=5, y=540)

    calculate_button = Button(frame_Comp_Int, text="Calculate", width=40, height=2, command=calculate_Interest)
    calculate_button.place(x=320, y=380)

    Instructions()


def Cent_Tend():
    frame_Cent_Tend = Frame(Win, width=900, height=600)
    frame_Cent_Tend.place(x=0, y=0)

    canvas = Canvas(frame_Cent_Tend, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnBack = Button(frame_Cent_Tend, image=BACK_ICON, command=MMW, bd=0, bg="white")
    btnBack.place(x=785, y=545)

    btnHome = Button(frame_Cent_Tend, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    lblTitle = Label(frame_Cent_Tend, text="Measures of Central Tendencies", bg='#8DD7FE', font=("Helvetica", 30))
    lblData = Label(frame_Cent_Tend, text="Data:", bg='#8DD7FE', font=("Helvetica", 20))
    lblMean = Label(frame_Cent_Tend, text="Mean:", bg='#8DD7FE', font=("Helvetica", 20))
    lblMedian = Label(frame_Cent_Tend, text="Median:", bg='#8DD7FE', font=("Helvetica", 20))
    lblMode = Label(frame_Cent_Tend, text="Mode:", bg='#8DD7FE', font=("Helvetica", 20))
    entData = Entry(frame_Cent_Tend, width=16, font=("Helvetica", 20))
    entMean = Entry(frame_Cent_Tend, width=16, font=("Helvetica", 20))
    entMedian = Entry(frame_Cent_Tend, width=16, font=("Helvetica", 20))
    entMode = Entry(frame_Cent_Tend, width=16, font=("Helvetica", 20))

    lblTitle.place(x=180, y=50)
    lblData.place(x=230, y=150)
    lblMean.place(x=230, y=310)
    lblMedian.place(x=230, y=410)
    lblMode.place(x=230, y=510)

    entData.place(x=450, y=150)
    entMean.place(x=450, y=310)
    entMedian.place(x=450, y=410)
    entMode.place(x=450, y=510)

    def Instructions():
        showinfo(title="Instructions",
                 message="Enter values separated by space or a comma.\n\nExample: 1 2 3 4 or 1,2,3,4 or 1, 2, 3, 4")

    def calculate_CentralTendencies():
        entMean.delete(0, END)
        entMedian.delete(0, END)
        entMode.delete(0, END)

        data = entData.get()
        data = data.replace(",", " ").split()
        # for x in data:
        data = [int(num) for num in data]
        Mean = round(statistics.mean(data), 2)
        Median = statistics.median(data)

        counter = Counter(data)
        most_common = counter.most_common()
        max_count = most_common[0][1]
        Mode = str([value for value, count in most_common if count == max_count])
        Mode = Mode.strip("[]")  # removes the brackets

        entMean.insert(END, Mean)
        entMedian.insert(END, Median)
        entMode.insert(END, Mode)

    calculate_button = Button(frame_Cent_Tend, text="Calculate", command=calculate_CentralTendencies, width=33,
                              height=3)
    calculate_button.place(x=452, y=200)

    instructions_button = Button(frame_Cent_Tend, image=INST_ICON, command=Instructions)
    instructions_button.place(x=5, y=540)

    Instructions()

# -------------------------------------------------------------------------------
def ABT():
    frame_ABT = Frame(Win, width=900, height=600)
    frame_ABT.place(x=0, y=0)

    canvas = Canvas(frame_ABT, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=BACKGROUND, anchor="nw")

    btnHome = Button(frame_ABT, image=HOME_ICON, command=Home, bd=0, bg="white")
    btnHome.place(x=845, y=545)

    lblTitle = Label(frame_ABT, text="FINAL OUTPUT ", font=("Helvetica", 30), bg='#8DD7FE', ).place(x=300, y=50)
    lblTitle2 = Label(frame_ABT, text="OBJECT ORIENTED PROGRAMMING LAB", font=("Helvetica", 20),
                      bg='#8DD7FE', ).place(x=180, y=125)
    lblTitle3 = Label(frame_ABT, text="58001 TTh 7:00 - 10:00\nEngr. Maria Rizette H. Sayo", font=("Helvetica", 15),
                      bg='#8DD7FE', ).place(x=330, y=175)
    lblInfo = Label(frame_ABT,
                    text="This application is composed of multiple calculators useful for\nMathemathics in the Modern "
                         "World and Physics for Engineers",
                    font=("Helvetica", 15), pady=10,
                    bg='#8DD7FE', ).place(x=180, y=250)
    lblTitle4 = Label(frame_ABT, text="PROPONENTS", font=("Helvetica", 20),
                      bg='#8DD7FE', ).place(x=360, y=350)
    lblLozano_pic = Label(frame_ABT, image=LOZANO_PIC, bd=0).place(x=75, y=400)
    lblTabobo_pic = Label(frame_ABT, image=TABOBO_PIC, bd=0).place(x=230, y=400)
    lblDelasalas_pic = Label(frame_ABT, image=DELASALAS_PIC, bd=0).place(x=385, y=400)
    lblGuzman_pic = Label(frame_ABT, image=GUZMAN_PIC, bd=0).place(x=540, y=400)
    lblSalino_pic = Label(frame_ABT, image=SALINO_PIC, bd=0).place(x=695, y=400)

    lblLozano_name = Label(frame_ABT, text="Gilmore Floyd Lozano", font=("Helvetica", 8), bg="white").place(x=85, y=530)
    lblTabobo_name = Label(frame_ABT, text="John Benedict Tabobo", font=("Helvetica", 8), bg="white").place(x=235,
                                                                                                            y=530)
    lblDelasalas_name = Label(frame_ABT, text="Reuben John Delas Alas ", font=("Helvetica", 8), bg="white").place(x=385,
                                                                                                                  y=530)
    lblGuzman_name = Label(frame_ABT, text="Roel John Guzman", font=("Helvetica", 8), bg="white").place(x=555,
                                                                                                        y=530)
    lblSalino_name = Label(frame_ABT, text="Neil Philipp Salino", font=("Helvetica", 8), bg="white").place(x=715,
                                                                                                           y=530)

Home()
Win.mainloop()
