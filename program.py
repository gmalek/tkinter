import tkinter as tk
import tkinter.messagebox
import pymysql
from logowanie import otwieraNoweOkno


def wyswietlaNapis():
    print("W konsoli")
    labelZmianaTekstu.config(text="W label")

def pobierzDane():
    print(f"Imie {e1.get()}, nazwisko {e2.get()}")

licznik = 0
def czas(labelLicznik):
    licznik = 0

    def licz():
        global licznik
        licznik+=1
        labelLicznik.config(text=licznik)
        labelLicznik.after(1000,licz)
    licz()

def pokazOkno(komunikat="Witaj w tkinter"):
    tk.messagebox.showinfo("Komunikat", komunikat)

def zamknij():
    master.destroy()

def zaloguj():
    login = e1.get()
    haslo = e2.get()

    if login and haslo:
        polaczenie = pymysql.connect(host="localhost", user="root", password="", db="dane")
        cursor = polaczenie.cursor()
        zapytanie = "select * from users;"

        cursor.execute(zapytanie)
        wynik = cursor.fetchall()

        loginy = []
        for i in wynik:
            loginy.append(i[1])
        if login in loginy:
            print("jest")
            zamknij()
            otwieraNoweOkno()
        else:
            pokazOkno("Nie ma takiego loginu")
    else:
        pokazOkno("Podaj dane")



master = tk.Tk()
master.geometry("500x500")

tk.Label(master, text="First Name").grid(row=0,column=0)
tk.Label(master, text="Last Name").grid(row=1,column=0)

tk.Label(master, text="Czas: ").grid(row=0,column=2)

labelLicznik = tk.Label(master,fg="dark green")
labelLicznik.grid(row=0,column=3)

czas(labelLicznik)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,text="Wyświetl", command=wyswietlaNapis).grid(row=2,column=0)
labelZmianaTekstu = tk.Label(master, text="Tu się zmieni tekst", fg="dark green")
labelZmianaTekstu.grid(row=2, column=1)

tk.Button(master,text="Pokaż dane", command=pobierzDane).grid(row=4,column=0)

tk.Button(master,text="Pokaż komunikat", command=pokazOkno).grid(row=5,column=0)

tk.Button(master,text="Otwórz nowe okno", command=otwieraNoweOkno).grid(row=6,column=0)

tk.Button(master,text="Zaloguj się", command=zaloguj).grid(row=7,column=0)

#tk.Button(master,text="QUIT",fg="red", command=quit).grid(row=8,column=0)

master.mainloop()




