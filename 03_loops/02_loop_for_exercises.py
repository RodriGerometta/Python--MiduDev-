###
# EJERCICIOS (for)
###

import os

os.system("cls")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
# print("\nEjercicio 1:")
# numeros_pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] if num % 2 == 0]
# print("Numeros pares del 2 al 20:\n", numeros_pares)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
# print("\nEjercicio 2:")

# numeros = [10, 20, 30, 40, 50]
# cant_num = 0
# suma = 0
# for n in numeros:
#     cant_num += 1
#     suma += n

# media = suma / cant_num
# print(f"La suma de los elementos de la lista es: {suma} y la candidad de elementos de la lista es: {cant_num} por lo tanto la media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
# print("\nEjercicio 3:")

# numeros = [15, 5, 25, 10, 20]
# print("Lista de numeros:\n", numeros)
# maximo = 0
# for n in numeros:
#     if n > maximo:
#         maximo = n

# print(f"El numero maximo de la lista es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
# print("\nEjercicio 4:")

# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# palabras_largas = []
# for palabra in palabras:
#     if len(palabra) > 5:
#         palabras_largas += [palabra]

# print("Palabras originales:\n", palabras)
# print("Palabras con más de 5 letras:\n", palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

while True:
    try:
        letra = input("Introduce una letra para contar cuantas palabras empiezan con esa letra: ").lower()
        if letra.isalpha() and len(letra) == 1:
            break
    except Exception:
        print("Error al introducir la letra, por favor intenta de nuevo")
        continue 

contador = 0
coincidencias = []
for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1
        coincidencias += [palabra]

if contador == 0:
    print(f"No hay palabras que empiecen con la letra '{letra}'")
else:
    print(f"Has introducido la letra: '{letra}' y hay {contador} palabras que empiezan con esa letra, las palabras son:\n {coincidencias}")
        