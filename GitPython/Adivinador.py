import random

number = random.randrange (1,50)
guess = int(input("Di algun numero entre 1 y 50: "))

intentos = 0

while guess != number:
    intentos += 1

    if guess < number:
        print ("Necesitas decir un numero mas alto. Intentalo de nuevo")
        guess = int(input("Di algun numero entre 1 y 50: "))
    else: 
        print ("Necesitas decir un numero mas bajo. Intentalo de nuevo")
        guess = int(input("Di algun numero entre 1 y 50: "))

print("Adivinaste el numero!")
print("Lo lograste un total de ", intentos, " intentos")