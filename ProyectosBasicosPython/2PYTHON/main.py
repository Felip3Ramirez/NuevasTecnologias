#Generando condicionales en python

nivelAgua=int(input('Nivel de agua medido por el sensor: '))

if nivelAgua>0 and nivelAgua<=200:
    print('Estoy operando en niveles muy bajos de agua')
elif nivelAgua>200 and nivelAgua<=450:
    print(f"El nivel de agua es{nivelAgua} por lo tanto operamos con normalidad")
elif nivelAgua>450:
    print('Peligro represa esta a punto de desbordarse')
else:
    print ('Nivel de agua no medido, por favor verificar el sensor')
    
#Operador ternario

