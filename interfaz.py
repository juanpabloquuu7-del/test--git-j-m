import logica

def imprimir_lista():
    datos = logica.cargar_datos()
    print("\n>>>> CATÁLOGO DE DOÑA PEPE <<<<")
    if not datos:
        print("Aún no hay empanadas en el comal.")
    else:
        for i, e in enumerate(datos):
            print(f"[{i+1}] {e['nombre']} --- ${e['precio']} {e['ingredientes']} {e['disponibilidad']}")

def capturar_nueva():
    print("\n-- Registro de Empanada --")
    n = input("¿Qué sabor es?: ").strip()
    p = input("¿A cuánto la va a dar?: ").strip()
    i = input("Que ingredientes lleva: ").strip()
    while True:
        d = input("Disponibles ? (Si/No)").capitalize().strip()
        if d != "Si" or "No":
            input ("Ingrese Si o No")
            return
        elif d == "Si" or "No":
            break
    logica.agregar_empanada(n,p,i,d)
    print("¡Listo! Ya se agregó.")

def capturar_edicion():
    imprimir_lista()
    idx = int(input("\nEscribe el número de la que vas a cambiar: "))
    n = input("Nombre nuevo: ")
    p = input("Precio nuevo: ")
    i = input("Que ingredientes lleva: ").strip()
    while True:
        d = input("Disponibles ? (Si/No)").capitalize().strip()
        if d != "Si" or "No":
            input ("Ingrese Si o No")
        else :
            break
    if logica.editar_empanada(idx, n, p,i,d):
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

