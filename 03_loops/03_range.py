###
# 03 - range()
# Permite crear una secuencia de números, que se puede usar para iterar sobre ella.
###

import os
os.system("cls")

# print("Range()") #No crea una lista, sino un objeto iterable que genera los números bajo demanda.

# nums = range(5) #Crea una secuencia de números del 0 al 4.
# print(nums) #Imprime el objeto range, no la lista de números.

# for num in range(5): #Itera sobre la secuencia de números generada por range(5).
#     print(num) #Imprime los números del 0 al 4, uno por línea.
    
# range(inicio, fin) #Crea una secuencia de números desde 'inicio' hasta 'fin - 1'.
# for num in range(1, 5): #Itera sobre la secuencia de números del 1 al 4.
#     print(num) #Imprime los números del 1 al 4, uno por línea.

# range(inicio, fin, paso) #Crea una secuencia de números desde 'inicio' hasta 'fin - 1', con un paso específico.
# for num in range(0, 10, 2): #Itera sobre la secuencia de numeros del 0 al 8, con un paso de 2.
#     print(num) #Imprime los números pares del 0 al 8, uno por línea.

# for num in range(-5, 0): #Itera sobre la secuencia de números del -5 al -1.
#     print(num) #Imprime los números del -5 al -1, uno por línea.

# for num in range(10, 0, -1): #Itera sobre la secuencia de números del 10 al 1, con un paso de -1.
#     print(num) #Imprime los números del 10 al 1, uno por línea.

# Convertir un objeto range en una lista
# num = range(10)
# list_of_nums = list(num) #Convierte el objeto range en una lista de números.
# print(list_of_nums) #Imprime la lista de números del 0 al 9.

# Hacer algo 5 veces usando range()
contador = 0
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
    
for _ in range(6): #Usamos un guion bajo (_) como variable de iteración cuando no necesitamos usar el valor de la variable.
    print(f"Contador: {_}") #Imprime el contador del 0 al 5, uno por línea.