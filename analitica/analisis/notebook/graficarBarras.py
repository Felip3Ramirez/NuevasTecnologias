
import matplotlib.pyplot as plt
import os

def generarBarra(tablaOrdenada, columnaX, columnaY, titulo, nombreArchivo=None):
    
    colores=[
        "#845ec2",
        "#d65db1",
        "#ff6f91",
        "#ff9671",
        "#ffc75f"
    ]
    
    agrupacionDatos=tablaOrdenada.groupby(columnaX)[columnaY].sum()
    plt.figure(figsize=(10,5))
    plt.bar(agrupacionDatos.index,agrupacionDatos.values,color=colores)
    plt.title(titulo)
    plt.xlabel(columnaX)
    plt.ylabel(columnaY)
    
    #guardar la grafica ANTES de mostrarla
    if nombreArchivo:
        #crear la carpeta si no existe
        carpeta = os.path.dirname(nombreArchivo)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"Carpeta creada: {carpeta}")
        
        plt.savefig(nombreArchivo, bbox_inches='tight', dpi=300)
        print(f"Grafica guardada en: {nombreArchivo}")
    
    plt.show()
    plt.close() #cerrar la figura para liberar memoria