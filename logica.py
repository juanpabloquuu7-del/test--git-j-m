import json
NOMBRE_ARCHIVO = "archivo.json"

def cargar_datos():
    try:
        # Intentamos abrir el archivo
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Si el archivo no existe todavía, devolvemos una lista vacía
        return []

def guardar_datos(lista):
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4)

def editar_empanada(indice, nombre, precio):
    lista = cargar_datos()
    if 0 <= indice < len(lista):
        lista[indice] = {"nombre": nombre, "precio": precio}
        guardar_datos(lista)
        return True
    return False


def agregar_empanada(nombre, precio):
    lista = cargar_datos()
    lista.append({"nombre": nombre, "precio": precio})
    guardar_datos(lista)

def proceso_eliminar(indice):
    lista = cargar_datos()
    if 0 <= indice < len(lista):
        lista.pop(indice)
        guardar_datos(lista)
        return True
    return False