# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
#
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------
def maakTabellenAan():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_pizzas(
        gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
        gerechtNaame TEXT NOT NULL,
        gerechtPrijs REAL NOT NULL);""")
    print("Tabel aangemaakt 'tbl_pizzas' aangemaakt")

### --------- Hoofdprogramma  ---------------
maakTabellenAan()
