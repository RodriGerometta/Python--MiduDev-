###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos de manera estructurada y permiten acceder a los valores mediante sus claves.
###

# Ejemplo tipico de un diccionario
persona = {
    "nombre": "Rodrigo",
    "edad": 30,
    "es_estudiante": True,
    "calificaciones": [8.5, 9.0, 7.5],
    "redes": {
        "facebook": "rodrigo.fb",
        "twitter": "@rodrigo_tw",
        "instagram": "@rodrigo_ig",
    },
}

# para acceder a un valor, se usa la clave entre corchetes
print(persona["nombre"])  # Imprime: Rodrigo
print(persona["calificaciones"][2])  # Imprime: 7.5
print(persona["redes"]["facebook"])  # Imprime: rodrigo.fb

# cambiar valores al acceder
persona["nombre"] = "Esteban"
persona["calificaciones"][2] = 10
print(persona["nombre"])
print(persona["calificaciones"][2])

print(persona)

# Eliminar completamente una pripiedad
del persona["edad"]
print(persona)

# eliminar con pop, ademas de eliminarlo te devuelve el resultado
es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = {"name": "Rodrigo", "age": 30}
b = {"name": "Lucila", "es_estudiante": True}

print(f"El diccionario a antes del update:\n {a}")
a.update(b)
print(f"El diccionario a despues del update\n {a}")

# Comprobar si existe una propiedad
print("name" in persona) #False
print("nombre" in persona) #True

# obtener todas las claves
print("\nKeys:")
print(persona.keys())

# obtener todos los valores
print("\nValues:")
print(persona.values())

# obtener tanto clave como valor
print("\nItems:")
print(persona.items())

print("\n")
for key, value in persona.items():
    print(f"{key}: {value}")