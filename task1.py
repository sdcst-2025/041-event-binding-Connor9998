import tkinter as tk
from tkinter import PhotoImage
import playsound

def playysound():
    try:
        playsound.playsound("audioss.mp3")
    except Exception as e:
        print(f"Error playing sound: {e}")

def imusic(event):
    playsound.playsound("music.mp3")
    print(event)
    
    

def playsounds(event):
   imusic() 


def playsoundwithevent(event):
    playysound()

window = tk.Tk()
window.title("Sizzurp")
window.geometry("825x210")

try:
    golds = PhotoImage(file="image111.png")
except Exception as e:
    print(f"Error loading image: {e}")
    golds = None






b2 = tk.Button(window, image=golds, text='Play')
cla= PhotoImage(file="imagez1111.png")
b1 = tk.Button(window, image=cla)
b1.bind("<Button>", playsoundwithevent)
kg= PhotoImage(file="gold11.png")
b3 = tk.Button(window, image= kg)
b3.bind("<Button>", imusic)
Slime= PhotoImage(file="imagell11102.png")
b4= tk.Button(window, image= Slime)

b2.grid(row=0, column=1)
b1.grid(row=0, column=0)
b3.grid(row=0, column= 2)
b4.grid(row=0, column=3)
window.mainloop()


"""
f = playsound.playsound('audioss.mp3')
"""


