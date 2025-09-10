
def buscarEmpleadoPorId(listaEmpleados, idBusqueda):
    for empleadoSeleccionado in listaProductos:
        if empleadoSeleccionado['id'] == idBusqueda:
            return empleadoSeleccionado
        
    return 

def eliminarEmpleadoId (listaEmpleados,idObjetivo):
    for empleadoSeleccionado in listaEmpleados:
        if empleadoSeleccionado['id'] == idObjetivo:
            listaEmpleados.remove(empleadoSeleccionado)
            return True
        else:
            print('No se encontro el empleado a eliminar :',idObjetivo )
    return False

