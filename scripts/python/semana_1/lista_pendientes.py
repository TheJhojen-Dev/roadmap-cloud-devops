#5. La Lista de Pendientes Dinámica

tareas = []

while True:
    nueva_tarea = input("Introduce una tarea (o escribe 'salir' para terminar): ")
    
    if nueva_tarea.lower() == "salir":
        break
        
    tareas.append(nueva_tarea)

print("\nTu lista de tareas para hoy:")
for tarea in tareas:
    print(f"- {tarea}")

		
	
