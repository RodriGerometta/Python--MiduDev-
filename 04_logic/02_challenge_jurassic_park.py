"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

import os
os.system("cls")

lista_huevos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def suma_huevos(lista):
    suma_total = 0
    suma_pares = 0
    for huevo in lista:
        suma_total += huevo
        if huevo % 2 == 0: 
            suma_pares += huevo            
    
    print(f"Suma total de huevos: {suma_total}")
    print(f"Suma total huevos de dinosaurios carnivoros (pares): {suma_pares}")
    
    return suma_pares
    
suma_huevos(lista_huevos)