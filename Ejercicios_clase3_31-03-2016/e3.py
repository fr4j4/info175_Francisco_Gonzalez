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
	def __init__(self,nombre,rut,f_nac,genero):
		super(alumno,self).__init__(nombre,rut,f_nac,genero)
		self.notas=[]
	def agregar_nota(self,valor,ponderacion,ramo,carrera):
		self.notas.append(nota(valor,ponderacion,ramo,carrera))
	def promedio_por_ramo():
		



a1=alumno("Francisco","18008790-7",1992,"M")
