#5. El Conversor de Temperaturas


while True:
	celsius = float(input("ingrese una temperatura en grado celsius: "))
	respuesta = input("¿Quieres convertir a (F)ahrenheit o (K)elvin?: ")
	respuesta.upper()
	
	if respuesta.upper() == "f": 
		F = (celsius * 9/5) + 32
		print (f"El resultado a grados fahrenheit es: {F}")
	elif respuesta == "k":
		K = celsius + 273.15
		print (f"El resultado a grador kelvin es: {K}")
			
	else:
		print("No se encontro el resultado esperado")
		
	cerrar = input("¿desea cerrar la app?(y/n): ")
	
	if cerrar == "y":
		print("¡Gracias por usar nuestro convertidor!")
		break
			
