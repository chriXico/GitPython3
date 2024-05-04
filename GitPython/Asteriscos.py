# Solicitar al usuario que ingrese la altura del triángulo
altura = int(input("Ingrese la altura del triángulo: "))

# Inicializar una variable para controlar el número de asteriscos a imprimir en cada línea
asteriscos = 1

# Bucle para generar las líneas del triángulo
for i in range(altura):
    # Imprimir la línea actual
    print('*' * asteriscos)
    
    # Incrementar el número de asteriscos para la siguiente línea
    asteriscos += 1
