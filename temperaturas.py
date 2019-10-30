import numpy as np
import random
import funciones

nom = ( "  L  M  MI  J  V  S  D " )
x = np.random.randint(18, 34, size=(5, 7))
mes = funciones.ultimos(x)
print(mes)

print(funciones.mayor_semana(mes))
print(funciones.menor_semana(mes))
print()

semana1 = mes[0,0:7]
suma1 = funciones.sumalista(semana1)
print(f"Promedio semana 1{suma1/7}")

semana2 = mes[1,0:7]
suma2 = funciones.sumalista(semana2)
print(f"Promedio semana 2{suma2/7}")

semana3 = mes[2,0:7]
suma3 = funciones.sumalista(semana3)
print(f"Promedio semana 3{suma3/7}")

semana4 = mes[3,0:7]
suma4 = funciones.sumalista(semana4)
print(f"Promedio semana 4{suma4/7}")

semana5 = mes[4,0:-4]
suma5 = funciones.sumalista(semana5)
print(f"Promedio semana 5{suma5/3}")

funciones.mayor_y_menor_del_mes (mes)
funciones.promedio_max (mes)
print( " El mes normal " )
print(nom)
print(mes)
print( " " )
funciones.dia_a_cambiar (mes)
print( " El mes con los cambios " )
print( " " )
print(nom)
print(mes)



        






