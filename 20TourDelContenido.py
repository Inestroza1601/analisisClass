#Menu tour de la clase de python 2025
def clear():
    import os
    os.system('cls' if os.name=='nt' else 'clear')
    
print("Tour de la clase de python 2025")
opcion = 0
while(opcion!=-1):
    print("Tour del contenido III paracial")
    print("1.- Tipos de Variables")
    print("2.- Operadores")
    print("3.- Operadores de Comparación")
    print("4.- Condicionales if")
    print("5.- Ciclo For")
    print("6.- Ciclo Wile")
    print("-1.- Salir")
    opcion=int(input("Escoge una opción: "))

    clear()

    match opcion:
        case 1:
            print("Tipos de Variables")
            print("Numericas: Enteras, flotantes o decimales o double")
            print("Texto o Cadena de caracteres, booleanas o logicas")
            input("\nEnter para continuar")
            clear()
        case 2:
            print("Operadores aritmeticos: +, -,*,/,**,%")
            input("\nEnter para continuar")
            clear()
        case 3:
            print("Operadores de comparacion: ==, <, >, <=, >=, != <>")
            print("Ademas: and &, or |, not que ayuda a los operadores de comparación.")
            input("\nEnter para continuar")
            clear()
        case 4:
            print("Condicional if")
            edad=20
            if edad>=21:
                print("Mayor de edad")
            else:
                print("Menor de edad")
            input("\nEnter para continuar")
            clear()
        case 5:
            print("Ciclo For")
            for i in range(5):
              print(i+1)
            input("\nEnter para continuar")
            clear()
        case 6:
            print("Que mas quiere?, si este programa esta corriendo con ")
            print("")
        case -1:
            print("Adios")
        case _:
            print("Opcion no valida")
            input("\nEnter para continuar")
            clear()