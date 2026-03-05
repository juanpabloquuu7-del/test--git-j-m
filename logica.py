bd_empanadas = []

def obtener_todo():
    return bd_empanadas

def proceso_guardar(nombre, precio):
    
    nueva = {"item": nombre, "costo": precio}
    bd_empanadas.append(nueva)
    return True