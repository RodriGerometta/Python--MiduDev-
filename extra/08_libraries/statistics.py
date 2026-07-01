import statistics
# el modulo statistics proporciona funciones para calcular estadísticas básicas como media, mediana, moda, etc.
# mean(data) devuelve la media aritmética de los datos. La media se calcula sumando todos los valores y dividiendo por el número de valores.
print("Media aritmetica: ", statistics.mean([1, 2, 3, 4, 5]))  # Output: 3

# median(data) devuelve la mediana de los datos. La mediana es el valor central de una lista ordenada de números.
print("Mediana: ", statistics.median([1, 2, 3, 4, 5]))  # Output: 3

# mode(data) devuelve la moda de los datos. La moda es el valor que aparece con más frecuencia en un conjunto de datos.
print("Moda: ", statistics.mode([1, 2, 2, 3, 4, 4, 4]))  # Output: 4