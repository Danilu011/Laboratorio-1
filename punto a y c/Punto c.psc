Algoritmo Control_Acceso
    Definir nivel_acceso, nivel_requerido Como Entero
    Definir tarjeta Como Entero
    Definir ultimocambio Como Entero
    
    Escribir "Bienvenido, Este programa verificara su acceso a nuestros edificios."
    Escribir "Ingrese su nivel de acceso (0 a 5): "
    Leer n_acceso
    
    Escribir "Ingrese el nivel de acceso requerido para esta �rea (0 a 5): "
    Leer n_requerido
    
    Escribir "�Su tarjeta est� activa? (1 para S�, 0 para No): "
    Leer tarjeta
    
    Escribir "Ingrese cu�ntos d�as han pasado desde que cambi� su contrase�a: "
    Leer ultimocambio
    
    Si (n_acceso >= n_requerido) Y (tarjeta = 1) Y (ultimocambio <= 30) Entonces
        Escribir "Acceso concedido. Bienvenido al �rea restringida."
    Sino
        Escribir "Acceso denegado. No cumple con los requisitos de seguridad."
    FinSi
FinAlgoritmo
