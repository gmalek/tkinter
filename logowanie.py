import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo







import tkinter
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter.messagebox import showinfo

def frameWidth(event):
        canvas_width = event.width
        canvas.itemconfig(canvas_frame, width = canvas_width)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def otwieraNoweOkno():
    global okno
    okno = Tk()
    okno.geometry("1024x500")
    okno.resizable(False, False)

    panel = ttk.PanedWindow(okno, orient=HORIZONTAL)
    panel.pack(fill=BOTH, expand=True)

    ramka1 = ttk.Frame(panel, width=100, height=200, relief=SUNKEN, padding=5)
    global canvas
    canvas = Canvas(panel, width=200, height=200, relief=SUNKEN, borderwidth=0)

    global ramka2
    ramka2 = ttk.Frame(canvas, padding=5)
    ramka2.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    vsb = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    canvas.bind('<Configure>', frameWidth)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    global canvas_frame
    canvas_frame = canvas.create_window((0,0),window=ramka2, anchor="nw")

    panel.add(ramka1, weight=1)
    panel.add(canvas, weight=3)


    ttk.Label(ramka1, text="First Name").grid(column=0, row=0)
    ttk.Button(ramka1, text="Pobierz dane", command=pobierzDane).grid(column=0, row=1)
    ttk.Button(ramka1, text="Dodaj użytkownika", command=dodajUzytkownika).grid(column=0, row=2)
    ttk.Button(ramka1, text="Usun użytkownia", command=usunUzytkownika).grid(column=0, row=3)
    ttk.Button(ramka1, text="Edytuj użytkownia", command=edytujUzytkownika).grid(column=0, row=4)

    okno.mainloop()


def pobierzDane():
    clear_frame()
    polaczenie = pymysql.connect(host="localhost", user="root", password="", db="dane")
    cursor = polaczenie.cursor()
    zapytanie = "select * from users;"

    cursor.execute(zapytanie)
    wynik = cursor.fetchall()

    wiersz = 2
    for i in wynik:

        kolumna = 0

        for x in i:
            ttk.Label(ramka2, width=10, text=x, borderwidth=2, relief='ridge').grid(row=wiersz, column=kolumna)
            kolumna+=1
        wiersz+=1

def zapisz():

    login = l1.get()
    haslo = h1.get()


    if login and haslo:
        polaczenie = pymysql.connect(host="localhost", user="root", password="", db="dane")
        cursor = polaczenie.cursor()
        zapytanie = f"insert into users values(111,\"{login}\",\"{haslo}\");"

        cursor.execute(zapytanie)
        polaczenie.commit()



def zapiszUser():
    user = u1.get()

    if user:
        user = u1.get()
        polaczenie = pymysql.connect(host="localhost", user="root", password="", db="dane")
        cursor = polaczenie.cursor()
        zapytanie = f"delete from users where login=\"{user}\";"

        print(zapytanie)

        cursor.execute(zapytanie)
        polaczenie.commit()


def dodajUzytkownika():
    clear_frame()
    ttk.Label(ramka2, width=10, text="login").grid(row=2, column=0)
    global l1
    l1 = ttk.Entry(ramka2)
    l1.grid(row=2, column=1)

    ttk.Label(ramka2, width=10, text="hasło").grid(row=3, column=0)
    global h1
    h1 = ttk.Entry(ramka2)
    h1.grid(row=3, column=1)

    ttk.Button(ramka2, text="Zapisz", command=zapisz).grid(column=1, row=4)

def usunUzytkownika():
    clear_frame()
    ttk.Label(ramka2, width=10, text="Podaj login użytkownika").grid(row=1, column=0)

    global u1
    u1 = ttk.Entry(ramka2)
    u1.grid(row=2, column=1)

    ttk.Button(ramka2, text="Zapisz", command=zapiszUser).grid(column=1, row=4)


def zmienUser():
    login = wybranyLogin.get()
    haslo = wybraneHaslo.get()


    polaczenie = pymysql.connect(host="localhost", user="root", password="", db="dane")
    cursor = polaczenie.cursor()
    zapytanie = f"update users set login=\"{login}\", haslo=\"{haslo}\" where login=\"{login}\";"

    cursor.execute(zapytanie)
    if polaczenie.commit()==None:
        pokazOkno("Hasło zmienione")

def pokazOkno(komunikat="Witaj w tkinter"):
    tk.messagebox.showinfo("Komunikat", komunikat)


def edytujUzytkownika():
    clear_frame()
    # create a list box
    dane = ('Java', 'C#', 'C', 'C++', 'Python',
             'Go', 'JavaScript', 'PHP', 'Swift')

    dane_zmienione = tk.StringVar(value=dane)

    listbox = tk.Listbox(
        ramka2,

        height=6,
        selectmode='extended')

    polaczenie = pymysql.connect(host="localhost", user="root", password="", db="dane")
    cursor = polaczenie.cursor()
    zapytanie = "select * from users;"

    cursor.execute(zapytanie)
    wynik = cursor.fetchall()

    for i in range(len(wynik)):
        listbox.insert(i, wynik[i][1])


    listbox.grid(column=0,row=1,sticky='nwes')


    global wybranyLogin, wybraneHaslo
    ttk.Label(ramka2, width=10, text="Wybrany login").grid(row=2, column=0)
    wybranyLogin = ttk.Entry(ramka2)
    wybranyLogin.grid(row=2, column=1)

    ttk.Label(ramka2, width=10, text="Hasło").grid(row=2, column=2)
    wybraneHaslo = ttk.Entry(ramka2)
    wybraneHaslo.grid(row=2, column=3)

    ttk.Button(ramka2, text="Zapisz", command=zmienUser).grid(column=1, row=4)





    def wybor_loginu(event):
        global wybrany_login, kopiaWybranyLogin
        kopiaWybranyLogin=None

        selected_indices = listbox.curselection()

        wybrany_login = ",".join([listbox.get(i) for i in selected_indices])
        msg = f'Wybrałeś użytkownika: {wybrany_login}'


        wybranyLogin.delete(0,END)

        wybranyLogin.insert(0,wybrany_login)
        kopiaWybranyLogin = wybrany_login
        showinfo(
            title='Information',
            message=msg)

    listbox.bind('<<ListboxSelect>>', wybor_loginu)





def clear_frame():
   for widgets in ramka2.winfo_children():
      widgets.destroy()
