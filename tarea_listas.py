# ===============================================
# Ejercicios Listas, Tuplas y diccionarios (Core)
# Juan Jose Gini Becker
# ===============================================

from collections import defaultdict
from expanded_ventas import ventas_expanded as ventas

# ventas = [
#     {
#         'fecha': '2024-08-03',
#         'producto': 'Mountain Bike',
#         'cantidad': 3,
#         'precio': 1500.0
#     },
#     {
#         'fecha': '2024-08-04',
#         'producto': 'Gravel Bike',
#         'cantidad': 4,
#         'precio': 1200.0
#     },
#     {
#         'fecha': '2024-08-05',
#         'producto': 'Helmets',
#         'cantidad': 30,
#         'precio': 15.50
#     },
#     {
#         'fecha': '2024-08-06',
#         'producto': 'Road Bike',
#         'cantidad': 3,
#         'precio': 2000
#     },
#     {
#         'fecha': '2024-08-07',
#         'producto': 'Mountain Bike Tires',
#         'cantidad': 10,
#         'precio': 29.90
#     },
# ]

nombre_archivo = 'informacion.txt'

# ===========================
# Calculo de Ingresos Totales
# ===========================

def ingresos_totales(lista_de_ventas):
    suma_total = 0
    for venta in lista_de_ventas:
        total_venta = venta['precio'] * venta['cantidad']
        suma_total += total_venta
    return suma_total

# print('INGRESOS TOTALES',
#       ingresos_totales(ventas), '\n', sep='\n')

with open(nombre_archivo, 'w') as file:
    file.write('INGRESOS TOTALES\n')
    file.write(f'{ingresos_totales(ventas)}\n\n')

# =================================
# Analisis del Producto mas vendido
# =================================

ventas_por_producto = defaultdict(int)

# for venta in ventas:
#     ventas_por_producto[venta['producto']] = 0

for venta in ventas:
    ventas_por_producto[venta['producto']] += venta['cantidad']
    
producto_mas_vendido = ''
cantidad_total = 0

for producto, cantidad_vendida in list(ventas_por_producto.items()):
    if cantidad_vendida > cantidad_total:
        producto_mas_vendido = producto
        cantidad_total = cantidad_vendida

# print('PRODUCTO MAS VENDIDO',
#       f'{producto_mas_vendido}: {cantidad_total}', '\n', sep='\n')

with open(nombre_archivo, 'a') as file:
    file.write('PRODUCTO MAS VENDIDO\n')
    file.write(f'{producto_mas_vendido}: {cantidad_total}\n\n')

# ===============================
# Promedio de precio por producto
# ===============================

precios_por_producto = defaultdict(tuple)

# precios_por_producto = { 'producto': ( float(suma_total), int(cantidad_vendida) ) }

for venta in ventas:
    suma_de_ventas = venta['cantidad'] * venta['precio']
    precios_por_producto[venta['producto']] += (suma_de_ventas, venta['cantidad'])

precios_por_producto = dict(precios_por_producto)

# print('PRECIOS POR PRODUCTO')
# for key, value in precios_por_producto.items():
#     precio_promedio = value[0] / value[1]
#     file.write(f'{key}: {precio_promedio}')
# print('\n')

with open(nombre_archivo, 'a') as file:
    file.write('PRECIOS POR PRODUCTO\n')
    for key, value in precios_por_producto.items():
        precio_promedio = value[0] / value[1]
        file.write(f'{key}: {precio_promedio}\n')
    file.write('\n')

# ==============
# Ventas por dia
# ==============

ingresos_por_dia = defaultdict(float)

for venta in ventas:
    ingresos_por_dia[venta['fecha']] += venta['cantidad'] * venta['precio']
    
ingresos_por_dia = dict(ingresos_por_dia)

# print('INGRESOS POR DIA')
# for key, value in ingresos_por_dia.items():
#     print(f'{key}: {value}')
# print('\n')

with open(nombre_archivo, 'a') as file:
    file.write('INGRESOS POR DIA\n')
    for key, value in ingresos_por_dia.items():
        file.write(f'{key}: {value}\n')

# =======================
# Representacion de Datos
# =======================

# Preparar el diccionario

resumen_ventas = {}

for venta in ventas:
    resumen_ventas[venta['producto']] = {
        'cantidad_total': 0,
        'ingresos_totales': 0.0,
        'precio_promedio': 0.0
    }

# Iterar y actualizar los datos

for venta in ventas:
    resumen_ventas[venta['producto']]['cantidad_total'] += venta['cantidad']
    resumen_ventas[venta['producto']]['ingresos_totales'] += venta['cantidad'] * venta['precio']
    precio_promedio_actualizado = resumen_ventas[venta['producto']]['ingresos_totales'] / resumen_ventas[venta['producto']]['cantidad_total']
    resumen_ventas[venta['producto']]['precio_promedio'] = precio_promedio_actualizado

# Imprimir informacion

# for producto, informacion in resumen_ventas.items():
#     print(producto.upper())
#     for llave, valor in informacion.items():
#         print(f'{llave}: {valor}')
#     print('\n')
    
with open(nombre_archivo, 'a') as file:
    file.write('\n')
    for producto, informacion in resumen_ventas.items():
        file.write(producto.upper())
        file.write('\n')
        for llave, valor in informacion.items():
            file.write(f'{llave}: {valor}\n')
        file.write('\n')
    