# -*- coding: utf-8 -*-
class Auto(object):
	def __init__(self):
		self.kilometraje=0
		self.bencina=0
		self.rendimiento=10
		self.encendido=False
	def encender(self):
		print "bum bum bummmm (encendido)"
		self.encendido=True;
	def apagar(self):
		print "ZzZzZzZzZz (apagado)"
		self.encendido=True;
	def mover (self,distancia):
		if self.encendido:
			if self.rendimiento*self.bencina>=distancia:
				print "moviendo...\n...Se ha desplazado "+str(distancia)+" km"
				self.bencina-=distancia/self.rendimiento
				self.kilometraje+=distancia
			else:
				print "falta bencina para mover"
		else:
			print "El auto está apagado, no se puede mover"
		
	def get_kilometraje(self):
		return self.kilometraje
	def get_bencina(self):
		return self.bencina
	def cargar_bencina(self,b):
		if self.encendido==False:
			print ("se ha cargado "+str(b)+" lt. de bencina")
			self.bencina+=b
		else:
			print "Debe apagar el auto antes de cargar"

a1=Auto()
a1.encender()
a1.apagar()
a1.cargar_bencina(40)
a1.encender()
a1.mover(50)