import tkinter as tk # Importuje ovladač oken
from tkinter import simpledialog as sd # Inportuje příkaz pro vložení stringu
from tkinter import messagebox as mb # Impotruje příkaz pro zobrazení stringu
import random # Importuje ovladač náhod

def zmenit_cislo(): # Příkaz změnit číslo na kostce
    nove_cislo = random.randint(1, 6)
    entry.delete(0,tk.END)
    entry.insert(0, str(nove_cislo))

def konec():
    a=sd.askstring('Ukončení hry', 'Kdo vyhrál?')
    mb.showinfo(title="Gratulace", message="gratiluji "+a+" k úspěšné výhře v této hře!")

window = tk.Tk() # Otevře okno tk.Tk
window.title("Hod kostkou")

entry = tk.Entry(window, font=("Helvetica", 300), justify='center', width=2) # Vytvoří podokno na čísla v okně tk.Tk
entry.insert(0, str(random.randint(1, 6))) # Vytvoří náhodné číslo
entry.pack(pady=20)

button = tk.Button(window, text="Hoď kostkou!", font=("Helvetica", 16), command=zmenit_cislo) # Vytvoří tlačítko pro hod kostkou
button.pack(pady=10)

button = tk.Button(window, text="Konec hry", font=("Helvetica", 16), command=konec)
button.pack(pady=10)

window.mainloop() # Opakuje cyklus
