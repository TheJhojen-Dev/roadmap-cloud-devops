#4. Tabla de Multiplicar (Bucle For)

numero = int(input("ingresa un numero (del 1 al 10): "))

for i in range(1, 10):
	resultado = numero * i
	print(f"{numero} x {i} = {resultado}")
	
