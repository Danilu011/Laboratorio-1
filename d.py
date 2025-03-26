#Lab #1 - Ejercicio D: Calculo de una compra c descuentos
#Autor: Angie Valentina Martínez Poveda,Camila Contreras,Daniela Martínez
#Fecha y Hora: 25-03-25 /12:00 p.m.
#Programa: Ingeniería de Sistemas 
#Docente: Jesús David Garcia Caro 
# Entrada de datos
# Solicitar datos al usuario
monto_compra = float(input("Ingrese el monto de la compra: "))
es_vip = input("¿Es cliente VIP? (sí/no): ")
tiene_codigo_descuento = input("¿Tiene código de descuento? (sí/no): ")

# Convertir respuestas a valores booleanos
if es_vip == "sí":
    es_vip = True
else:
    es_vip = False

if tiene_codigo_descuento == "sí":
    tiene_codigo_descuento = True
else:
    tiene_codigo_descuento = False

# Inicializar descuento total
descuento_total = 0

# Aplicar descuentos según condiciones
if monto_compra > 100:
    descuento_total += 0.20  # Descuento del 20%

if es_vip:
    descuento_total += 0.10  # Descuento adicional del 10%

if tiene_codigo_descuento:
    descuento_total += 0.05  # Descuento adicional del 5%

# Calcular el total a pagar
total_a_pagar = monto_compra * (1 - descuento_total)

# Mostrar el resultado
print("Total a pagar después de descuentos: $", round(total_a_pagar, 2))