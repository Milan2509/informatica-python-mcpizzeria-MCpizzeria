### --------- Bibliotheken en globale variabelen ----------------
import sqlite3

with sqlite3.connect("MCPizzeria.db") as db:
    # cursor is object waarmee je data uit de database kan halen
    cursor = db.cursor()

### --------- Functie definities -----------------

def maakTabellenAan():
    # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_pizzas(
        gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
        gerechtNaam TEXT NOT NULL,
        gerechtPrijs REAL NOT NULL);
    """)
    print("Tabel 'tbl_pizzas' aangemaakt.")

     #dit maakt het klanten tabel aan
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_klanten(
        klantNr INTEGER PRIMARY KEY AUTOINCREMENT,
        klantAchternaam TEXT);""")
    print("Tabel 'tbl_klanten' aangemaakt.")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_winkelWagen(
        bestelRegel INTEGER PRIMARY KEY AUTOINCREMENT,
        klantNr INTEGER,
        gerechtID INTEGER,
        aantal INTEGER NOT NULL,
        FOREIGN KEY (klantNr) REFERENCES tbl_klanten(klantNr)
        FOREIGN KEY (gerechtID) REFERENCES tbl_pizzas(gerechtID)
        );""")
    print("Tabel 'tbl_winkelWagen' aangemaakt.")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam)  # SQL om ALLE gegevens te halen
    opgehaalde_gegevens = cursor.fetchall()  # sla gegevens op in een variabele
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens)  # druk gegevens af

def voegPizzaToe(naam_nieuwe_pizza, prijs_nieuwe_pizza):
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (naam_nieuwe_pizza, prijs_nieuwe_pizza))
    db.commit()  # gegevens naar de database wegschrijven
    print("Pizzas toegevoegd:")
    printTabel("tbl_pizzas")

def verwijderPizza(gerechtNaam):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,))
    print("Gerecht verwijderd uit 'tbl_pizzas':", gerechtNaam)
    db.commit()  # gegevens naar de database wegschrijven
    printTabel("tbl_pizzas")

def pasGerechtAan(gerechtID, nieuweGerechtNaam, nieuwePrijs):
    cursor.execute("UPDATE tbl_pizzas SET gerechtNaam = ?, gerechtPrijs = ? WHERE gerechtID = ?", 
                   (nieuweGerechtNaam, nieuwePrijs, gerechtID))
    db.commit()  # gegevens naar de database wegschrijven
    print("Gerecht aangepast")
    printTabel("tbl_pizzas")

def voegKlantToe(naam_nieuwe_klant):
    cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?)", (naam_nieuwe_klant,))
    db.commit()
    print("Klant toegevoegd:")
    printTabel("tbl_klanten")

def zoekKlantInTabel(ingevoerde_klantnaam):
    cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?", (ingevoerde_klantnaam,))
    zoek_resultaat = cursor.fetchall()
    if zoek_resultaat == []:
        print("Geen klant gevonden met achternaam", ingevoerde_klantnaam)
        print("Klant wordt nu toegevoegd.")
        cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?)", (ingevoerde_klantnaam,))
        db.commit()  # gegevens in de database zetten
        printTabel("tbl_klanten")
        cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?", (ingevoerde_klantnaam,))
        zoek_resultaat = cursor.fetchall()
    return zoek_resultaat

def vraagOpGegevensPizzaTabel():
    cursor.execute("SELECT * FROM tbl_pizzas")
    resultaat = cursor.fetchall()
    print("Tabel tbl_pizzas:", resultaat)
    return resultaat

def voegToeAanWinkelWagen(klantNr, gerechtID, aantal):
    cursor.execute("INSERT INTO tbl_winkelWagen VALUES(NULL, ?, ?, ?)", (klantNr, gerechtID, aantal))
    db.commit()  # gegevens in de database zetten
    printTabel("tbl_winkelWagen")

def vraagOpGegevensWinkelWagenTabel():
    cursor.execute("SELECT * FROM tbl_winkelWagen")
    resultaat = cursor.fetchall()
    print("Tabel tbl_winkelWagen:", resultaat)
    return resultaat

### --------- Hoofdprogramma ---------------
maakTabellenAan()
# voegKlantToe("Janssen")
# voegKlantToe("Smit")

# voegPizzaToe("Margarita", 9.50)
# voegPizzaToe("Hawaii", 12.25)
# voegPizzaToe("Salami", 10.00)
