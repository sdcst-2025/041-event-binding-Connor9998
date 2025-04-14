import tkinter as tk
from tkinter import PhotoImage
import playsound as p

def playsound(event):
    print(event)
    p.playsound("audioss.mp3")


window = tk.Tk()
window.title("Sizzurp")
window.geometry("500x500")

golds = PhotoImage(file="image.png")

b2 = tk.Button(window, image=golds, text='Play', command= playsound)
b1 =  tk.Button(window,text="Click to play")
b1.bind("<Button>",playsound)


b2.place(x=30, y=150)
b1.place(x=70,y=120)

b2.pack()
b1.pack()
window.mainloop()



"""
f = playsound.playsound('audioss.mp3')
"""


