import random

# color = random.choice
# print(f"The color is {color}.")

# from random import choice
# choice(seq) devuelve un elemento aleatorio de la secuencia no vacía seq. La secuencia puede ser una lista, tupla, cadena u otro tipo de secuencia.
# color = choice(["red", "blue", "green"])
# print(f"The color is {color}.")  

# from random import randint
# que hace? 
# randint(a, b) devuelve un número entero aleatorio N tal que a <= N <= b. Es decir, incluye ambos extremos del rango especificado.
number = random.randint(1, 10)
print(number)

# from random import shuffle
# shuffle(x) mezcla aleatoriamente los elementos de la lista x in situ, es decir, modifica la lista original. No devuelve ningún valor. Es útil para mezclar elementos de una lista de manera aleatoria.
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)