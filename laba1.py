# 9 + 3 - 10 * 13 + 7
# 2 + 3 * 5 / 2 - 10 / 3, p=23
from tkinter import *

def stepen(a,p):
    avm = 1.1
    b = 1
    while not avm.is_integer():
        avm = (1 + p * b) / a
        b += 1
    return avm

def clicked():
    #vir = input("Введите выражение: ")
    vir = txt.get()
    #p = int(input("Введите поле: "))
    p = txt1.get()
    p = int(p)
    vir = vir.split()
    #print(vir)
    for i in range(len(vir)):
     if vir[i].isalnum():
        vir[i] = int(vir[i])
    while "*" in vir or "/" in vir:
     for i in range(len(vir)):
        if vir[i] == "*":
            vir[i] = (vir[i-1] * vir[i+1]) % p
            vir.remove(vir[i-1])
            vir.remove(vir[i])
            #print(vir, "Выполнил умножение")
            break
        elif vir[i] == "/":
            vir[i] = stepen(vir[i+1],p)
            vir.remove(vir[i - 1])
            vir.remove(vir[i])
            #print(vir, ", выполнил деление")
            break
    while "+" in vir or "-" in vir:
     for i in range(len(vir)):
        if vir[i] == "+":
            vir[i] = (vir[i-1] + vir[i+1]) % p
            vir.remove(vir[i-1])
            vir.remove(vir[i])
            #print(vir, ", выполнил сложение")
            break
        elif vir[i] == "-":
            vir[i] = (vir[i-1] - vir[i+1]) % p
            vir.remove(vir[i - 1])
            vir.remove(vir[i])
            #print(vir, ", выполнил отрицание")
            break
    v = vir[0]
    #print(v)
    #print(v % p)
    txt2.insert(INSERT, v % p)

window = Tk()
window.title("Калькулятор полей")
window.geometry('325x250')
window["bg"] = "pink"

lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=0)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=1)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=2)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=3)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=4)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=5)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=6)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=7)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=8)

lbl1 = Label(window, text="Введите выражение:", bg="pink", font=("Gulim", 14))
lbl1.grid(column=2, row=0)
txt = Entry(window,width=40)
txt.grid(column=2, row=1)
lbl11 = Label(window, text="Введите поле:", bg="pink", font=("Gulim", 14))
lbl11.grid(column=2, row=2)
lbl4 = Label(window, text="Поле должно быть простым числом!!!!", bg="pink", fg="red", font=("Gulim", 7))
lbl4.grid(column=2, row=3)
txt1 = Entry(window,width=10)
txt1.grid(column=2, row=4)

lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=2, row=5)

btn = Button(window, text="Решить", bg="red", command=clicked)
btn.grid(column=2, row=6)

txt2 = Entry(window,width=40)
txt2.grid(column=2, row=8)
window.mainloop()
