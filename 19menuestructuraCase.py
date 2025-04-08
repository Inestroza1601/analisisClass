#menu sencillo
import os
os.system('cls' if os.name=='nt' else 'clear')

opcion=0
while opcion!=-1:
    print("1.- Suma | 2.- Ciclo For | -1.- Salir")
    # print("2.- Ciclo For")
    # print("-1.- Salir")
    opcion=int(input("Escoge una opción: "))
    match opcion:
        case 1:
            print("Suma")
            a=10
            b=20
            print(a+b)
        case 2:
            print("Ciclo For")
            for i in range(5):
                print(f"{i}")
        case _:
            print("opcion no valida")
print("Programa terminado Satisfactoriamente")