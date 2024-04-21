monto = float(input("Cantidad a invertir?: "))
interes = float(input("Interes porcentual anual?: "))
años = int(input("Años?: "))

for i in range(1, años + 1):
    capital = monto * (1 + interes / 100) ** i
    print(f"Capital tras " + str(i) + " años: {:.2f}".format(capital))
