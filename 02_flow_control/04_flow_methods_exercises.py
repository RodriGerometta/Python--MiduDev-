###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

import os

os.system("cls")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# numeros = [1, 2, 3, 4, 5] # Crea una lista con los números del 1 al 5
# numeros.append(6) # Añade el número 6 al final usando append()
# numeros.insert(2, 10) # Inserta el número 10 en la posición 2 usando insert()
# numeros[0] = 0 # Modifica el primer elemento de la lista para que sea 0
# print(numeros) # Imprime la lista resultante

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# lista_a = [1, 2, 3] # Crea la primera lista
# lista_b = [4, 5, 6, 1, 2] # Crea la segunda lista
# print("Lista A inicial:", lista_a) # Imprime la lista A inicial
# print("Lista B inicial:", lista_b) # Imprime la lista B inicial
# lista_a.extend(lista_b) # Extiende lista_a con lista_b usando extend()
# print("Lista A después de extend:", lista_a) # Imprime la lista A después de extenderla
# lista_a.remove(1) # Elimina la primera aparición del número 1 en lista_a usando remove()
# print("Lista A después de remove(1):", lista_a) # Imprime la lista A después de eliminar el número 1
# eliminado = lista_a.pop(3) # Elimina el elemento en el índice 3 de lista_a usando pop() y guarda el elemento eliminado
# print("Lista A después de pop(3):", lista_a) # Imprime la lista A después de eliminar el elemento en el índice 3
# print("Elemento eliminado con pop(3):", eliminado) # Imprime el elemento eliminado con pop(3)
# lista_b.clear() # Limpia completamente lista_b usando clear()
# print("Lista A después de las operaciones:", lista_a) # Imprime la lista A después de las operaciones
# print("Lista B después de clear():", lista_b) # Imprime la lista B después de las operaciones

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Crea una lista con los números del 1 al 10
# del numeros[2:5]  # Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5)
# print(numeros)  # Imprime la lista resultante

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# numeros = [5, 2, 8, 1, 9, 4, 2]  # Crea una lista con los números dados
# print("Lista original:", numeros)  # Imprime la lista original
# numeros.sort()  # Ordena la lista de forma ascendente usando sort()
# print("Lista ordenada:", numeros)  # Imprime la lista ordenada
# contar = numeros.count(2)  # Cuenta cuántas veces aparece el número 2 en la lista usando count()
# print("Número de veces que aparece el número 2:", contar)  # Imprime el conteo del número 2
# print("¿El número 7 está en la lista?", 7 in numeros)  # Comprueba si el número 7 está en la lista usando in

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# original = [1, 2, 3]  # Crea la lista original
# copia_1 = original[:]  # Crea una copia de la lista original usando slicing
# copia_2 = original.copy()  # Crea otra copia usando copy()
# referencia = original  # Crea una referencia a la lista original
# referencia[0] = 10  # Modifica el primer elemento de la lista referencia a 10
# print("Lista original:", original)  # Imprime la lista original
# print("Copia 1 (slicing):", copia_1)  # Imprime la copia creada con slicing
# print("Copia 2 (copy()):", copia_2)  # Imprime la copia creada con copy()
# print("Referencia:", referencia)  # Imprime la referencia a la lista original

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

frutas = ["Manzana", "pera", "BANANA", "naranja"]  # Crea una lista con las cadenas dadas
print("Lista original:", frutas)  # Imprime la lista original
frutas.sort(key=str.lower)  # Ordena la lista sin diferenciar entre mayúsculas y minúsculas usando sort() con key=str.lower
print("Lista ordenada sin diferenciar mayúsculas y minúsculas:", frutas)  # Imprime la lista ordenada