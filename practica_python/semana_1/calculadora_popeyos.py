#1. El Calculador de Ganancias (Popeyos)

precio_popeyo = int(input("ingrese el precio del popeyo: "))
ventas = int(input("ingrese las cantidad vendida: "))

ganancia = precio_popeyo * ventas

if ganancia >= 20:
	print("Dia productivo")
else:
	print("Dia lento")

