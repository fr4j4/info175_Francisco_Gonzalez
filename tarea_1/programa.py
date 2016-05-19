# -*- coding: utf-8 -*-
from Tkinter import *  
import string 

texto_salida=0
var_metodo=0
salto=0

def encrypt(text):
	out="cenit"
	if(var_metodo.get()==2):
		out=cenitpolar(text)
	elif(var_metodo.get()==1):
		out=cesar(text,salto.get())
	return out
def settext(text):
	texto_salida.config(state="normal")
	texto_salida.delete("1.0",END)#borra todo lo que contiene el texto de salida
	texto_salida.insert(INSERT,text)
	texto_salida.config(state="disabled")

def cenitpolar(input):
	output=""
	for c in input:
		aux=c;
		if c=="c":
			aux="p"
		elif c=="e":
			aux="o"
		elif c=="n":
			aux="l"
		elif c=="i":
			aux="a"
		elif c=="t":
			aux="r"

		elif c=="p":
			aux="c"
		elif c=="o":
			aux="e"
		elif c=="l":
			aux="n"
		elif c=="a":
			aux="i"
		elif c=="r":
			aux="t"

		elif c=="C":
			aux="P"
		elif c=="E":
			aux="O"
		elif c=="N":
			aux="L"
		elif c=="I":
			aux="A"
		elif c=="T":
			aux="R"

		elif c=="P":
			aux="C"
		elif c=="O":
			aux="E"
		elif c=="L":
			aux="N"
		elif c=="A":
			aux="I"
		elif c=="R":
			aux="T"
		output+=aux;
	return output

def cesar(palabra,n):
	p=""
	letra=False
	abc_l=string.ascii_lowercase
	abc_u=string.ascii_uppercase
	for i in range (0,len(palabra)):
		letra=False
		for j in range (0,len(abc_l)):
			if(palabra[i]==abc_l[j]):
				if(j+n>len(abc_l)-1):
					n=n-len(abc_l)
				p=p+abc_l[j+n]
				letra=True;
			elif(palabra[i]==abc_u[j]):
				if(j+n>len(abc_u)-1):
					n=n-len(abc_u)
				p=p+abc_u[j+n]
				letra=True;
		if letra==False:
			p=p+palabra[i]
	return p

root =Tk()

var_metodo=IntVar()
salto=IntVar()

root.geometry("320x320")#tamaño ventana
root.title("Encriptador super-secreto")#titulo ventana

#definicionn de los widgets que componen la ventana
label_1=Label(root,text="Ingrese texto_entrada a encriptar")
label_2=Label(root,text="Seleccione un método de encriptacion")
label_3=Label(root,text="Especifique un salto\npara la encriptaicon cesar")
label_4=Label(root,text="Texto encriptado")

empty_label_1=Label(root,text="")#label vacio, para hacer un "salto de fila"

spin=Spinbox(root,width=2,from_=0, to=sys.maxsize,state="readonly",textvariable=salto)

texto_entrada=Text(root,width="45",height="5")
texto_salida=Text(root,width="45",height="5",state="disabled")

boton=Button(root,text="Encriptar!",command=lambda:settext(encrypt(texto_entrada.get("1.0",END))))

radio_1=Radiobutton(root,text="césar",variable=var_metodo,value=1,command=lambda:spin.config(state="readonly"))#value=1
radio_2=Radiobutton(root,text="cenit-polar",variable=var_metodo,value=2,command=lambda:spin.config(state="disabled"))#value=2


#definir posiciones de los widgets
label_2.grid(row=2,columnspan=2)
label_1.grid(row = 0,columnspan=2)
texto_entrada.grid(row = 1,column=0,columnspan=2)
radio_1.grid(row = 3,column=0)
radio_2.grid(row = 3,column=1)
label_3.grid(row=4,columnspan=1)
spin.grid(row=4,column=1)
empty_label_1.grid(row=5)
label_4.grid(row=6,column=0)
texto_salida.grid(row=7,columnspan=2)

boton.grid(row=8,columnspan=3)

var_metodo.set(1)#establece el valor de la variable en 1 lo que provocará que el radio button 1 se seleccione cuando parta el programa

root.mainloop()
