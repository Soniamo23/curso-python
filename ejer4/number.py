import random

numero_secreto = random.randint(1, 100)

intentos = 0
adivina = None

while adivina != numero_secreto:
    adivina = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    
    if adivina < numero_secreto:
        print("Demasiado bajo")
    elif adivina > numero_secreto:
        print("Demasiado alto")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")