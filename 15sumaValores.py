import os
os.system('cls' if os.name=='nt' else 'clear')

#programa que pide 10 valores y los suma

#acumulador
acumulador=0
for i in range(10):
    num=float(input(f"Ingrese un numero[{i+1}]: "))
    acumulador+=num
print(acumulador)