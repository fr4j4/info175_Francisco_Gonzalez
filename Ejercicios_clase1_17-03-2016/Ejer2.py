def imprimeLista(l):
	lista=sorted(l)
	linea=""
	for i in range (0,len(lista)):
		if i != len(lista)-1:
			#print lista[i],",",
			linea+=lista[i]+","
		else:
			#print lista[i]
			linea+=lista[i]
	print linea

if __name__=="__main__":
	c=0
	repite=True
	palabra=""
	lista=[]
	while repite:
		print ""
		print "Palabras en la lista: ",c
		print "ingrese palabra ",(c+1)
		print "no ingrese nada para terminar"
		palabra=raw_input();
		if len(palabra)>0:
			lista.append(palabra)
			c+=1
		else:
			repite=False
	print "Lista ordenada:"
	imprimeLista(lista);

