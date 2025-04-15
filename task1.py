import tkinter as tk
from tkinter import PhotoImage
import playsound

def playysound():
    try:
        playsound.playsound("audioss.mp3")
    except Exception as e:
        print(f"Error playing sound: {e}")

def playsoundwithevent(event):
    playysound()

window = tk.Tk()
window.title("Sizzurp")
window.geometry("500x500")

try:
    golds = PhotoImage(file="image.png")
except Exception as e:
    print(f"Error loading image: {e}")
    golds = None

b2 = tk.Button(window, image=golds, text='Play', command=playysound)
b1 = tk.Button(window, text="Click to play")
b1.bind("<Button>", playsoundwithevent)

b2.place(x=30, y=150)
b1.place(x=70, y=120)

window.mainloop()


"""
f = playsound.playsound('audioss.mp3')
"""


