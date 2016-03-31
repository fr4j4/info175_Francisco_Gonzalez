# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.geometry("320x480")#tamaño ventana
root.title("Encriptador super-secreto")#titulo ventana
label_1=Label(root,text="Ingrese texto a encriptar").pack()
texto=Text(root,width="40",height="5").pack()


root.mainloop()