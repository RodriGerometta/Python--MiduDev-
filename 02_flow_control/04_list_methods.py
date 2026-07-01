###
# 04 - List Methods
# Los metodos mas importantes para trabajar con listas
###

import os
os.system("cls")

# lista1 = [1, 2, 3, 4, 5]

# # Agregar elementos a una lista
# print("\nAgregar elementos a una lista")
# print("Lista Original:", lista1) # [1, 2, 3, 4, 5]
# lista1.append(6)  # Agrega el elemento 6 al final de la lista
# print("Después de append(6):", lista1)  # [1, 2, 3, 4, 5, 6]

# # Insertar elementos en una posición específica
# print("\nInsertar elementos en una posición específica")
# print("Lista Original:", lista1) # [1, 2, 3, 4, 5, 6]
# lista1.insert(2, 2.5)  # Inserta el elemento 2.5 en el índice 2
# print("Después de insert(2, 2.5):", lista1)  # [1, 2, 2.5, 3, 4, 5, 6]

# # Agregar varios elementos a una lista
# print("\nAgregar varios elementos a una lista")
# print("Lista Original:", lista1) 
# lista1.extend([7, 8, 9])  # Agrega los elementos 7, 8 y 9 al final de la lista
# print("Después de extend([7, 8, 9]):", lista1) # [1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9]

# # Eliminar elementos de una lista
# # Con "Remove" se elimina el primer elemento que coincida con el valor especificado, si no se encuentra el valor se genera un error
# print("\nEliminar elementos de una lista")
# print("Lista Original:", lista1) # [1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9]
# lista1.remove(2.5)  # Elimina el primer elemento con el valor 2.5
# print("Después de remove(2.5):", lista1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Con "Pop" se elimina el ultimo elemento de la lista, si se especifica un indice se elimina el elemento en esa posicion, si el indice no existe se genera un error
# print("\nEliminar elementos de una lista con pop")
# print("Lista Original:", lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ultimo = lista1.pop()  # Elimina el último elemento de la lista y lo devuelve
# print("Después de pop():", lista1)  # [1, 2, 3, 4, 5, 6, 7, 8]
# print("Elemento eliminado con pop():", ultimo)  # 9

# print("\nEliminar elementos de una lista con pop especificando un indice")
# print("Lista Original:", lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# eliminado = lista1.pop(1) # Elimina el elemento en el índice 1 (en este caso el número 2) y lo devuelve
# print("Después de pop(1):", lista1)  # [1, 3, 4, 5, 6, 7, 8, 9]
# print("Elemento eliminado con pop(1):", eliminado)  # 2

# # Con "Del" se elimina el elemento en la posicion especificada, si el indice no existe se genera un error
# print("\nEliminar elementos de una lista con 'Del'")
# print("Lista Original:", lista1) # [1, 3, 4, 5, 6, 7, 8, 9]
# del lista1[0]  # Elimina el elemento en el índice 0 (en este caso el número 1)
# print("Después de 'Del' lista1[0]:", lista1)  # [3, 4, 5, 7, 8]

# # Con "Del" se puede eliminar un rango de elementos utilizando slicing, si el rango no es valido se genera un error
# print("\nEliminar un rango de elementos de una lista con 'Del'")
# print("Lista Original:", lista1) # [3, 4, 5, 7, 8]
# del lista1[1:3]  # Elimina los elementos desde el índice 1 hasta el 2 (excluyendo el 3) 
# print("Después de 'Del' lista1[1:3]:", lista1)  # [3, 7, 8]

# # Eliminar todos los elementos de una lista con "Clear"
# print("\nEliminar todos los elementos de una lista con 'Clear'")
# print("Lista Original:", lista1) # [3, 7, 8]
# lista1.clear()  # Elimina todos los elementos de la lista
# print("Después de clear():", lista1)  # []

# # Metodos para ordenar y contar elementos en una lista
# # Modificando la lista original con "Sort" y "Reverse"
# print("\nMétodos para ordenar y contar elementos en una lista")
# numbers = [5, 2, 9, 1, 5, 6]
# print("Lista Original:", numbers) # [5, 2, 9, 1, 5, 6]
# numbers.sort()  # Ordena la lista en orden ascendente
# print("Después de sort():", numbers)  # [1, 2, 5, 5, 6, 9]
# numbers.reverse()  # Invierte el orden de la lista
# print("Después de reverse():", numbers)  # [9, 6, 5, 5, 2, 1]

# # Crear una nueva lista ordenada con "Sorted" sin modificar la lista original "Creando una copia"
# numbers2 = sorted(numbers)  # Crea una nueva lista ordenada en orden ascendente
# print("Lista Original:", numbers) # [9, 6, 5, 5, 2, 1]
# print("Nueva lista ordenada con sorted():", numbers2)  # [1, 2, 5, 5, 6, 9]

# # Ordenar una lista de cadenas de texto todo en minusculas con "Sort" y "Sorted"
# print("\nOrdenar una lista de cadenas de texto todo en minusculas con 'Sort' y 'Sorted'")
# frutas = ["manzana", "pera", "plátano", "naranja"]
# print("Lista Original:", frutas) # ['manzana', 'pera', 'plátano', 'naranja']
# frutas.sort()  # Ordena la lista en orden alfabético
# print("Después de sort():", frutas)  # ['manzana', 'naranja', 'pera', 'plátano']
# frutas2 = sorted(frutas)  # Crea una nueva lista ordenada en orden
# print("Lista Original:", frutas) # ['manzana', 'naranja', 'pera', 'plátano']
# print("Nueva lista ordenada con sorted():", frutas2)  # ['manzana', 'naranja', 'pera', 'plátano']

# # Ordenar una lista de cadenas de texto con mayusculas y minusculas con "Sort" y "Sorted"
# print("\nOrdenar una lista de cadenas de texto con mayusculas y minusculas con 'Sort' y 'Sorted'")
# frutas_mixtas = ["Manzana", "pera", "Plátano", "naranja"]
# print("Lista Original:", frutas_mixtas) # ['Manzana', 'pera', 'Plátano', 'naranja']
# frutas_mixtas.sort()  # Ordena la lista en orden alfabético, las mayúsculas se ordenan antes que las minúsculas
# print("Después de sort():", frutas_mixtas)  # ['Manzana', 'Plátano', 'naranja', 'pera']
# frutas_mixtas2 = sorted(frutas_mixtas)  # Crea una nueva lista ordenada en orden alfabético, las mayúsculas se ordenan antes que las minúsculas
# print("Lista Original:", frutas_mixtas) # ['Manzana', 'Plátano', 'naranja', 'pera']
# print("Nueva lista ordenada con sorted():", frutas_mixtas2)  # ['Manzana', 'Plátano', 'naranja', 'pera']

# # Ordenar la lista de cadenas de texto con mayusculas y minusculas utilizando el parametro "key" con "Sort" y "Sorted"
# print("\nOrdenar la lista de cadenas de texto con mayusculas y minusculas utilizando el parametro 'key' con 'Sort' y 'Sorted'")
# frutas_mixtas3 = ["Manzana", "pera", "Plátano", "naranja"]
# print("Lista Original:", frutas_mixtas3) # ['Manzana', 'pera', 'Plátano', 'naranja']
# frutas_mixtas3.sort(key=str.lower)  # Ordena la lista en orden alfabético ignorando mayúsculas y minúsculas
# print("Después de sort() con key=str.lower:", frutas_mixtas3)  # ['Manzana', 'naranja', 'pera', 'Plátano']
# frutas_mixtas4 = sorted(frutas_mixtas3, key=str.lower)  # Crea una nueva lista ordenada en orden alfabético ignorando mayúsculas y minúsculas
# print("Lista Original:", frutas_mixtas3) # ['Manzana', 'naranja', 'pera', 'Plátano']
# print("Nueva lista ordenada con sorted() con key=str.lower:", frutas_mixtas4)  # ['Manzana', 'naranja', 'pera', 'Plátano']

# # Contar elementos con "Count". El metodo "Count" cuenta el numero de veces que un elemento aparece en la lista, si el elemento no se encuentra en la lista devuelve 0
# print("\nContar elementos en una lista con 'Count'")
# print("Lista Original:", numbers) # [9, 6, 5, 5, 2, 1]
# contar = numbers.count() 
# print("Número de elementos en la lista:", contar)  # 6

# Longitud de una lista con "Len"
print("\nLongitud de una lista con 'Len'")
numbers = [9, 6, 5, 5, 2, 1]
print("Lista Original:", numbers) # [9, 6, 5, 5, 2, 1]
longitud = len(numbers)
print("Número de elementos en la lista:", longitud)  # 6

# in y not in para verificar si un elemento existe en una lista
print("\nVerificar si un elemento existe en una lista con 'in' y 'not in'")
print("Lista Original:", numbers) # [9, 6, 5, 5, 2, 1]
print("¿El número 5 está en la lista?", 5 in numbers)  # True
print("¿El número 10 está en la lista?", 10 in numbers)  # False
print("¿El número 5 no está en la lista?", 5 not in numbers)  # False
print("¿El número 10 no está en la lista?", 10 not in numbers)  # True
