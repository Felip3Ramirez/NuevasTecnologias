#gestionar el inventario de una tienda online
#producto -> id, nombre, descripcion, precioUnitario, cantidadBodega
#Generar a traves cli 
#Menu 
# 1.Registrar producto 
# 2.Mostrar de forma ordenada e individual cada producto 
# 3.Calcular el costo total del inventario 
# 4.Mostrar producto en especifico (buscar por id) 
# 5.Permitir eliminar de la bodega todos los pruductor asociados en un ID especifico 
# 0.Salir 

#Uso de variables y estructuras de datos

#Repetir unas salidas en pantalla

opcionMenu = 150
producto ={}
productos=[]
while opcionMenu != 0:
    print("!!!!!!!!!!!!!!!!!!!!!!!!Aplicacion!!!!!!!!!!!!!!!!!!!!!!!!")
    print('Menu de opciones')
    print('1.Registrar producto')
    print('2.Mostrar productos')
    print('3.Calcular costo total del inventario')
    print('4.Mostrar producto en especifico')
    print('5.Eliminar producto por ID')
    print('0.Salir')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    opcionMenu = int(input('Ingrese una opcion: '))
    
    #Zona de comparacion
    
    if opcionMenu == 1:
        print('Registrar producto')
        #Debo crear un diccionario desde cero para almacenar la informacion de cada producto
        print('Ingresando un producto')
        producto ['id']=input('Digita el id del producto a ingresar: ')
        producto ['nombre']=input('Digita el nombre del producto a ingresar: ')
        producto ['descripcion']=input('Digita la descripcion del producto a ingresar: ')
        producto ['fotografia']=input('Ingrese la fotografia del producto a ingresar: ')
        producto ['precioUnitario']=input=float(('Digita precio unitario del producto a ingresar: '))
        producto ['cantidadBodega']=input=int(('Digita cantidad en bodega del producto a ingresar: '))

        productos.append(producto) #Lista que se carga con diccionario
        print('Producto adregado con exito \n')
    elif opcionMenu == 2:
        print('Mostrar productos')
        #Debo mostrar los productos de forma ordenada 
        print('Mostrando los productos en bodega: ')
        for productoSeleccionado in productos:
            print('ID: ', productoSeleccionado['id'])
            print('Nombre: ', productoSeleccionado['nombre'])
            print('Descripcion: ', productoSeleccionado['descripcion'])
            print('Fotografia: ', productoSeleccionado['fotografia'])
            print('Precio Unitario: ', productoSeleccionado['precioUnitario'])
            print('Cantidad en Bodega: ', productoSeleccionado['cantidadBodega'])
            print('-----------------------------------')
            
            
    elif opcionMenu == 3:
        print('Calcular costo total del inventario')
        #TAREA  cantidad y precio 
        #codigo para calcular costo total
    elif opcionMenu == 4:
        print('Mostrar producto en especifico')
        #codigo para mostrar producto por ID
    elif opcionMenu == 5:
        print('Eliminar producto por ID')
        #codigo para eliminar producto por ID
    elif opcionMenu == 0:
        print('Salir')
        break
    else:
        print('Opcion no valida, intente de nuevo')
