import string
import random

caracteres = string.ascii_letters + string.digits + string.punctuation

longitud = int(input("Ingresa la longitud de la contraseña: "))

while longitud < 8:
    print("La longitud de la contraseña debe ser de al menos 8 caracteres.")
    longitud = int(input("Ingresa la longitud de la contraseña: "))

contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

print(f"La contraseña generada es: {contraseña}")