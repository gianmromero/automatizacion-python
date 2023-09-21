import pyinputplus as pyip
import time
#   Bienvenida
print("¿Cómo quieres tu sanguche? ")
time.sleep(1) # Se detiene por 1 segundo la ejecución del script.
#   Selecciones
selecciones = []
#   Pan
print("¿Qué clase de pan quisieras? ")
pan = pyip.inputMenu(['integral', 'blanco', 'frances'])
selecciones.append(pan)
#   Proteina
print("¿Qué clase de proteína deseas? ")
proteina = pyip.inputMenu(['pollo', 'pavo', 'jamon', 'tofu'])
selecciones.append(proteina)
#   ¿Con o sin queso?
print("¿Deseas agregar queso a tu order? Escribe Si/No")
res = pyip.inputYesNo(yesVal='si', noVal='no')
if res == 'si':
    print("¿Qué queso deseas? ")
    queso = pyip.inputMenu(['cheddar', 'suizo', 'mozzarella'])
    selecciones.append(queso)
else:
    queso = None
#   Adicionales
adicional = pyip.inputMenu(['mayonesa', 'mostaza', 'lechuga', 'tomate'])
selecciones.append(adicional)
#   Cantidad
cantidad = pyip.inputInt('¿Cuántos quisieras? ', min=1)
#   Diccionario de productos con sus precios.
productos = {
    'integral': 1.5,
    'blanco': 1.0,
    'frances': 0.9,
    'pollo': 3.5,
    'pavo': 4.0,
    'jamon': 4.0,
    'tofu': 4.2,
    'cheddar': 1.2,
    'suizo': 1.75,
    'mozzarella': 1.9,
    'mayonesa': 0.5,
    'mostaza': 0.5,
    'lechuga': 0.5,
    'tomate': 0.5
}

#   Función para obtener el subtotal
def sub_total_precio(selecciones):
    costo = 0
    for seleccion in selecciones:
        for k, v in productos.items():
            if k == seleccion:
                costo += v
        
    return costo
#   Subtotal
subtotal = sub_total_precio(selecciones)

#   Función para multiplicar el subtotal con la cantidad
def total_precio(subtotal, cantidad):
    res = subtotal * cantidad
    return res

#  Total
print(total_precio(subtotal, cantidad))