""" 
	file: run2.py
	autor: PC
"""

from misvariables import *

# uso de condicional simple

nota = input("Por favor ingrese la primera nota: ")
nota2 = input("Por favor ingrese la segunda nota: ")

# Se convierte en entero las variables cadena
nota = int(nota)
nota2 = int(nota2)

# Estructuras condicional SiNo-Entonces
if nota >=18:
	# print(%s, su valor de nota es: %d % (mensaje, nota))
	print("%s: %d" % (mensaje, nota))
else: 
	print("%s: %d" % (mensaje2, nota))

if nota2 >=18:
	print("%s: %d" % (mensaje, nota2))
else: 
	print("%s: %d" % (mensaje2, nota2))
