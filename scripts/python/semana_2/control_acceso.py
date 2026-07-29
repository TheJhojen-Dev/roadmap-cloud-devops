#Control de Acceso Lógico

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if nombre == "Admin" or edad >= 18:
	print ("acceso concedido")
else:
	print ("Acceso denegado")
