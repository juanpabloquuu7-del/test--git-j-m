import logica

def imprimir_lista():
    datos = logica.obtener_todo()
    print("\n>>>> CATÁLOGO DE DOÑA PEPE <<<<")
    if not datos:
        print("Aún no hay empanadas en el comal.")
    else:
        for i, e in enumerate(datos):
            print(f"[{i}] {e['item']} --- ${e['costo']}")
