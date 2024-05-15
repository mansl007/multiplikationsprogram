import tkinter as tk
from tkinter import colorchooser
import time as tm
from colour import Color
import random as rn
import json

# gradient av färger som en colorskeem skulle kunna välje från/ acepta för att göra en outift



tunt = []
tjockt = []
jeans = []
finbyxor = []
topp = [tunt, tjockt]
under = [jeans, finbyxor]
kläder = [topp, under]

with open("my_array.json", "r") as file:
    try:
        loaded_array = json.load(file)
    except:
        print("du har inga sparade plagg")
    finally:
        print("så ska vi lägga till några")
def VilketPlagg():
    Plagg = input("Är det en topp? ")
    if Plagg.lower() == "ja":
        vart = 1
        Plagg = input("Är det tunt? ")
        if Plagg.lower() == "ja":
            värme = 0
        else:
            värme = 1
    else:
        vart = 0
        Plagg = input("Är det jeans? ")
        if Plagg.lower() == "ja":
            värme = 1
        else:
            värme = 0
    return vart, värme

def pick_color():
    def Color_Select():
            color = colorchooser.askcolor()[1]  # Ask the user to choose a color and get the hex code
            if color:
                color_label.config(foreground=color)  # Set the foreground color of the Label
            
                Färg = color
                
                root.destroy()  # Close the window after color selection
                return Färg
            else:
                root.destroy()  # Close the window if no color is selected
                return None

    # Create the color selection window
    root = tk.Toplevel()
    root.title("Select Color")

    # Create a Label widget
    color_label = tk.Label(root, text="Select the color of your clothing", font=("Helvetica", 18))
    color_label.pack(pady=20)

    # Create a button to trigger color selection
    Färg= Color_Select()
    tk.Tk.destroy
    return Färg


def outfit():
    if värme == 1:
        överKropp = rn.randint(0,len(tunt))
        underKropp = rn.randint(0,len(jeans))
        överKropp = tunt(överKropp)
        underKropp = jeans(underKropp)
        print("du borde ha",överKropp(1),"och",underKropp(1))
    else:
        överKropp = rn.randint(0,len(tjockt))
        underKropp = rn.randint(0,len(finbyxor))
    

while True:
    print("Vill du lägga till ett plagg?")
    svar = input()
    if svar.lower() == "ja":
        vart, värme = VilketPlagg()
        tm.sleep(1)
        print("Färg")
        Färg = pick_color()
        svar2 = input("beskriv plagget")
        if Färg: #lägger till färg i arrays
            if vart == 1 and värme == 0:
                tunt.append([Färg, svar2])
            elif vart == 1 and värme == 1:
                tjockt.append([Färg, svar2])
            elif vart == 0 and värme == 1:
                jeans.append([Färg, svar])
            elif vart == 0 and värme == 0:
                finbyxor.append([Färg, svar2])
    else:
        print("vill du ha en outfit?")
        svar = input()
        if svar.lower() =="ja":
            värme = 1
            outfit(värme)
    with open("my_array.json", "w") as file:
        json.dump(kläder, file)