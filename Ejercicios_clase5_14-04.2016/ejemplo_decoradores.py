# -*- coding: utf-8 -*-
LOGIN=False

def autenticado(f):
	def inner(*args, **kwargs):#se puede llamar como se quiera
		if LOGIN:
			f(*args,**kwargs)
		else:
			#raise Exception#lanzo excepcion
			print "Ud. no tiene permiso"
	return inner
	


def avisar(f):
	#funcion decoradora
	def inner(*args,**kwargs):
		f(*args,**kwargs)
		print "se ha ejecutado %s" %f.__name__
	return inner


@autenticado
@avisar
def abrir_puerta():
	print "Abrir puerta"

@autenticado
@avisar
def cerrar_puerta():
	print "Cerrar puerta"


abrir_puerta()