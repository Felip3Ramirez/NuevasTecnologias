
def buscarProductoPorId(listaProductos, idBusqueda):
    for productoSeleccionado in listaProductos:
        if productoSeleccionado['id'] == idBusqueda:
            return productoSeleccionado
        
    return 

def eliminarProductoId (listaProductos,idObjetivo):
    for productoSeleccionado in listaProductos:
        if productoSeleccionado['id'] == idObjetivo:
            listaProductos.remove(productoSeleccionado)
            return True
        else:
            print('No se encontro el producto a eliminar :',idObjetivo )
    return False

'''print('Mostrar producto en especifico')
        # codigo para mostrar producto por ID
        id_buscar = input('Digite el ID del producto que quiere ver: ')
        encontrado = False
        for producto in productos:
            if producto['id'] == id_buscar:
                print('Producto encontrado:')
                print('ID: ', producto['id'])
                print('Nombre: ', producto['nombre'])
                print('Descripcion: ', producto['descripcion'])
                print('Fotografia: ', producto['fotografia'])
                print('Precio Unitario: ', producto['precioUnitario'])
                print('Cantidad en Bodega: ', producto['cantidadBodega'])
                encontrado = True
        if encontrado == False:
            print('No se encontro el producto')
            
            
print('Eliminar producto por ID')
        # codigo para eliminar producto por ID
        id_eliminar = input('Digite el ID del producto que quiere eliminar: ')
        encontrado = False
        for i in range(len(productos)):
            if productos[i]['id'] == id_eliminar:
                print('Se va a eliminar:', productos[i]['nombre'])
                del productos[i]
                print('Producto eliminado')
                encontrado = True
                break
        if encontrado == False:
            print('No se encontro el producto')            '''