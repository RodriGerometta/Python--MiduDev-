"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

import os
os.system("cls")


nums = [4, 5, 6, 2]
goal = 8

# Forma de hacer para principiantes, con dos bucles anidados (O(n^2))
# def find_first_sum(nums, goal):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == goal:
#                 return [i, j]
#     return None

# Forma optimizada, con un diccionario para guardar los números vistos (O(n)) "Forma mas profesional"    
def find_first_sum(nums, goal):
  seen = {} # diccionario para guardar el numero y su índice

  for index, value in enumerate(nums):
    missing = goal - value
    if missing in seen:
      return [seen[missing], index]
    seen[value] = index # guardar el número actual a los vistos, porque no hemos encontrado la combinación

  return None

result = find_first_sum(nums, goal)
print(result)