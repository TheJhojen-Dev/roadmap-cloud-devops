#Buscador de Dispositivos

red= ["Router", "Switch", "PC", "Servidor"]

asignar = input("ingrese un nombre: ")

if asignar in red:
	red.remove(asignar)
	print (red)
else:
	red.append(asignar)
	print(red)



