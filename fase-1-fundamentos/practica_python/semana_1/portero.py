#2. El Portero del Club "Linux"

edad = int(input("ingresa tu edad: "))

edad_restante = 18 - edad

if edad >= 18:
	print("Bienvenido a la terminal")
else:
	print(f"Acceso restringido: te faltan {edad_restante} años")
	
