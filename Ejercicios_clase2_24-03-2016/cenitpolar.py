import string
def cenitpolar(input):
	"""
		C E N I T
		P O L A R
	"""
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
		output+=aux;
	return output

if __name__=="__main__":
	entrada=raw_input("Frase a encriptar:")
	print "Codificacion a cenit-polar:"
	print cenitpolar(entrada)