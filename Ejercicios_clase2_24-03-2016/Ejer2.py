# -*- coding: utf-8 -*-
import string
def encrypt(palabra,n):
	p=""
	letra=False
	abc=string.ascii_lowercase
	for i in range (0,len(palabra)):
		letra=False
		for j in range (0,len(abc)):
			if(palabra[i]==abc[j]):
				if(j+n>len(abc)-1):
					n=n-len(abc)
				p=p+abc[j+n]
				letra=True;
		if letra==False:
			p=p+palabra[i]
	return p

if __name__=="__main__":
	print(encrypt(raw_input("Ingrese una palabra: ").lower(),int(raw_input("Ingrese un numero: "))))