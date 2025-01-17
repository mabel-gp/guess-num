"""Guess Number User"""

import random 


def guess_num_user(x):  # x = límite superior

    print("----------------------------")
    print("  ¡Bienvenido(a) al juego!  ")
    print("----------------------------")
    print("Debes adivinar el número generado por la computadora.")

    random_number = random.randint(1, x) # Llama a la fx randint() del module random

    prediction = 0

    # while => sin # específico de iteraciones
    while prediction != random_number:
        prediction = int(input(f"\nAdivina un número entre 1 y {x}: "))

        if prediction < random_number:
            print("El número es mayor")
        elif prediction > random_number:
            print("El número es menor")

    
    # Cuando es ciclo se detenga
    print(f"Si, el número correcto era {random_number} ¡Adivinaste!\n")


guess_num_user(5)
