def ordenalista(l):
	return sorted(l)

if __name__=="__main__":
	c=0
	print "Palabras en la lista: ",c
	repite=True
	palabra=""
	lista=[]
	while repite:
		print "Palabras en la lista: ",c
		print "ingrese palabra ",(c+1)
		print "no ingrese nada para terminar"
		palabra=raw_input();
		if len(palabra)>0:
			lista.append(palabra)
			c+=1
		else:
			repite=False

	lista=ordenalista(lista)

	for l in lista:
		print l

