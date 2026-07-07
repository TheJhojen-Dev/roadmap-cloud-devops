import subprocess

# Lista de objetivos basada en tus conceptos de Redes (Fase 2)
objetivos = ["127.0.0.1", "google.com", "192.168.1.1"]

def verificar_hosts():
    print(f"{'OBJETIVO':<20} | {'ESTADO':<10}")
    print("-" * 35)
    
    for host in objetivos:
        # Ejecutamos el comando 'ping' usando la lógica de Linux que ya conoces
        # -c 1 (un solo paquete), -W 1 (espera de 1 segundo)
        resultado = subprocess.run(
            ['ping', '-c', '1', '-W', '1', host],
            stdout=subprocess.DEVNULL, # Redirección a /dev/null para limpiar salida 
            stderr=subprocess.DEVNULL
        )
        
        # En Linux, un código de retorno 0 significa ÉXITO 
        if resultado.returncode == 0:
            estado = "✅ ACTIVO"
        else:
            estado = "❌ CAÍDO"
            
        print(f"{host:<20} | {estado:<10}")

if __name__ == "__main__":
    verificar_hosts()
