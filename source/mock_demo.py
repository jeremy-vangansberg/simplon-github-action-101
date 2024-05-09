import random

def f1():
    return random.randint(1, 100)  # Retourne un nombre aléatoire entre 1 et 100

def f2():
    result = f1()
    return result * 10
