import csv
import os
os.system("cls")  # Limpiar la consola (en Windows)

# students = []

# with open("students2.csv") as file:  # Abrir el archivo en modo de lectura
#     reader = csv.DictReader(file)  # Crear un lector de CSV
#     for name, home in reader:  # Iterar sobre cada fila del archivo
#         students.append({"name": name, "home": home})  # Agregar un diccionario con el nombre y el hogar a la lista de estudiantes
        
# # Ordenar los estudiantes por nombre utilizando una función lambda (funcion anónima)
# for student in sorted(students, key=lambda student: student["name"]):  
#     print(f"{student['name']} is from {student['home']}.")

name = input("What is your name? ")
home = input("Where are you from? ")

with open("students2.csv", "a") as file:  # Abrir el archivo en modo de escritura (append)
    writer = csv.DictWriter(file, fieldnames=["name", "home"])  # Crear un escritor de CSV con los nombres de los campos
    writer.writerow({"name": name, "home": home})  # Escribir una nueva fila con el nombre y el hogar del estudiante
    