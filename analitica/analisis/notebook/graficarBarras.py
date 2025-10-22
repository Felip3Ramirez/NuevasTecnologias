import matplotlib.pyplot as plt

def generarBarra(tablaOrdenada, columnaX, columnaY, titulo):
    
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
    plt.show()