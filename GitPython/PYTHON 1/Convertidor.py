"""Esta linea de codigo es una peticion que la maquina le hace al usuario para ingresar la cantidad a convertir en monedas"""

cantidad = int(input("Cantidad a convertir: "))

"""Aqui se define la funcion para la conversion, seguida de las calculadoras de moneda correspondiente 
(ven cuantas monedas del tipo caben) y la parte de cantidad que actualiza el conteo despues de dejar de usar cierta moneda"""

def convertir_Monedas(cantidad):
    monedas20 = cantidad // 20
    cantidad %= 20

    monedas10 = cantidad // 10
    cantidad %= 10

    monedas5 = cantidad // 5
    cantidad %= 5

#Esta linea asigna el resto de numro a 1 despues de que 20 10 y 5 dejen de contar
    monedas1 = cantidad
#Esta linea devuelve la cantidad de monedas de cada denominación
    return monedas20, monedas10, monedas5, monedas1

"""Se llama la funcion de convertidor con la cantidad ingresada por el usuario
y comienza a asignar los resultados a cada variable"""
monedas20, monedas10, monedas5, monedas1 = convertir_Monedas(cantidad)

"""Se imprimen los resultados"""
print("Monedas de $20: ", monedas20)
print("Monedas de $10: ", monedas10)
print("Monedas de $5: ", monedas5)
print("Monedas de $1: ", monedas1)