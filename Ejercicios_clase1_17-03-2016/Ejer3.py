
if __name__=="__main__":
	lista=[]
	repite=True
	while repite:
		print "Ingrese frase"
		linea=raw_input();
		if len(linea)>0:
			linea=linea.upper()
			lista.append(linea)
		else:
			repite=False
	for l in lista:
		print l
