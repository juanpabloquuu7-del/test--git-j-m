NOMBRE_ARCHIVO = "empanadas.json"

def cargar_datos():
    try:
        # Intentamos abrir el archivo
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Si el archivo no existe todavía, devolvemos una lista vacía
        return []

def proceso_guardar(nombre, precio):
    
    nueva = {"item": nombre, "costo": precio}
    bd_empanadas.append(nueva)
    return True

def proceso_editar(indice, nombre, precio):
   
    if 0 <= indice < len(bd_empanadas):
        bd_empanadas[indice]["item"] = nombre
        bd_empanadas[indice]["costo"] = precio
        return True
    return False

def proceso_eliminar(indice):
    if 0 <= indice < len(bd_empanadas):
        bd_empanadas.pop(indice)
        return True
    return False