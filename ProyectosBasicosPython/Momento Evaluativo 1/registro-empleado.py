from funciones import buscarEmpleadoPorId, eliminarEmpleadoId

opcionMenu = 150
empleados = []

while opcionMenu != 0:
    print("!!!!!!!!!!!!!!!!!!!!!!!!Registro Empleados!!!!!!!!!!!!!!!!!!!!!!!!")
    print('Menu de opciones')
    print('1.Registrar empleado')
    print('2.Mostrar todo los empleados')
    print('3.Ver el total de la nomina')
    print('4.Eliminar empleado por ID')
    print('0.Salir')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    opcionMenu = int(input('Ingrese una opcion: '))
    
    
    
    if opcionMenu == 1:
        print('Registrar empleado')
        empleado = {}  
        print('Ingresando un empleado')
        empleado['id'] = int(input('Digita el id del empleado a ingresar: '))
        empleado['nombre'] = input('Digita el nombre del empleado a ingresar: ')
        empleado['correo'] = input('Digita el correo del empeado a ingresar: ')
        empleado['telefono'] = input('Digite el telefono del empleado a ingresar: ')
        empleado['valorHora'] = float(input('Digite el valor por hora que le pagan: '))
        empleado['horasTrabajadas'] = int(input('Digite las horas que el empleado trabaja: '))
        empleado['cargo'] = input('Digite el cargo del empleado: ')
        empleados.append(empleado) 
        print('Empleado agregado con exito \n')
        print('-----------------------------------')
        
    elif opcionMenu == 2:
        print('Mostrar empleados')
        
        print('Mostrando los empleados de la empresa: ')
        
        for empleadoSeleccionado in empleados:
            
            print('Nombre: ', empleadoSeleccionado['nombre'])
            print('Cargo: ', empleadoSeleccionado['cargo'])
            salario = empleadoSeleccionado["horasTrabajadas"]*empleadoSeleccionado["valorHora"]
            print( f'El salario de empleado es de {salario}')
        if len(empleados) == 0:
            print('No hay empleados ingresados')
            print('-----------------------------------') 
            
    elif opcionMenu == 3:
        print('Calcular total de la nomina')
        totalNomina = 0
        nombre = " "
        for empleado in empleados:
            nombre = empleado["nombre"]
            horas = empleado['horasTrabajadas']
            valorHora = empleado["valorHora"]
            subtotal = valorHora * horas
            totalNomina = subtotal*30
        print( f'La nomina de {nombre} es de un total de {totalNomina}')
        print('-----------------------------------')
        if len(empleados) == 0:
            print('No hay empleados en el sistema')
            print('-----------------------------------') 
            
    elif opcionMenu == 4:
        print('Eliminar empleado por ID')
        idBuscar=int(input('Digita el Id del empleado a eliminar: '))
        if eliminarEmpleadoId(empleados, idBuscar):
            print('Empleado eliminado con exito')
            print('-----------------------------------')
        else:
            print('Empleado no encontrado')  
            print('-----------------------------------')  
        
    elif opcionMenu == 0: 
        print('-----------------------------------')
        print('Saliendo del programa, hasta pronto') 
        print('-----------------------------------')  
        break
    else:
        print('Opcion no valida, intente de nuevo')