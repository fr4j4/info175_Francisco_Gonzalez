# -*- coding: utf-8 -*-
from datetime import date

class persona(object):
	def __init__(self,nombre,rut,f_nac,genero):
		self.nombre=nombre
		self.rut=rut
		self.f_nac=f_nac
		self.genero=genero
	def get_edad(self):
		return date.today().year-self.f_nac

class nota(object):
	def __init__(self,valor,ponderacion,ramo,carrera):
		self.valor=valor
		self.ponderacion=ponderacion
		self.ramo=ramo
		self.carrera=carrera
	def get_valor(self):
		return self.valor
	def get_ponderacion(self):
		return self.ponderacion
	def modificar(self,valor,ponderacion,ramo,carrera):
		self.valor=valor
		self.ponderacion=ponderacion
		self.ramo=ramo
		self.carrera=carrera

class alumno(persona):
	def __init__(self,nombre,rut,f_nac,genero,carrera,promocion,correo):
		super(alumno,self).__init__(nombre,rut,f_nac,genero)
		self.promocion=promocion
		self.carrera=carrera
		self.corre=correo
		self.notas=[]
	def agregar_nota(self,valor,ponderacion,ramo,carrera):
		self.notas.append(nota(valor,ponderacion,ramo,carrera))
		print "nota agregada"
		print "             ramo: "+ramo+" valor: "+str(valor)+" ponderacion: "+str(ponderacion)+" carrera: "+carrera
	def promedio_por_ramo(self):
		ramos={}#diccionario
		for i in range(0,len(self.notas)):
			if ramos.has_key(self.notas[i].ramo)==False:
				ramos[self.notas[i].ramo]=0
			ramos[self.notas[i].ramo]+=self.notas[i].valor*self.notas[i].ponderacion

		print "Notas por ramos:"
		for ramo,nota in ramos.items():
			print ramo +" : "+str(nota)
	def pga(self):
		pass
	



a1=alumno("Francisco","18008790-7",1992,"M","ICI","2012","francisco.gonzalez@uach.cl")
a1.agregar_nota(7.0,0.25,"Programacion","ICI")
a1.agregar_nota(7.0,0.25,"Programacion","ICI")
a1.agregar_nota(7.0,0.25,"Programacion","ICI")
a1.agregar_nota(7.0,0.25,"Programacion","ICI")
a1.agregar_nota(7.0,0.5,"Lenguaje","ICI")
a1.agregar_nota(7.0,0.5,"Lenguaje","ICI")
a1.promedio_por_ramo()