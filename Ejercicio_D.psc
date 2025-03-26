Algoritmo Ejercicio_D
		Definir montoCompra, totalPagar Como Real
		Definir esVIP, tieneCodigo Como Caracter
		
		Escribir "Ingrese el monto de la compra:"
		Leer montoCompra
		Escribir "¿Es cliente VIP? (s/n):"
		Leer esVIP
		Escribir "¿Tiene código de descuento especial? (s/n):"
		Leer tieneCodigo
		
		totalPagar <- montoCompra
		
		Si montoCompra > 100 Entonces
			totalPagar <- totalPagar * 0.80
		FinSi
		
		Si esVIP = "s" Entonces
			totalPagar <- totalPagar * 0.90
		FinSi
		
		Si tieneCodigo = "s" Entonces
			totalPagar <- totalPagar * 0.95
		FinSi
		
		Escribir "El total a pagar después de los descuentos es: ", totalPagar
	
FinAlgoritmo
