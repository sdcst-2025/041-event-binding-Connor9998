import tkinter as tk
from tkinter import PhotoImage
import playsound

def playysound():
    try:
        playsound.playsound("audioss.mp3")
    except Exception as e:
        print(f"Error playing sound: {e}")

def imusic():
    playsound.playsound("music.mp3")
    
    

def playsounds(event):
   imusic() 


def playsoundwithevent(event):
    playysound()

window = tk.Tk()
window.title("Sizzurp")
window.geometry("500x500")

try:
    golds = PhotoImage(file="image11.png")
except Exception as e:
    print(f"Error loading image: {e}")
    golds = None



b2 = tk.Button(window, image=golds, text='Play', command=playysound)
b1 = tk.Button(window, text="FIND OUT ._.")
b1.bind("<Button>", playsoundwithevent)
kg= PhotoImage(file="gold.png")
b3 = tk.Button(window, image= kg, command= imusic )
b3.bind("<Button>", imusic)

b2.place(x=30, y=150)
b1.place(x=350, y=190)
b3.place(x=350, y=150)
window.mainloop()


"""
f = playsound.playsound('audioss.mp3')
"""


