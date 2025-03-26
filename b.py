import math
print ("Buen día,Este programa determinara el volumen de una esfera dependiendo su radio, para saber la cantidad de material que se usara para su producción")
r= float(input("Ingrese el radio de la esfera: "))
v = (4/3)*math.pi*(r**3)
print(f"El volumen de la esfera es de:={v} cm^3" )