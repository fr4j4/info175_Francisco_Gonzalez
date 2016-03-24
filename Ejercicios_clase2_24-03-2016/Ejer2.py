# -*- coding: utf-8 -*-
import string
def encrypt(palabra,n):
	p=""
	abc=string.ascii_lowercase
	for i in range (0,len(palabra)):
		for j in range (0,len(abc)):
			if(palabra[i]==abc[j]):
				m=1;
				if(j+n>len(abc)-1):
					n=n-len(abc)
				p=p+abc[j+n]
	return p

if __name__=="__main__":
	print(encrypt(raw_input("Ingrese una palabra: ").lower(),int(raw_input("Ingrese un numero: "))))