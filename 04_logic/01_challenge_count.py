"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

import os
os.system("cls")

def ingresar_cadena():
    while True:
        texto = input("Ingrese una cadena de texto:").upper()
        if texto.strip() != "":
            contar_letras(texto)
            break
        else:
            print("Error: La cadena no puede estar vacía. Por favor, ingresa una cadena válida.")
            #continue 
        #break
    
    
    
def contar_letras(texto):
    count_r = texto.count("R")
    count_j = texto.count("J")
    print(f"Cantidad de R (Reed Richards): {count_r}")
    print(f"Cantidad de J (Johnny Storm): {count_j}")
    
    if count_r == count_j:
        print("La alianza entre Reed Richards y Johnny Storm está en equilibrio.")
        return True
    else:
        print("La alianza entre Reed Richards y Johnny Storm no está en equilibrio.")
        return False
    
ingresar_cadena()