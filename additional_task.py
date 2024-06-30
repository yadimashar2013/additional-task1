# Конвертер единиц измерения:
# Библиотеки: tkinter
# Описание: Приложение с графическим интерфейсом для конвертации различных единиц измерения
# (длина, вес, объем и т.д.).

# импорт tkinter
from tkinter import *
from tkinter import ttk, StringVar, Text

# создаем окно прграммы
window = Tk()
# созданем глобальные переменные
from_users = StringVar(window)
to_users = StringVar(window)


# функция для очистки значений
def clear_all():
    from_users.delete(0, END)
    to_users_mm.delete("1.0", "end")
    to_users_cm.delete("1.0", "end")
    to_users_m.delete("1.0", "end")
    to_users_km.delete("1.0", "end")


# функция выхода из программы
def exit():
    window.destroy()


# функция для вычисления и ввода значений
def converted_users():
    mm = float(from_users.get()) * 1000
    cm = float(from_users.get()) * 100
    dm = float(from_users.get()) * 10
    km = float(from_users.get()) / 1000

    to_users_mm.insert(END, mm)
    to_users_cm.insert(END, cm)
    to_users_m.insert(END, dm)
    to_users_km.insert(END, km)


# создаем заголовок
window.title('Дополнительное задание')
# задаем размер окна
window.geometry('700x400+300+150')
# создаем название программы
heading = ttk.Label(window, text='Приложение для конвертации длины и расстояния', font=("Arial Bold", 13))
heading.pack()
# пункты меню
lbl2 = ttk.Label(window, text='Введите значение исходной величины в метрах', font=("Arial Bold", 11))
lbl2.place(x=50, y=80)

lbl1 = ttk.Label(window, text='Миллиметры', font=("Arial Bold", 11))
lbl1.place(x=50, y=120)

lbl1 = ttk.Label(window, text='Сантиметры', font=("Arial Bold", 11))
lbl1.place(x=50, y=160)

lbl1 = ttk.Label(window, text='Дициметры', font=("Arial Bold", 11))
lbl1.place(x=50, y=200)

lbl1 = ttk.Label(window, text='Километры', font=("Arial Bold", 11))
lbl1.place(x=50, y=240)
# создание поля для ввода исходного значения
from_users = ttk.Entry(window, width=20, textvariable=from_users)
from_users.place(x=500, y=80)
# поля для вывода преобразованных значений
to_users_mm = Text(window, height=1, width=15)
to_users_mm.place(x=500, y=120)

to_users_cm = Text(window, height=1, width=15)
to_users_cm.place(x=500, y=160)

to_users_m = Text(window, height=1, width=15)
to_users_m.place(x=500, y=200)

to_users_km = Text(window, height=1, width=15)
to_users_km.place(x=500, y=240)
# рабочие кнопки
btn = ttk.Button(window, text="Результат", command=converted_users)
btn.place(x=420, y=350)

btn1 = ttk.Button(window, text="Выход", command=exit)
btn1.place(x=580, y=350)

btn2 = ttk.Button(window, text="Сбросить", command=clear_all)
btn2.place(x=500, y=350)
# вывод прграммы
window.mainloop()
# В прцессе проектирования программы использовал инфрмацию с сайтов: https://docs.python.org,
# https://metanit.com, https://pythonru.com, https://pythonpip.ru, https://python-scripts.com.
