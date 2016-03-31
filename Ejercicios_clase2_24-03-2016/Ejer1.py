# -*- coding: utf-8 -*-
def function(size):
	numeros=[x for x in range (1,size+1)]
	numeros=filter(lambda x: x%3==0 and x%7==0,numeros)
	return numeros

if __name__=="__main__":
	print function(int(raw_input("Ingrese un numero: ")));
