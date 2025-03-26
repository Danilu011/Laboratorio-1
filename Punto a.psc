Algoritmo Retraso_Tareas
    Definir retraso, dias_asignados Como Real
    Definir p Como Real
	
    Escribir "Bienvenido, este codigo mostrara el porcentaje de retraso en sus tareas"
    Escribir "Ingrese la cantidad de días de retraso en la tarea:"
    Leer retraso
	
    Escribir "Ingrese la cantidad total de días asignados a la tarea:"
    Leer dias_asignados
	
    
    Si dias_asignados > 0 Entonces
        p <- (dias_retraso / dias_asignados) * 100
        Escribir "El porcentaje de retraso es: ", p, "%"
    Sino
        Escribir "Error!!! Los días asignados deben ser mayores a cero."
    FinSi
FinAlgoritmo
