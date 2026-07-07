#El Centinela de la Lista

invitados = []

while True:
	print ("Si desea abandonar escriba 'salir'")
	peticion = input("ingrese un valor: ")
	
	if peticion == "salir":
		print ("finalizando programa...\n")
		break
		
	else:
		invitados.append(peticion)
		print("\nValor añadido\n")
	
print(f"lista final: {invitados}")
