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
    #dit maakt het pizza tabel aan
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_pizzas(
        gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
        gerechtNaam TEXT NOT NULL,
        gerechtPrijs REAL NOT NULL);""")
    print("Tabel aangemaakt 'tbl_pizzas' aangemaakt")
    
    #dit maakt het klanten tabel aan
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_klanten(
        klantNr INTEGER PRIMARY KEY AUTOINCREMENT,
        klantAchternaam TEXT);""")
    print("Tabel 'tbl_klanten' aangemaakt.")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam)
    opgehaalde_gegevens = cursor.fetchall()
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens)

def voegPizzaToe(naam_nieuwe_pizza, prijs_nieuwe_pizza):
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (naam_nieuwe_pizza, prijs_nieuwe_pizza))
    db.commit() #gegevens naar de database wegschrijven
    print("Pizzas toegevoegd:")
    printTabel("tbl_pizzas")
    
def verwijderPizza(gerechtNaam):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,))
    print("Gerecht verwijderd uit 'tbl_pizzas':", gerechtNaam )
    db.commit() #gegevens naar de database wegschrijven
    printTabel("tbl_pizzas")

def pasGerechtAan(gerechtID, nieuweGerechtNaam, nieuwePrijs):
    cursor.execute("UPDATE tbl_pizzas SET gerechtNaam = ?, gerechtPrijs = ? WHERE gerechtID = ?", (nieuweGerechtNaam, 
    nieuwePrijs, gerechtID ))
    db.commit() #gegevens naar de database wegschrijven
    print("Gerecht aangepast")
    printTabel("tbl_pizzas")

def voegKlantToe(naam_nieuwe_klant):
    cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?)", (naam_nieuwe_klant,))
    db.commit()
    print("Klant toegevoegd:")
    printTabel("tbl_klanten")

### --------- Hoofdprogramma  ---------------
maakTabellenAan()
printTabel("tbl_pizzas")