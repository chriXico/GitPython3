puntuacion = int(input("Ingrese su puntuación: "))
salario = float(input("Ingrese su salario mensual: "))

if puntuacion >= 0 and puntuacion <= 3:
        rendimiento = "Inaceptable"
elif puntuacion >= 4 and puntuacion <= 6:
        rendimiento = "Aceptable"
elif puntuacion >= 7 and puntuacion <= 10:
        rendimiento = "Meritorio"

pago = salario * (puntuacion / 10)

if rendimiento != "Puntuación fuera de rango":
    print("Nivel de Rendimiento:", rendimiento)
    print("Cantidad de Dinero Recibido: $", pago)
else:
    print("Por favor, ingrese una puntuación válida (de 0 a 10).")
