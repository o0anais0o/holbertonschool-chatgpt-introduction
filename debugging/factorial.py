#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémentation nécessaire pour éviter la boucle infinie
    return result

if len(sys.argv) < 2:
    print("Usage: python3 script.py <nombre_entier>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Le nombre doit être positif ou nul.")
        sys.exit(1)
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
    sys.exit(1)

f = factorial(n)
print(f)