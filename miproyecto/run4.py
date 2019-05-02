""" 
	file: run3.py
	autor: PC

	Deseamos obtener el costo de una carrera universitaria.
	-El valor promedio de cada ciclo es de $ 1200.
	-El valor promedio del seguro educativo por ciclo es de 
	$ 100, si la edad del estudiante es menor o igual a 20, 
	caso contrario sera de $ 150.
	-Si el estudiante tiene una modalidad a distancia el numero 
	de ciclos es de 10 caso contrario debera seguir 8 ciclos.
	-Obtener la proyeccion del costo de la carrera de un estudiante.
"""

# ingreso por teclado de los valores de las variables
modalidad = input("Por favor ingrese su modalidad: ")
edad = input("Por favor ingrese su edad: ")

# Se convierte en entero las variables cadena
edad = int(edad)

# Estructuras condicional SiNo-Entonces 
if (modalidad == "Presencial") or (modalidad == "presencial"):
	ciclos = 8
else: 
	if (modalidad == "Distancia") or (modalidad == "distancia"):
		ciclos = 10
		

if edad <=20:
	# valor a pagar por cada ciclo
	valor_promedio = 1200
	# Se calcula el seguro segun la cantidad de ciclos de la carrera
	seguro = 100 * ciclos
	# se calcula el valor total a pagar por los ciclos de la carrera
	costocarrera_ciclos = ciclos * valor_promedio
	# Formula para encontrar el costo final a pagar por toda la carrera
	costo_final = costocarrera_ciclos + seguro
	# se imprime el mensaje dando a conocer es costo a pagar
	print("Su costo final a pagar por la carrera es: %.2f" % costo_final)
else:
	# valor a pagar por cada ciclo
	valor_promedio = 1200
	# Se calcula el seguro segun la cantidad de ciclos de la carrera
	seguro = 150 * ciclos
	# se calcula el valor total a pagar por los ciclos de la carrera
	costocarrera_ciclos = ciclos * valor_promedio
	# Formula para encontrar el costo final a pagar por toda la carrera
	costo_final = costocarrera_ciclos + seguro
	# se imprime el mensaje dando a conocer es costo a pagar
	print("Su costo final a pagar por la carrera es: %.2f" % costo_final)
		

