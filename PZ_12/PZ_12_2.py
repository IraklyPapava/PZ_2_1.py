# Вариант 16
# column - столбец
# row - строка
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

window = Tk()

window.title("Мой интерфейс")   # заголовок
window.geometry("700x300")   # размер окна

# ЗАДАЧА
def button_command():
    text1 = textText.get()
    text2 = str.title(text1)
    lblO.config(text=text2)
    return None


# ТЕКСТ
lblText1 = Label(window, text="При вводе предложения каждое слово будет начинаться с заглавной буквы", font=("Arial Bold", 13, "bold"), padx=30)
lblText1.grid(column=0, row=0, columnspan=4, sticky=N)

lblText2 = Label(window, text="Если вы введёте число, то программа вернёт вам ваше число!!!", fg="red", font=("Arial Bold", 11), padx=80)
lblText2.grid(column=0, row=2, columnspan=4, sticky=N)

lblP1 = Label(window, text="", font=("Arial Bold", 11), padx=80)
lblP1.grid(column=0, row=1, columnspan=4, sticky=N)

lblP2 = Label(window, text="", font=("Arial Bold", 11), padx=80)
lblP2.grid(column=0, row=3, columnspan=4, sticky=N)

lblP3 = Label(window, text="", font=("Arial Bold", 11), padx=80)
lblP3.grid(column=0, row=5, columnspan=4, sticky=N)

lblP4 = Label(window, text="", font=("Arial Bold", 11), padx=80)
lblP4.grid(column=0, row=7, columnspan=4, sticky=N)

lblO = Label(window, font=("Arial Bold", 11), padx=80)
lblO.grid(column=0, row=8, columnspan=4, sticky=N)


# ПОЛЕ ВВОДА
textText = Entry(window, width=85)
textText.grid(column=0, row=4, columnspan=4, sticky=N)


# КНОПКА
btnV = Button(window, text="Выполнить", bg="#699", fg="white", font=("Arial Bold", 11), width=8, height=1, padx=150, command=button_command)
btnV.grid(column=0, row=6, columnspan=4, sticky=N)


window.resizable(width=False, height=False)   # нельзя менять размер окна

window.mainloop()   # запуск постоянного цикла

