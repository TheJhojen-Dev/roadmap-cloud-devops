#3. La Alerta de Batería (Bucle While)

bateria = 10

while True:
	bateria -= 1
	print(bateria)
	
	if bateria == 0:
		print("Apagando sistema...")
		break
