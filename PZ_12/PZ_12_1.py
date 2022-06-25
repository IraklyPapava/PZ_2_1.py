# Вариант 16
# column - столбец
# row - строка
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox   # выбор
from tkinter.ttk import Checkbutton   # галочка
from tkinter.font import Font

window = Tk()

window.title("Мой интерфейс")   # это заголовок
window.geometry("900x560")   # это размер окна

RamkaA = Frame(window, width=900, height=30, bg="#699")
RamkaA.grid(column=0, row=0, columnspan=9, sticky=W)

RamkaB = Frame(window, width=900, height=80, bg="#ccc")
RamkaB.grid(column=0, row=12, columnspan=9, rowspan=9, sticky=W)

my_FontZ = Font(family="Arial Bold", size=13, weight="bold")   # для заголовка
my_Font = Font(family="Arial Bold", size=10, weight="bold")   # для жирного текста
my_FontD = Font(family="Arial Bold", size=10, underline=1)   # для подчеркнутого текста

combo1 = Combobox(window)
combo2 = Combobox(window, width=25)
combo3 = Combobox(window, width=25)
combo4 = Combobox(window, width=25)

# ТЕКСТ
lblTitle = Label(window, text="Workshop Registration", bg="#699", font=my_FontZ, padx=3)
lblTitle.grid(column=0, row=0, sticky=W)

lblRegister = Label(window, text="Register now while seats are available!", font=my_FontD, pady=13, padx=3)
lblRegister.grid(column=0, row=1, sticky=W)

lblFirstN = Label(window, text="First Name *", font=my_Font, pady=11, padx=3)
lblFirstN.grid(column=0, row=2, sticky=W)

lblLastN = Label(window, text="Last Name *", font=my_Font, pady=11, padx=3)
lblLastN.grid(column=0, row=3, sticky=W)

lblComp = Label(window, text="Company/Institution *", font=my_Font, pady=11, padx=3)
lblComp.grid(column=0, row=4, sticky=W)

lblAdr = Label(window, text="Address *", font=my_Font, pady=11, padx=3)
lblAdr.grid(column=0, row=5, sticky=W)

lblCity = Label(window, text="City", font=my_Font, pady=11, padx=3)
lblCity.grid(column=0, row=6, sticky=W)

lblState = Label(window, text="State / Province / Region", font=my_Font, pady=11, padx=3)
lblState.grid(column=0, row=7, sticky=W)

lblCountry = Label(window, text="Country", font=my_Font, pady=11, padx=3)
lblCountry.grid(column=0, row=8, sticky=W)

lblEmail = Label(window, text="Email *", font=my_Font, pady=11, padx=3)
lblEmail.grid(column=0, row=9, sticky=W)

lblPhone = Label(window, text="Phone Number *", font=my_Font, pady=11, padx=3)
lblPhone.grid(column=0, row=10, sticky=W)

lblLunch = Label(window, text="Lunch", font=my_FontD, pady=11, padx=25)
lblLunch.grid(column=3, row=1, sticky=W)

lblMeal = Label(window, text="Meal Preference", font=my_Font, pady=11, padx=25)
lblMeal.grid(column=3, row=2, sticky=W)

lblPayD = Label(window, text="Payment Details", font=my_FontD, pady=11, padx=25)
lblPayD.grid(column=3, row=3, sticky=W)

lblPayM = Label(window, text="Payment Mode", font=my_Font, pady=11, padx=25)
lblPayM.grid(column=3, row=4, sticky=W)

lblDD = Label(window, text="DD/Cheque No.", font=my_Font, pady=11, padx=25)
lblDD.grid(column=3, row=7, sticky=W)

lblDraw = Label(window, text="Drawn On (Bank Name)", font=my_Font, pady=11, padx=25)
lblDraw.grid(column=3, row=8, sticky=W)

lblPay = Label(window, text="Payable at", font=my_Font, pady=11, padx=25)
lblPay.grid(column=3, row=9, sticky=W)

lblPus1 = Label(window, text="")
lblPus1.grid(column=0, row=10, sticky=W)

lblPus2 = Label(window, text="")
lblPus2.grid(column=0, row=11, sticky=W)


# ПОЛЕ У ТЕКСТА
textFirstN = Entry(window, width=28)
textFirstN.grid(column=1, row=2, sticky=W)

textLastN = Entry(window, width=28)
textLastN.grid(column=1, row=3, sticky=W)

textComp = Entry(window, width=28)
textComp.grid(column=1, row=4, sticky=W)

textAdr = Text(window, height=5, width=21)
textAdr.grid(column=1, row=5, sticky=W)

textCity = Entry(window, width=28)
textCity.grid(column=1, row=6, sticky=W)

textEmail = Entry(window, width=28)
textEmail.grid(column=1, row=9, sticky=W)

textPhone = Entry(window, width=28)
textPhone.grid(column=1, row=10, sticky=W)

textDD = Entry(window, width=28)
textDD.grid(column=4, row=7, sticky=W)

textDraw = Entry(window, width=28)
textDraw.grid(column=4, row=8, sticky=W)

textPay = Entry(window, width=28)
textPay.grid(column=4, row=9, sticky=W)


# ВЫПАДАЮЩИЙ СПИСОК
combo1['values'] = ("More Actions", "Action1", "Action2", "Action3", "Action4", "Action5")
combo1.current(0)
combo1.grid(column=1, row=0)

combo2['values'] = ("-Select-", "-Select1-", "-Select2-", "-Select3-", "-Select4-")
combo2.current(0)
combo2.grid(column=1, row=7, sticky=W)

combo3['values'] = ("-Select-", "-Select1-", "-Select2-", "-Select3-", "-Select4-")
combo3.current(0)
combo3.grid(column=1, row=8, sticky=W)

combo4['values'] = ("Vegetarian", "Bland Meal", "Kosher", "Hindu", "Seafood Meal")
combo4.current(0)
combo4.grid(column=4, row=2, sticky=W)


# ГАЛОЧКА
chk1 = BooleanVar()
chk1.set(False)
cash = Checkbutton(window, text="Cash", var=chk1)
cash.grid(column=4, row=4, sticky=W)

chk2 = BooleanVar()
chk2.set(False)
cheque = Checkbutton(window, text="Cheque", var=chk1)
cheque.grid(column=4, row=5, sticky=W)

chk3 = BooleanVar()
chk3.set(False)
demand = Checkbutton(window, text="Demand Draft", var=chk1)
demand.grid(column=4, row=6, sticky=W)


# КНОПКИ
btnS = Button(window, text="Submit", bg="#699", fg="white", font=my_Font, width=8, height=1, padx=1)
btnS.grid(column=1, row=12, sticky=SE, padx=1)

btnR = Button(window, text="Reset", bg="#699", fg="white", font=my_Font, width=8, height=1, padx=1)
btnR.grid(column=2, row=12, sticky=SE, padx=1)

window.resizable(width=False, height=False)   # нельзя менять размер окна

window.mainloop()  # запуск постоянного цикла
