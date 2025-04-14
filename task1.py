import tkinter as tk
from tkinter import PhotoImage
import mp3play

f = mp3play.load('audioss.mp3'); play = lambda: f.play()


window = tk.Tk()
window.title("Sizzurp")
window.geometry("500x500")

golds = PhotoImage(file="image.png")

button2 = tk.Button(window, image=golds, root, text = 'Play', command = play )

button2.place(x=30, y=150)

window.mainloop()