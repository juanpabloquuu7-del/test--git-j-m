import logica

def imprimir_lista():
    datos = logica.cargar_datos()
    print("\n>>>> CATÁLOGO DE DOÑA PEPE <<<<")
    if not datos:
        print("Aún no hay empanadas en el comal.")
    else:
        for i, e in enumerate(datos):
            print(f"[{i}] {e['item']} --- ${e['costo']}")

def capturar_nueva():
    print("\n-- Registro de Empanada --")
    n = input("¿Qué sabor es?: ")
    p = input("¿A cuánto la va a dar?: ")
    logica.guardar_datos(n, p)
    print("¡Listo! Ya se agregó.")

def capturar_edicion():
    imprimir_lista()
    idx = int(input("\nEscribe el número de la que vas a cambiar: "))
    n = input("Nombre nuevo: ")
    p = input("Precio nuevo: ")
    if logica.proceso_editar(idx, n, p):
        print("¡Cambio guardado!")
    else:
        print("Ese número no existe.")

def capturar_eliminacion():
    imprimir_lista()
    idx = int(input("\n¿Cuál quieres quitar? (Número): "))
    if logica.proceso_eliminar(idx):
        print("¡Empanada borrada del sistema!")
    else:
        print("Error: No se encontró esa empanada.")

