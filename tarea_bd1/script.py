# -*- coding: utf-8 -*-
'''
1- ¿Cantidad total de ventas en el año 2013? (sale → gross_total)
2- ¿Precio promedio de venta por producto? (sale_product → net_unit_price)
3- ¿Total de ventas (gross_total) por cliente? (sale→ gross_total)
4- ¿Total de ventas por cliente en el año 2014? (sale → gross_total)
5- ¿Cantidad y monto total de ventas por día en noviembre de 2013?
6- ¿Cantidad y montos totales agrupados por producto en orden descendente según cantidad? 
   (sale_product → quantity, gross_total)
'''
import sqlite3 as lite
con = None
cursor= None
data = None

con=lite.connect('pos_empresa.db')
cursor=con.cursor()

print("Conexion a la base de datos ... OK")

#1
cursor.execute("select count(*) from sale where date like '2013%'")
data=cursor.fetchone()
print ("1- "+str(data[0])+" ventas se realizaron el año 2013\n")

#2
limite_2=10 #limite de productos a mostrar
cursor.execute("select avg(net_unit_price) as promedio,  product.name from sale_product join product where product_id=product.id group by product.name order by name asc limit "+str(limite_2))
data=cursor.fetchall()
print("2- precio de venta promedio - producto (limitado a primeros "+str(limite_2)+" productos\n")
for d in data:
	print "   "+str(d[0]) +" - "+ d[1]

print("")

#3
limite_3=10 #limite de productos a mostrar
cursor.execute("select count(gross_total),entity.names, company_name from sale join entity where entity_id=entity.id group by entity_id order by names,company_name limit "+str(limite_3))
data=cursor.fetchall()
print "3- Total Ventas - nombre cliente (limitado a primeros "+str(limite_3)+" clientes)\n"
for d in data:
	print "   "+str(d[0]) +" - "+d[1] +d[2]
print("")

#4
limite_4=10 #limite de productos a mostrar
agno=2014
cursor.execute("select count(gross_total),entity.names, company_name from sale join entity where entity_id=entity.id and sale.date like '"+str(agno)+"%' group by entity_id  order by names,company_name limit "+str(limite_4))
data=cursor.fetchall()
print "4- Total Ventas - nombre cliente (limitado a primeros "+str(limite_4)+" clientes), año "+str(agno)+"\n"
for d in data:
	print "   "+str(d[0]) +" - "+d[1] +d[2]
print("")

#5 
limite_5=10 #limite de productos a mostrar
cursor.execute("select count(gross_total), sum(gross_total) ,date from sale where date like '2013-11%' group by date order by date limit "+str(limite_5))
data=cursor.fetchall()
print "5- Cantidad Ventas - Monto total ventas - Fecha (limitado a primeras "+str(limite_5)+" fechas ), Noviembre 2013"
for d in data:
	print "   "+str(d[0]) +" - "+str(d[1]) +d[2]
print("")

#6
limite_6=10 #limite de productos a mostrar
cursor.execute("select sum(quantity) as Cantidad,sum(gross_total) as Monto_total,product.name from sale_product join product where product_id=product.id group by sale_product.product_id order by Cantidad desc limit "+str(limite_6))
data=cursor.fetchall()
print "6- Cantidad Ventas - Monto total ventas - Fecha (limitado a primeros "+str(limite_6)+" productos )"
for d in data:
	print "   "+str(d[0]) +" - "+str(d[1])+" - "+d[2]
print("")

con.commit()
con.close()
