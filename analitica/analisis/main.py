#Traer un registro de N ventas para analizar con pandas
#Primeros pasos con pandas

from data.listasSimuladas import generar_ventas

import pandas as pd

datos_simulados=generar_ventas(1000)

#Organizando la fuente de datos con pandas

tablaOrenada=pd.DataFrame(datos_simulados)

#Informacion general
#print(tablaOrenada.info())

#Obtener la informacion estadistica basica (descriptiva)
#print(tablaOrenada.describe())

#Obtener la informacion de los primeros 20 registros
#print(tablaOrenada.head(20))

#Obtener la informacion de los ultimos n registros
#print(tablaOrenada.taicantidad

#Acceder a una columna seleccionar  en especifico
#print(tablaOrenada['vendedor'])

#Tarea como hago para acceder a varias columnas al mismo tiempo
#print(tablaOrenada[['cantidad','vendedor','total']])

#Puedo aplicar agrupaciones (Agrupar datos numericos y strings)
#print(tablaOrenada.groupby('producto')['total'].sum())
#print(tablaOrenada.groupby('vendedor')['total'].sum())
#print(tablaOrenada.groupby('fecha')['total'].sum().head(31))


#######################################################################################################
#Transformando datos con pandas
#Aplicando filtros o data queris


#Yo puedo obtener de lo9s datos las ventas realizadas en enero de 2025
queryUno=tablaOrenada.query("fecha >= '2025-01-01' and fecha <='2025-01-31'")

#Yo como administrador del punto de ventas puedo ver o obtener la cantidad mayor o igual a 3 de productos vendidos
queryDos=tablaOrenada.query("cantidad >= 3")

#Yo como adminstrador del punto de venta puedo ver las ventas del producto camiseta polo
queryTres=tablaOrenada.query("producto == 'Camiseta Polo'")

#Yo puedo obtener las ventas de tallas de m o l
queryCuatro=tablaOrenada.query("talla.isin (['M','L'])")

#yo como lider de bodega puedo acceder a los productos cuyo precio unitario este entre 150000 y 300000
queryCinco=tablaOrenada.query("precioUnitario >= 150000 and precioUnitario <=300000")

#yo como administrador del punto de venta puedo ver las ventas realizadas por el vendedor juan pablo gil
querySeis=tablaOrenada.query("vendedor == 'Juan Pablo Gil'")

#yo puedo obtener las ventas de los fines de semana
#crear una columna con el numero del dia de la semana (0-lunes,6-domingo)
#tablaOrenada['diaSemana']=pd.to_datetime(tablaOrenada['fecha']).dt.dayofweek
tablaOrenada["fecha"]=pd.to_datetime(tablaOrenada["fecha"])
tablaOrenada['diaSemana']=tablaOrenada["fecha"].dt.day_of_week
querySiete=tablaOrenada.query("diaSemana == 5 and diaSemana ==6")

#yo puedo ver ventas cuyo total se mayor a un millon
queryOcho=tablaOrenada.query("total > 1000000")

#yo quiero ver totas las ventas de todos los producto excluyendo las camisas polo
queryNueve=tablaOrenada.query("producto != 'Camiseta Polo'")

#yo puedoi ver las ventas entre 2 fechas especificas
queryDies=tablaOrenada.query("fecha >= '2025-01-01' and fecha <= '2025-03-31'")


#Estudiantes
#yo quiero ver ventas con cantidad mayor que 10 y total mayor a 600000
#filtroCantidadTotal=(tablaOrenada['cantidad']>10) & (tablaOrenada['total']>600000)
#ver ventas de productos que contengan la palabra camisas
#filtroProductoCamisas=tablaOrenada['producto'].str.contains('Camisa')
#ver ventas de vendedores cuyo nombre contiene la palabra juan
#filtroVendedorJuan=tablaOrenada['vendedor'].str.contains('Juan')
#Obtener las ventas con precio unitario mayor al promedio general
#filtroPrecioPromedio=tablaOrenada['precioUnitario']>tablaOrenada['precioUnitario'].mean()
#Obtener las ventas con total mayor al doble del precio unitario
#filtroTotalDoblePrecio=tablaOrenada['total']>2*tablaOrenada['precioUnitario']
#ventas de pantalon p jen ajustado con cantidad mayor o igual a 2
#filtroProductoPantalonCantidad= (tablaOrenada['producto']=='Pantalones') & (tablaOrenada['cantidad']>=2)
#ver ventas mayor a 400000
#filtroTotalMayor400k=tablaOrenada['total']>400000
#ventas de todos menos las de pablo gil
#filtroVendedorNoPablo=tablaOrenada['vendedor']!='Juan Pablo Gil'
#ventas ordenadas por total desendente
#filtroVentasOrdenadas=tablaOrenada.sort_values(by='total',ascending=False)


#Graficas a generar
#total de ventas por producto
#total de ventas por vendedor
#total de ventas con cantidad >=3
#total de ventas de producto caro (precio unitario >400000)