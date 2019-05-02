""" 
	file: run3.py
	autor: PC

	nota mayor o igual a 18: sobresaliente

	nota mayor o igual a 16 y menor a 18: muy buena

	nota mayor o igual a 13 y menor a 16: buena

	nota menor a 13: insuficiente
"""

from misvariables import *

# uso de condicional anidado

nota = input("Por favor ingrese la nota: ")

# Se convierte en entero las variables cadena
nota = int(nota)

# Estructuras condicional SiNo-Entonces compuesta por varias
if nota >=18:
	print("%s : nota %d" % ("Sobresaliente", nota))
else: 
	if (nota >=16) and (nota <18):
		print("%s : nota %d" % ("Muy buena", nota))
	else:
		if (nota >=13) and (nota <16):
			print("%s : nota %d" % ("Buena", nota))
		else: 
			print("%s : nota %d" % ("Insuficiente", nota))
