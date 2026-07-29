equipos = ["Router", "Switch", "PC1", "Server"]

print(f"Equipos actuales: {equipos}")
equipo_a_retirar = input("¿Qué equipo desea retirar? ")

# Verificamos si el equipo existe antes de intentar borrarlo
if equipo_a_retirar in equipos:
    equipos.remove(equipo_a_retirar)
    print("Equipo retirado con éxito.")
    print(f"Lista actualizada: {equipos}")
else:
    print("Error: El equipo no se encuentra en el inventario.")
