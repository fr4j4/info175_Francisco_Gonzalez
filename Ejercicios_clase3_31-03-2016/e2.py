# -*- coding: utf-8 -*-
class vehiculo(object):
	def __init__(self):
		self.kilometraje=0
		self.bencina=0
		self.rendimiento=10
		self.encendido=False
		self.ruedas=0
		self.peso=0

	def encender(self):
		print "bum bum bummmm (encendido)"
		self.encendido=True

	def apagar(self):
		print "ZzZzZzZzZz (apagado)"
		self.encendido=True

	def mover (self,distancia):
		if self.encendido:
			if self.rendimiento*self.bencina>=distancia:
				print "moviendo...\n...Se ha desplazado "+str(distancia)+" km"
				self.bencina-=distancia/self.rendimiento
				self.kilometraje+=distancia
			else:
				print "falta bencina para mover"
		else:
			print "El vehiculo está apagado, no se puede mover"
		
	def get_kilometraje(self):
		return self.kilometraje

	def get_bencina(self):
		return self.bencina

	def cargar_bencina(self,b):
		if self.encendido==False:
			print ("se ha cargado "+str(b)+" lt. de bencina")
			self.bencina+=b
		else:
			print "Debe apagar el vehiculo antes de cargar"

	def set_ruedas(self,ruedas):
		self.ruedas=ruedas

	def set_peso(self,peso):
		self.peso=peso



class acoplado(object):
		def __init__(self,carga,ruedas,peso):
			self.carga=carga
			self.ruedas=ruedas
			self.peso=peso
		def set_ruedas(self,ruedas):
			self.ruedas=ruedas
		def set_peso(self,peso):
			self.peso=peso
		def get_carga(self):
			return self.carga
		def get_peso(self):
			return self.peso
		def get_ruedas(self):
			return self.ruedas

class camion(vehiculo):
	def __init__(self):
		super(camion,self).__init__()#importante llamar al super
		self.acoplados=[]

	def agregar_acoplado(self,carga,ruedas,peso):
		self.acoplados.append(acoplado(carga,ruedas,peso))
		print "agregado acoplado: carga: "+carga+",ruedas: "+str(ruedas)+", peso: "+str(peso)
		self.peso+=peso
	def quitar_acoplado(self,carga):
		i=0
		for a in self.get_acoplados():
			if a.get_carga()==carga:
				self.acoplados.pop(i)
				print "carga eliminada ("+str(carga)+")"
				break
			i+=1

	def get_acoplados(self):
		return self.acoplados
	def get_ruedas(self):
		return self.ruedas
	def get_peso(self):
		return self.peso
	def imprime_acoplados(self):
		print "acoplados:"
		for a in self.get_acoplados():
			print "carga: "+a.get_carga()
			print "      ruedas: "+str(a.get_ruedas())
			print "      peso: "+str(a.get_peso())

c1=camion()
c1.set_peso(20000)
c1.set_ruedas(8)
c1.cargar_bencina(300)
c1.encender()
print "peso: "+str(c1.get_peso())
c1.agregar_acoplado("madera",5,300)
c1.agregar_acoplado("vines",18,800)
print "peso: "+str(c1.get_peso())
c1.imprime_acoplados()
c1.quitar_acoplado("madera")
c1.imprime_acoplados()