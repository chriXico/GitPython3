def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def main():
    
    oracion = input("¿Qué tienes en mente hoy? ")

    # El contador
    palabras_oracion = contar_palabras(oracion)
    print("¡Qué bien, acabas de decirme lo que tienes en mente en", palabras_oracion, "palabras!")

    # Para abrir el archivo
    nombre_archivo = input("Por favor, ingresa el nombre del archivo para contar palabras: ")
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras_archivo = contar_palabras(contenido)
            print(f"El archivo '{nombre_archivo}' contiene {palabras_archivo} palabras.")
    except FileNotFoundError:
        print("El archivo no pudo ser encontrado.")

if __name__ == "__main__":
    main()
