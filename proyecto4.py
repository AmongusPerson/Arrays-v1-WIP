from tkinter import *
pg = Tk()
pg.geometry("500x500")
pg.title("Arrays")
pg.configure(background="#264653")

lb1 = Label(pg, text="Proyecto de Arrays", bg="#e76f51", fg="white", font=200)
lb1.place(relx=0.5, rely=0.04, anchor=CENTER,)

lb2 = Label(pg, text=".", bg="#2a9d8f", fg="white", font=200)
lb2.place(relx=0.5, rely=0.11, anchor=CENTER,)

lb3 = Label(pg, text=".", bg="#2a9d8f", fg="white", font=200)
lb3.place(relx=0.5, rely=0.18, anchor=CENTER,)

lb4 = Label(pg, text=".", bg="#2a9d8f", fg="white", font=200)
lb4.place(relx=0.5, rely=0.32, anchor=CENTER,)


meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

def fn1():
    lb2["text"] = meses
    lb3["text"] = numeros
    vr1 = max(numeros)
    vr1 = numeros.index(vr1)
    vr2 = meses[vr1]+numeros[vr1]
    lb4["text"] = meses[vr1]
    lb4["text"] = lb4["text"] + numeros[vr1]
    
bt1 = Button(pg, text="Ejecutar", bg="#e76f51", fg="white", command=fn1)
bt1.place(relx=0.5, rely=0.25, anchor=CENTER,)

pg.mainloop()