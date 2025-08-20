#Creando una lista de datos en python
#Las listas se nombran en plural

jugadores=["Juan","Raul","Manuel","Martin"]

#Agregando listad

jugadores.append("Carlos")
jugadores.append(input("Digita un nombre: "))

#Mostrando los datos de una lista

print(jugadores)


#Creando diccionarios en python

jugador = {
    "id":45,
    "nombre":"Edwin Cardona",
    "edad":40,
    "posicion":"Medio campista",
    "salarioMensual":200000000,
    "estaLesionado":True
    } #CLAVE : VALOR

#Como agrego un nuevo elemento a un diccionario

jugador["golesTemporada"]=6

#Mostrando los datos de un diccionario

print(jugador)
