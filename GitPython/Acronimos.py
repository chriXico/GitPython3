frase = input("Ingrese una frase: ")
acronimo = ""
for palabra in frase.split():
    acronimo += palabra[0].upper()

print("El acrónimo es:", acronimo)
