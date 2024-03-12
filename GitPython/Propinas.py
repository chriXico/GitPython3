# Solicitar la factura total
cuenta = float(input("¿Cuál es la factura total de hoy, por favor? $"))

# Calcular la propina del 18%, 20% y 25%
propina18 = round(cuenta * 0.18)
propina20 = round(cuenta * 0.20)
propina25 = round(cuenta * 0.25)

# Calcular el total con propina para cada tasa
total18 = round(cuenta + propina18)
total20 = round(cuenta + propina20)
total25 = round(cuenta + propina25)

# Imprimir los resultados
print(f"La propina del 18% es de ${propina18}, lo que eleva el total a ${total18}")
print(f"La propina del 20% es de ${propina20}, lo que eleva el total a ${total20}")
print(f"La propina del 25% es de ${propina25}, lo que eleva el total a ${total25}")
