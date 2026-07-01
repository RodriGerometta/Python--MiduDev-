###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementos de cualquier tipo
###

import os

os.system("cls")  # Limpiar la consola (en Windows)

# # Crear una lista
# print("\nCrear listas")
# lista1 = [1, 2, 3, 4, 5]  # Lista de enteros
# lista2 = ["manzanas", "peras", "platanos"]  # lista de cadenas
# lista3 = [1, "manzanas", 3.14, True]  # lista mixta

# lista_vacia = []  # lista vacía
# lista_de_listas = [[1, 2], [3, 4], [5, 6]]  # lista de listas
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matriz (lista de listas)

# print("Lista de enteros:", lista1)
# print("Lista de cadenas:", lista2)
# print("Lista mixta:", lista3)
# print("Lista vacía:", lista_vacia)
# print("Lista de listas:", lista_de_listas)
# print("Matriz:", matriz)


# # Acceder a elementos de una lista por indice
# print("\nAcceder a elementos de una lista por indice")
# print(lista2[0])  # Primer elemento ("manzanas")
# print(lista2[1])  # Segundo elemento ("peras")
# print(lista2[2])  # Tercer elemento ("platanos")
# print(lista2[-1])  # Último elemento ("platanos")
# print(lista2[-2])  # Penúltimo elemento ("peras")

# # Acceder a elementos de una lista de listas/matriz
# print("\nAcceder a elementos de una lista de listas/matriz")
# print(lista_de_listas[0][1])  # Primera sublista ([1, 2])

# # Cambio de elementos en una lista
# # Slicing de listas
# lista_cambio = [1, 2, 3, 4, 5]
# print("lista_cambio original:", lista_cambio)
# print(lista_cambio[1:4])# Elementos desde el indice 1 hasta el 3 (excluyendo el 4) # [2, 3, 4]
# print(lista_cambio[:3]) # Elementos desde el inicio hasta el indice 2 (excluyendo el 3) # [1, 2, 3]
# print(lista_cambio[2:]) # Elementos desde el indice 2 hasta el final # [3, 4, 5]
# print(lista_cambio[:]) # Todos los elementos de la lista # [1, 2, 3, 4, 5]

# # Paso
# print("\nPaso en slicing de listas")
# # print(lista_cambio[desde:hasta:paso])
# lista_paso = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("lista_paso original\n", lista_paso)
# print("lista_paso[::2]\n", lista_paso[::2])  # Elementos desde el inicio hasta el final con un paso de 2 # [0, 2, 4, 6, 8]
# print("lista_paso[::3]\n", lista_paso[::3])  # Elementos desde el inicio hasta el final con un paso de 3 # [0, 3, 6, 9]
# print("lista_paso[::-1]\n", lista_paso[::-1])  # Elementos desde el final hasta el inicio con un paso de -1 (reversa) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# # Modificar elementos de una lista
# print("\nModificar elementos de una lista")
# lista_modificar = [1, 2, 3, 4, 5]
# lista_modificar[0] = 20 # Cambiar el primer elemento a 20
# print("lista_modificar después de modificar el primer elemento\n", lista_modificar) # [20, 2, 3, 4, 5]

# # Añadir elementos a una lista
# print("\nAñadir elementos a una lista")
# lista_añadir = [1, 2, 3]
# print("lista_añadir original\n", lista_añadir)  # [1, 2, 3]

# # Forma larga y menos eficiente
# lista_añadir = lista_añadir + [4, 5, 6]  # Concatenar una nueva lista con los nuevos elementos
# print("lista_añadir después de concatenar\n", lista_añadir)  # [1, 2, 3, 4, 5, 6]

# # Forma corta y más eficiente
# lista_añadir += [7, 8, 9]  # Concatenar una nueva lista con los nuevos elementos usando el operador +=
# print("lista_añadir después de usar +=\n", lista_añadir)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Recupera longitud de una lista
print("\nRecupera longitud de una lista")
lista_longitud = [1, 2, 3, 4, 5]
print("Longitud de lista_longitud: ", len(lista_longitud))  # 5