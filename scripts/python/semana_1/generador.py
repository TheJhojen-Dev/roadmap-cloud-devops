#4. Generador de Usuarios (Telemática)

nombre = input("ingresa tu nombre de usuario: ")
año = int(input("ingresa tu año nacimiento: "))

edad = 2026 - año

usuario = nombre.lower() + str (edad)

print(f"Bienvenido {usuario}")
