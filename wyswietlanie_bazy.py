from tkinter import *
from tkinter import ttk
import sqlite3


def wyswietl():
    ikona = PhotoImage(file="car.png")

    # Funkcja usuwania rekordu
    def usun_rekord():
        # Połączenie z bazą danych
        baza = sqlite3.connect("baza_wspisow.db")
        c = baza.cursor()
        lista = my_tree.selection()

        # Usuwanie elementu z drzewa i z bazy
        for el in lista:
            my_tree.delete(el)
            c.execute(f"DELETE from wpisy WHERE oid={el}")

        # Zamknięcie połączenia
        baza.commit()
        baza.close()

    # Połączenie z bazą danych
    baza = sqlite3.connect("baza_wspisow.db")
    c = baza.cursor()
    # Parametry okna
    wyswietlanie = Toplevel()
    wyswietlanie.title("Wpisy dziennika")
    wyswietlanie.wm_iconphoto(False, ikona)
    wyswietlanie.geometry("1000x600")
    wyswietlanie.resizable(width=False, height=False)
    wyswietlanie.title("Wpisy")
    wyswietlanie.wm_iconphoto(False, ikona)
    tbg = PhotoImage(file="tree_background.png")
    Label(wyswietlanie, image=tbg).place(x=-100, y=-170)

    # Utworzenie drzewa
    ramka = Frame(wyswietlanie)
    ramka.pack(pady=20)
    suwak = Scrollbar(ramka)
    suwak.pack(side=RIGHT, fill=Y)
    my_tree = ttk.Treeview(ramka, yscrollcommand=suwak)
    my_tree.pack()
    my_tree['columns'] = ("Kategoria", "Nazwa", "Koszt", "Data", "Przebieg", "Uwagi")

    # Formatowanie drzewa
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Kategoria", anchor=W, width=120)
    my_tree.column("Nazwa", anchor=W, width=120)
    my_tree.column("Koszt", anchor=W, width=120)
    my_tree.column("Data", anchor=W, width=120)
    my_tree.column("Przebieg", anchor=W, width=120)
    my_tree.column("Uwagi", anchor=W, width=300)

    # Zmiana stylu drzewa
    styl = ttk.Style()
    styl.theme_use("clam")
    my_tree.tag_configure('nieparzyste', background="white")
    my_tree.tag_configure('parzyste', background="lightblue")

    # Utworzenie nagłówków
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Kategoria", text="Kategoria", anchor=W)
    my_tree.heading("Nazwa", text="Nazwa", anchor=W)
    my_tree.heading("Koszt", text="Koszt", anchor=W)
    my_tree.heading("Data", text="Data", anchor=W)
    my_tree.heading("Przebieg", text="Przebieg", anchor=W)
    my_tree.heading("Uwagi", text="Uwagi", anchor=W)

    # Pobranie rekordów z bazy
    c.execute("SELECT *,oid FROM wpisy")
    rekordy = c.fetchall()

    # Dodawanie danych do wierszy drzewa
    suma_kosztow = 0
    licznik = 0
    for r in rekordy:
        if licznik % 2 == 0:
            my_tree.insert(parent='', index='end', iid=r[6], text="",
                           values=(r[0], r[1], str(r[2]) + " zł", r[3], str(r[4]) + " km", r[5]), tags='parzyste')
        else:
            my_tree.insert(parent='', index='end', iid=r[6], text="",
                           values=(r[0], r[1], str(r[2]) + " zł", r[3], str(r[4]) + " km", r[5]), tags='nieparzyste')
        licznik += 1
        suma_kosztow += r[2]
    my_tree.insert(parent='', index='end', iid=rekordy[len(rekordy)-1], text="",
                           values=('', 'Razem:', str(suma_kosztow) + " zł", '', '', ''))

    # Przycisk usuwania rekordu
    Button(wyswietlanie, width=20, height=2, font=("Arial", 12, "bold"), command=usun_rekord, text="Usuń wpis",
           bg="#A9C8D8", borderwidth=3).pack(pady=35)

    # Przycisk zamykania
    Button(wyswietlanie, width=20, height=2, font=("Arial", 12, "bold"), command=wyswietlanie.destroy, text="Zamknij",
           bg="#A9C8D8", borderwidth=3).pack(pady=15)

    # Zamknięcie połączenia
    baza.commit()
    baza.close()
    wyswietlanie.mainloop()
