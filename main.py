import interfaz

def menu_principal():
    while True:
        print("\n--- SISTEMA EMPANADAS DOÑA PEPE ---")
        print("1. Ver Menú")
        print("2. Agregar")
        print("3. Editar")
        print("4. Eliminar")
        print("5. Salir")

        op = input("Seleccione: ")

        if op == "1":interfaz.imprimir_lista()

        elif op == "2": interfaz.capturar_nueva()

        elif op == "3": interfaz.capturar_edicion()

        elif op == "4": interfaz.capturar_eliminacion()
        
        elif op == "5": 
            print("Cerrando caja... ¡Adiós!")
            break


menu_principal()
