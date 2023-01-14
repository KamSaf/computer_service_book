import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import sqlite3


# Funkcja dodawania wpisu do bazy
def dodaj_wpis():
    ikona = PhotoImage(file="car.png")
    wbg = PhotoImage(file="backgroundw.png")
    # Dodawanie rekordów do bazy
    def dodaj_do_bazy():
        if koszt.get().isdigit() and przebieg.get().isdigit() and len(rodzaj.get())>0 and len(nazwa.get())>0 and len(data.get())>0:
            # Połączenie z bazą danych
            baza = sqlite3.connect("baza_wspisow.db")
            c = baza.cursor()
            c.execute("INSERT INTO wpisy VALUES (:rodzaj, :nazwa, :koszt, :data, :przebieg, :uwagi)",
                      {
                          'rodzaj': rodzaj.get(),
                          'nazwa': nazwa.get(),
                          'koszt': koszt.get(),
                          'data': data.get(),
                          'przebieg': przebieg.get(),
                          'uwagi': uwagi.get()
                      })

            # Zamknięcie połączenia z bazą
            baza.commit()
            baza.close()

            # Usuwanie wartości z pól
            rodzaj.delete(0, END)
            nazwa.delete(0, END)
            koszt.delete(0, END)
            data.delete(0, END)
            przebieg.delete(0, END)
            uwagi.delete(0, END)
        else:
            tkinter.messagebox.showerror(title="Błąd danych", message="Wprowadzono błędne dane")


    dodawanie = Toplevel()
    dodawanie.geometry("700x350")
    dodawanie.resizable(width=False, height=False)
    dodawanie.title("Dodawanie wpisu")
    dodawanie.wm_iconphoto(False, ikona)
    Label(dodawanie, image=wbg).place(x=-190, y=-190)
    Grid.rowconfigure(dodawanie, 1, weight=1)
    Grid.rowconfigure(dodawanie, 2, weight=1)
    Grid.rowconfigure(dodawanie, 3, weight=1)
    Grid.rowconfigure(dodawanie, 4, weight=1)
    Grid.rowconfigure(dodawanie, 5, weight=1)
    Grid.rowconfigure(dodawanie, 6, weight=1)
    Grid.rowconfigure(dodawanie, 7, weight=1)
    Grid.rowconfigure(dodawanie, 8, weight=1)
    Grid.columnconfigure(dodawanie, 0, weight=1)
    Grid.columnconfigure(dodawanie, 1, weight=1)

    Label(dodawanie, width=20, text="Kategoria wydatku: ", font=("Arial", 10, "bold"), bg="#A9C8D8",
          borderwidth=3).grid(row=1, column=0)
    rodzaj = ttk.Combobox(dodawanie, value=["Tankowanie", "Usługa", "Wydatek", "Inne"], width=40)
    rodzaj.grid(row=1, column=1)

    Label(dodawanie, width=20, text="Nazwa wydatku: ", font=("Arial", 10, "bold"), bg="#A9C8D8",
          borderwidth=3).grid(row=2, column=0)
    nazwa = Entry(dodawanie, width=45, borderwidth=5)
    nazwa.insert(0, "Nazwa")
    nazwa.grid(row=2, column=1)

    Label(dodawanie, width=20, text="Koszt: ", font=("Arial", 10, "bold"), bg="#A9C8D8",
          borderwidth=3).grid(row=3, column=0)
    koszt = Entry(dodawanie, width=45, borderwidth=5)
    koszt.insert(0, 0)
    koszt.grid(row=3, column=1)

    Label(dodawanie, width=20, text="Data: ", font=("Arial", 10, "bold"), bg="#A9C8D8",
          borderwidth=3,).grid(row=4, column=0)
    data = Entry(dodawanie, width=45, borderwidth=5)
    data.insert(0, "DD/MM/YYYY")
    data.grid(row=4, column=1)

    Label(dodawanie, width=20, text="Przebieg: ", font=("Arial", 10, "bold"), bg="#A9C8D8",
          borderwidth=3).grid(row=5, column=0)
    przebieg = Entry(dodawanie, width=45, borderwidth=5)
    przebieg.insert(0, 0)
    przebieg.grid(row=5, column=1)

    Label(dodawanie, width=20, text="Uwagi: ", font=("Arial", 10, "bold"), bg="#A9C8D8",
          borderwidth=3).grid(row=6, column=0)
    uwagi = Entry(dodawanie, width=45, borderwidth=5)
    uwagi.grid(row=6, column=1)
    # Przyciski
    Button(dodawanie, text="Dodaj", font=("Arial", 10, "bold"), width=40, height=2, bg="#A9C8D8",
           command=dodaj_do_bazy).grid(row=7, column=0, columnspan=2)
    Button(dodawanie, text="Zamknij", font=("Arial", 10, "bold"), width=40, height=2, command=dodawanie.destroy,
           bg="#A9C8D8").grid(row=8, column=0, columnspan=2)
    dodawanie.mainloop()
