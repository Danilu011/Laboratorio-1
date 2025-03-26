
print("Bienvenido, este programa calculará el porcentaje de retraso en sus tareas.")

dias_retraso = float(input("Ingrese la cantidad de días de retraso en la tarea: "))
dias_asignados = float(input("Ingrese la cantidad total de días asignados a la tarea: "))

if dias_asignados > 0:
    porcentaje_retraso = (dias_retraso / dias_asignados) * 100
    print(f"El porcentaje de retraso es: {porcentaje_retraso:.2f}%")
else:
    print("Error!!! Los días asignados deben ser mayores a cero")
