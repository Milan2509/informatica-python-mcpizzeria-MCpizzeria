from tkinter import *
import MCPizzeriaSQL  # Assuming this is your database interaction module

# Create the main window
venster = Tk()
venster.wm_title("MC Pizzeria")

# Add a Welcome Label
labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

# Add a Close Button
knopSluit = Button(venster, text="Sluiten", width=12, command=venster.destroy)
knopSluit.grid(row=17, column=4)

# Add Entry Fields and Labels for Customer Information
# Customer Name
labelKlantnaam = Label(venster, text="Klantnaam:")
labelKlantnaam.grid(row=1, column=0, sticky="W")
ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

# Customer Number
labelKlantNr = Label(venster, text="Klantnummer:")
labelKlantNr.grid(row=2, column=0, sticky="W")
invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

# Add a Search Button for Customer
def zoekKlant():
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    invoerveldKlantnaam.delete(0, END)
    invoerveldKlantNr.delete(0, END)
    for rij in gevonden_klanten:
        invoerveldKlantNr.insert(END, rij[0])
        invoerveldKlantnaam.insert(END, rij[1])

knopZoekKlant = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
knopZoekKlant.grid(row=1, column=2)

# Add a Listbox to Display Pizzas
listboxMenu = Listbox(venster, height=6, width=50)
listboxMenu.grid(row=2, column=1, rowspan=6, columnspan=2, sticky="W")

def toonMenuInListbox():
    listboxMenu.delete(0, END)
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    listboxMenu.insert(0, "ID\tGerecht\tPrijs")
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel)

knopToonPizzas = Button(venster, text="Toon alle pizza’s", width=12, command=toonMenuInListbox)
knopToonPizzas.grid(row=3, column=4)

# Add Selection Handling for Listbox
def haalGeselecteerdeRijOp(event):
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0]
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst)
    invoerveldGeselecteerdePizza.delete(0, END)
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst)

listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

labelGeselecteerdePizza = Label(venster, text="Gekozen pizza:")
labelGeselecteerdePizza.grid(row=9, column=0, sticky="W")
invoerveldGeselecteerdePizza = Entry(venster)
invoerveldGeselecteerdePizza.grid(row=9, column=1, sticky="W")

# Add OptionMenu for Quantity Selection
aantalGeslecteerdePizza = IntVar()
aantalGeslecteerdePizza.set(1)  # Default value
optieMenuAantal = OptionMenu(venster, aantalGeslecteerdePizza, 1, 2, 3, 4, 5)
optieMenuAantal.grid(row=10, column=1, sticky="W")

# Add Button to Add to Cart
def voegToeAanWinkelWagen():
    klantNr = invoerveldKlantNr.get()
    gerechtID = invoerveldGeselecteerdePizza.get().split()[0]  # Assuming ID is the first part
    aantal = aantalGeslecteerdePizza.get()
    MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal)
    winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
    listboxWinkelwagen.delete(0, END)
    for regel in winkelwagen_tabel:
        listboxWinkelwagen.insert(END, regel)

knopVoegToeAanWinkelWagen = Button(venster, text="Voeg toe", width=12, command=voegToeAanWinkelWagen)
knopVoegToeAanWinkelWagen.grid(row=11, column=4)

# Add Listbox to Display Cart
listboxWinkelwagen = Listbox(venster, height=6, width=50)
listboxWinkelwagen.grid(row=12, column=1, rowspan=6, columnspan=2, sticky="W")

# Start the main loop
venster.mainloop()
