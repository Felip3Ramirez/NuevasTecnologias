#Traer un registro de N ventas para analizar con pandas
#Primeros pasos con pandas

from data.listasSimuladas import generar_ventas

import pandas as pd

datos_simulados=generar_ventas(1000)

#Organizando la fuente de datos con pandas

tablaOrenada=pd.DataFrame(datos_simulados)

#Informacion general
#print(tablaOrenada.info)

#Obtener la informacion estadistica basica (descriptiva)
#print(tablaOrenada.describe())

#Obtener la informacion de los primeros 20 registros
#print(tablaOrenada.head(20))

#Obtener la informacion de los ultimos n registros
#print(tablaOrenada.taicantidad

#Acceder a una columna seleccionar  en especifico
#print(tablaOrenada['vendedor'])

#Tarea como hago para acceder a varias columnas al mismo tiempo
print(tablaOrenada[['cantidad','vendedor','total']])

#Puedo aplicar agrupaciones (Agrupar datos numericos y strings)
#print(tablaOrenada.groupby('producto')['total'].sum())
#print(tablaOrenada.groupby('vendedor')['total'].sum())
#print(tablaOrenada.groupby('fecha')['total'].sum().head(31))
