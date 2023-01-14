from tkinter import *
import sqlite3
import dodawanie_do_bazy
import wyswietlanie_bazy
import eksport_do_arkusza


# Utworzenie i połączenie się z bazą danych
baza = sqlite3.connect("baza_wspisow.db")
c = baza.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS wpisy(
               rodzaj_wydatku text,
               nazwa_wydatku text,
               koszt real,
               data text,
               przebieg integer,
               uwagi text
               ) """)

# Zamknięcie połączenia
baza.commit()
baza.close()

# Utworzenie i ustalenie parametrów głównego okna
root = Tk()
root.resizable(width=False, height=False)
root.geometry("900x550")
root.title("Dziennik kosztów")
ikona = PhotoImage(file="car.png")
root.wm_iconphoto(False, ikona)
bg = PhotoImage(file="background.png")
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 0, weight=1)


# Dodanie tła głównego okna
Label(root, image=bg).place(x=-180, y=-185)

# Utworzenie elementów głównego okna
Button(root, text="Dodaj wpis do dziennika", font=("Arial", 12, "bold"), padx=88, pady=16,
       command=dodawanie_do_bazy.dodaj_wpis,
       bg="#A9C8D8").grid(row=1, column=0, sticky="w")
Button(root, text="Wyświetl wszystkie wpisy", font=("Arial", 12, "bold"), padx=83, pady=16, bg="#A9C8D8",
       command=wyswietlanie_bazy.wyswietl).grid(row=2, column=0, sticky="w")
Button(root, text="Eksportuj do arkusza kalk.", font=("Arial", 12, "bold"), padx=80, pady=16,
       bg="#A9C8D8", command=eksport_do_arkusza.eksportowanie).grid(row=3, column=0, sticky="w")
Button(root, text="Zamknij program", font=("Arial", 12, "bold"), padx=118, pady=16, command=root.destroy,
       bg="#A9C8D8").grid(row=4, column=0, sticky="w")
Label(root, text="Kamil Safaryjski 2023").grid(row=5, column=2, sticky="se")

# Wywołanie głównego okna
root.mainloop()
