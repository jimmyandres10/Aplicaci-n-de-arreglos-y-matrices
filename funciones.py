def ultimos(p):
    p[4][6]=0
    p[4][5]=0
    p[4][4]=0
    p[4][3]=0
    return p

def dias(x):
    diccionario = {0:"lunes",1:"martes",2:"miercoles",3:"jueves",4:"viernes",5:"sabado",6:"domingo"}
    dia = diccionario[x]
    return dia

def mayor_semana(x):
    for i in range(5): 
        mayor_de_la_semana = max(x[i])
        for j in range(7):
            if mayor_de_la_semana == x[i][j]:
                dia=dias(j)

        print(f"la mayor temperatura en la semana {i+1}  es: {mayor_de_la_semana} el {dia}")



def menor_semana(x):
    for i in range(4): 
        menor_de_la_semana = min(x[i])
        for j in range(7):
            if menor_de_la_semana == x[i][j]:
                dia=dias(j)
        
        print(f"la menor temperatura en la semana {i+1}  es: {menor_de_la_semana} el {dia}")


def menor_semana5(x):
    for i in len(mes[4,0:-4]): 
        menor_de_la_semana5 = min((mes[4,0:-4]))
        for j in range(3):
            if menor_de_la_semana5 == x[i][j]:
                dia=dias(j)
        
        print(f"la menor temperatura en la semana 5  es: {menor_de_la_semana5} el {dia}")
        



def sumalista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])


def numero_dia(x):
    if x%7==0:
        s=int(x/7)-1
    else:
        s=int(x/7)

    f=s*7
    ds= x-f
    if ds == 7:
        ds=0
    return ds

def mayor_y_menor_del_mes(x):
    import numpy as np
    valormx=x.max()
    numero=numero_dia(np.argmax(x))
    dia=dias(numero)
    print(f"el valor maximo del mes fue: {valormx} un {dia}")
    print("")
    valormn=x.min()
    numero2=numero_dia(np.argmin(x))
    dia2=dias(numero2)
    print(f"el valor minimo del mes fue: {valormn} un {dia2}")
    print("")


def promedio_max(x):
    promediomaximo=0
    for i in range(5):
        suma=0
        
        if i != 4:
            for j in range(7):
                suma+=x[i][j]

            promedio=suma/7
        else:
            for j in range(3):
                suma+=x[i][j]
            promedio=suma/3

        if promediomaximo < promedio:
            promediomaximo = promedio
            semana=i

    print(f"la semana mas calurosa fue la semana  {semana} con una temperatura promedio de: {promediomaximo}")
    print("")

def dia_a_cambiar(x):
    y =int(input("digite el numero del dia que quiere cambiar: "))
    print("")
    valor=input("ingrese la nueva temperatura: ")
    print("")

    if y%7==0:
        s=int(y/7)-1
    else:
        s=int(y/7)

    f=s*7
    ds= y-f-1
    x[s][ds]=valor








