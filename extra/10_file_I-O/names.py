import os
os.system("cls")  # Limpiar la consola (en Windows)

# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))
    
# for name in sorted(names):
#     print(f"Hello, {name}!")
    
# name = input("What is your name? ")

# with open("names.txt", "a") as file:  # Abrir el archivo en modo de adición (append)
#     file.write(name + "\n")  # Escribir el nombre en el archivo seguido de un salto de línea

# with open("names.txt", "r") as file:  # Abrir el archivo en modo de lectura
#     lines = file.readlines()  # Leer todas las líneas del archivo
    
# for line in lines:
#     print("Hello, ", line)

# with open("names.txt", "r") as file: # Abrir el archivo en modo de lectura
#     for line in file:
#         print("Hello, ", line.strip())  # Eliminar el salto de línea al imprimir

names = []

with open("names.txt") as file:  # Abrir el archivo en modo de lectura
    for line in file:
        names.append(line.rstrip())  # Eliminar el salto de línea al agregar el nombre a la lista
        
for name in sorted(names, reverse=True):  # Ordenar los nombres en orden descendente
    print(f"Hello, {name}!") 