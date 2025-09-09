from funciones import buscarProductoPorId, eliminarProductoId

# Gestionar el inventario de una tienda online
# producto -> id, nombre, descripcion, precioUnitario, cantidadBodega
# Generar a traves cli 
# Menu 
# 1.Registrar producto 
# 2.Mostrar de forma ordenada e individual cada producto 
# 3.Calcular el costo total del inventario 
# 4.Mostrar producto en especifico (buscar por id) 
# 5.Permitir eliminar de la bodega todos los pruductor asociados en un ID especifico 
# 0.Salir 

# Uso de variables y estructuras de datos

opcionMenu = 150
productos = []

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
    
    # Zona de comparacion
    
    if opcionMenu == 1:
        print('Registrar producto')
        # Debo crear un diccionario desde cero para almacenar la informacion de cada producto
        producto = {}  # Crear nuevo diccionario
        print('Ingresando un producto')
        producto['id'] = int(input('Digita el id del producto a ingresar: '))
        producto['nombre'] = input('Digita el nombre del producto a ingresar: ')
        producto['descripcion'] = input('Digita la descripcion del producto a ingresar: ')
        producto['fotografia'] = input('Ingrese la fotografia del producto a ingresar: ')
        producto['precioUnitario'] = float(input('Digita precio unitario del producto a ingresar: '))
        producto['cantidadBodega'] = int(input('Digita cantidad en bodega del producto a ingresar: '))

        productos.append(producto)  # Lista que se carga con diccionario
        print('Producto adregado con exito \n')
        print('-----------------------------------')
        
    elif opcionMenu == 2:
        print('Mostrar productos')
        # Debo mostrar los productos de forma ordenada 
        print('Mostrando los productos en bodega: ')
        
        for productoSeleccionado in productos:
            print('ID: ', productoSeleccionado['id'])
            print('Nombre: ', productoSeleccionado['nombre'])
            print('Descripcion: ', productoSeleccionado['descripcion'])
            print('Fotografia: ', productoSeleccionado['fotografia'])
            print('Precio Unitario: ', productoSeleccionado['precioUnitario'])
            print('Cantidad en Bodega: ', productoSeleccionado['cantidadBodega'])
            print('-----------------------------------')
        if len(productos) == 0:
            print('No hay productos en la bodega')
            print('-----------------------------------') 
            
    #si no hay productos en la bodega, mostrar un mensaje que no hay productos        
    elif opcionMenu == 3:
        print('Calcular costo total del inventario')
        # codigo para calcular costo total
        total = 0
        for producto in productos:
            precio = producto['precioUnitario']
            cantidad = producto['cantidadBodega']
            subtotal = precio * cantidad
            total = total + subtotal
            print('Producto:', producto['nombre'], '- Subtotal:', subtotal)
        print('El costo total del inventario es:', total)
        print('-----------------------------------')
        if len(productos) == 0:
            print('No hay productos en la bodega')
            print('-----------------------------------') 
        
    elif opcionMenu == 4:
        print('Mostrar producto en especifico')
        idBuscar=int(input('Digita el Id del producto a buscar: '))
        productoEncontrado = buscarProductoPorId(productos, idBuscar)
        print(productoEncontrado)
        #Si el producto encontrado es none devolver un mensaje de no encontrado
            
    elif opcionMenu == 5:
        print('Eliminar producto por ID')
        idBuscar=int(input('Digita el Id del producto a eliminar: '))
        if eliminarProductoId(productos, idBuscar):
            print('Producto eliminado con exito')
            print('-----------------------------------')
        else:
            print('Producto no encontrado')  
            print('-----------------------------------')  
        
    elif opcionMenu == 0: 
        print('-----------------------------------')
        print('Saliendo del programa, hasta pronto') 
        print('-----------------------------------')  
        break
    else:
        print('Opcion no valida, intente de nuevo')