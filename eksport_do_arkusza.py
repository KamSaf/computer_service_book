import tkinter.messagebox
import pandas as pd
#from openpyxl.workbook import Workbook
import sqlite3


def eksportowanie():
    # Połączenie z bazą danych
    baza = sqlite3.connect("baza_wspisow.db")
    c = baza.cursor()

    # Pobranie rekordów z bazy
    c.execute("SELECT *,oid FROM wpisy")
    rekordy = c.fetchall()
    df = pd.DataFrame(rekordy, columns=["Kategoria", "Nazwa", "Koszt", "Data", "Przebieg", "Uwagi", "ID"])
    with pd.ExcelWriter("dziennik_kosztów.xlsx") as writer:
        df.to_excel(writer, sheet_name="Wpisy")
    tkinter.messagebox.showinfo(title="Eksport", message="Pomyślnie wyeksportowano dane do pliku dziennik_kosztów.xlsx.")

