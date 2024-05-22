tareas = []

while True:
    print("\n--- Listado de Tareas ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Ingresa una opción (1-4): ")

    if opcion == "1":
        tarea = input("Ingresa la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada correctamente.")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas en la lista.")
        else:
            print("Tareas actuales:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

            indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
            if indice < 0 or indice >= len(tareas):
                print("Índice inválido.")
            else:
                tarea_eliminada = tareas.pop(indice)
                print(f"Tarea '{tarea_eliminada}' eliminada correctamente.")

    elif opcion == "3":
        if not tareas:
            print("No hay tareas en la lista.")
        else:
            print("Tareas actuales:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")