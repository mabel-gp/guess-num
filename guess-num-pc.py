""""Guess Num PC"""

import random

def guess_num_pc(x):

    print("----------------------------")
    print("  ¡Bienvenido(a) al juego!  ")
    print("----------------------------")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.")

    low_limit = 1
    upper_limit = x

    # Valor de la respuesta del user
    response = ""

    while response != "c":

        # Generar predicción
        if low_limit != upper_limit:
            prediction = random.randint(low_limit, upper_limit)
        else:
            prediction = low_limit

        # Obtener respuesta del usuario
        response = input(f"Mi predicción es {prediction}. Si es muy alta, ingresa (A). Si es muy baja, inGresa (B). Si es correcta, ingresa(C)").lower()

        if response == "a":
            upper_limit = prediction - 1 # Para que sea más baja
        elif response == "b":
            low_limit = prediction + 1 # Para que sea más alta
    
    print(f"La computadora adivinó tu número correctamente: {prediction}") 


guess_num_pc(5)