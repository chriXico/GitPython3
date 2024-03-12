def informacion(pregunta, tipo_validacion):
    while True:
        respuesta = input(pregunta)
        if tipo_validacion(respuesta):
            return respuesta
        else:
            print("Entrada inválida. Por favor, inténtelo nuevamente.")

def validarNombre(nombre):
    return nombre.strip() != ""

def validarFecha(fecha):
    return fecha.strip() != ""

def validarDireccion(direccion):
    return direccion.strip() != ""

def validarObjetivos(objetivos):
    return objetivos.strip() != ""

def main():
    print("Por favor, ingresa tu información personal:")
    nombre = informacion("¿Cómo te llamas? ", validarNombre)
    fecha_nacimiento = informacion("¿Cuál es tu fecha de nacimiento? ", validarFecha)
    direccion = informacion("¿Cuál es tu dirección? ", validarDireccion)
    objetivos_personales = informacion("¿Cuáles son tus objetivos personales? ", validarObjetivos)

    print("\nResumen de la información:")
    print("Nombre:", nombre)
    print("Fecha de nacimiento:", fecha_nacimiento)
    print("Dirección:", direccion)
    print("Objetivos personales:", objetivos_personales)

# funcion __name__ para llamar el main
if __name__ == "__main__":
    main()
