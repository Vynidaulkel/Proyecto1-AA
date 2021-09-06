from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

#Crea la ventana principal
raiz = tk.Tk() 
raiz.title("Domino") #Cambiar el nombre de la ventana 
raiz.geometry("700x600") #Configurar tamaño
#-------------------------------------

#Carga la imagen del fondo
ImgMapa = Image.open('fondo.jpeg')
ImgMapa = ImgMapa.resize((700, 600), Image.ANTIALIAS) # Redimension (Alto, Ancho)
ImgMapa = ImageTk.PhotoImage(ImgMapa)
fondo = Label(raiz, image=ImgMapa)
fondo.pack()
fondo.place(x=0,y=0)


#Carga la imagen del fondo
comp = Image.open('comp.jpg')
comp = comp.resize((350, 300), Image.ANTIALIAS) # Redimension (Alto, Ancho)
comp = ImageTk.PhotoImage(comp)
mapa = Label(raiz, image=comp)
mapa.pack()
mapa.place(x=185,y=100)
#-------------------------------------



button1 = tk.Button(raiz, font=("Courier",22), bg="green", text="Start",height=0,width=8)
button1.place(x=285,y=485)

raiz.mainloop() 
