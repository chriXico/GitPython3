import random

# Solicitar al usuario que ingrese un número
number = int(input("Di algun numero entre 1 y 50: "))

# Inicializar el contador de intentos de la máquina
intentos = 0

while True:
    # Generar un número aleatorio para la máquina
    guess = random.randrange(1, 50)
    print("La máquina dice:", guess)
    intentos += 1

    # Solicitar al usuario que indique si la máquina necesita decir un número más alto o más bajo
    respuesta = input("Necesitas decir un numero mas alto o necesitas decir un numero mas bajo? (mas alto/mas bajo): ")

    if respuesta.lower() == "mas alto" and guess < number:
        print("Correcto, la máquina necesita decir un número más alto.")
    elif respuesta.lower() == "mas bajo" and guess > number:
        print("Correcto, la máquina necesita decir un número más bajo.")
    else:
        print("Adivinaste el numero!")
        print("Lo lograste un total de ", intentos, " intentos")
        break
