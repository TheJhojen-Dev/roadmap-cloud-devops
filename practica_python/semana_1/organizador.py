#1. El Organizador de "Cappuccino Studio"

proyectos = ["Logo", "Sprites", "Mapa"]

nuevo_proyecto = input ("ingresa un nuevo proyecto: ")

if nuevo_proyecto:
    proyectos.insert(0, nuevo_proyecto)

# Imprimimos el total de proyectos
print(f"Actualmente tienes un total de {len(proyectos)} proyectos en la lista.")
