print ("Bienvenido, Este programa verificara su acceso a nuestros edificios.")

# Solicitar datos al usuario
nivel_acceso = int(input("Ingrese su nivel de acceso (0 a 5): "))
nivel_requerido = int(input("Ingrese el nivel de acceso requerido para esta área (0 a 5): "))
tarjeta_activa = input("¿Su tarjeta está activa? (Sí/No): ")
dias_ultimo_cambio = int(input("Ingrese cuántos días han pasado desde que cambió su contraseña: "))

# Verificación de acceso a los edificios
if (nivel_acceso >= nivel_requerido) and tarjeta_activa and (dias_ultimo_cambio <= 30):
    print("Acceso concedido. Bienvenido al área restringida.")
else:
    print("Acceso denegado. No cumple con los requisitos de seguridad.")
