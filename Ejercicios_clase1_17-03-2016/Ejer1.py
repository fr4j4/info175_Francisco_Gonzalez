# -*- coding: utf-8 -*-

def analiza_num(x,y):
	if x>y:
		print x,"es mayor que",y
	elif y>x:
		print x,"es menor que",y
	else:
		print "ambos numeros son iguale"

if __name__=="__main__":
	print "Ingrese primer numero"
	num1=input()
	print "Ingrese segundo numero"
	num2=input()
	analiza_num(num1,num2)