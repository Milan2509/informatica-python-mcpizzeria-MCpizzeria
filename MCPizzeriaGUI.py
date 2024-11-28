# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
# Luuk & Milan
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL

### ---------  Functie definities  -----------------


### --------- Hoofdprogramma  ---------------
venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

#sql functies
#Voeg Pizzas Toe
# MCPizzeriaSQL.voegPizzaToe("Magarita", 9.50)
# MCPizzeriaSQL.voegPizzaToe("Hawaii", 12.25)
# MCPizzeriaSQL.voegPizzaToe("Salami", 10.00)

# #Verwijder Pizzas
# MCPizzeriaSQL.verwijderPizza("Hawaii")

# #Verander Pizzas
# MCPizzeriaSQL.pasGerechtAan(3, "Salamiiii", 19.25)

# #Voeg klant toe
# MCPizzeriaSQL.voegKlantToe("Janssen")




#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
