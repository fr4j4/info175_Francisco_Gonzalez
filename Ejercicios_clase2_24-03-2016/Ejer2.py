# -*- coding: utf-8 -*-
import string
def encrypt(palabra,n):
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

if __name__=="__main__":
	print(encrypt(raw_input("Ingrese una palabra: "),int(raw_input("Ingrese un numero: "))))