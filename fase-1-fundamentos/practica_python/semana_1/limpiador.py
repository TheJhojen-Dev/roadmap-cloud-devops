# El texto sucio que llega del cliente
entrada_cliente = "  FRESA  "

# Limpiamos los espacios y pasamos todo a minúsculas
sabor_limpio = entrada_cliente.strip().lower()

# Verificamos si es igual a "fresa"
if sabor_limpio == "fresa":
    print("¡Coincidencia encontrada! Es fresa.")
else:
    print(f"El sabor detectado es: {sabor_limpio}")
