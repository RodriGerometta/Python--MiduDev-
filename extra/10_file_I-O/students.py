import os
os.system("cls")  # Limpiar la consola (en Windows)

# with open("students.csv") as file:  # Abrir el archivo en modo de lectura
#     for line in file:
#         name, house = line.rstrip().split(",")  # Eliminar el salto de línea y separar el nombre y la casa
#         print (f"{name} is in {house}.")

students = []

with open("students.csv") as file:  # Abrir el archivo en modo de lectura
    for line in file:
        name, house = line.rstrip().split(",")  # Eliminar el salto de línea y separar el nombre y la casa
        student = {"name": name, "house": house}  # Crear un diccionario para cada estudiante
        
        students.append(student)
        
def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

# # Ordenar los estudiantes por nombre utilizando una función lambda (funcion anónima)
# for student in sorted(students, key=lambda student: student["name"]):  
#     print(f"{student['name']} is in {student['house']}.")
        
for student in sorted(students, key=get_name):  # Ordenar los estudiantes por nombre utilizando la función get_name
    print(f"{student['name']} is in {student['house']}.")