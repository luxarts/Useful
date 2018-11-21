#!/usr/bin/env python3

# Importa el modulo del sistema operativo
import os
os.system("clear") # Limpia la terminal

# Importa los modulos para los argumentos
import argparse
import sys

# Instancia el modulo
parser = argparse.ArgumentParser(description="Descripcion del script")

# Define los argumentos
parser.add_argument("-a1", "--arg1", default=None, action="store", help="Guarda el valor del argumento (accion por defecto)")
parser.add_argument("-a2", "--arg2", default=None, action="store_true", help="Guarda True cuando esta presente")
parser.add_argument("-a3", "--arg3", default=None, action="store_false", help="Guarda False cuando esta presente")
parser.add_argument("-a4", "--arg4", default=None, action="store_const", const=123, help="Guarda la constante cuando esta presente")

# Guarda los argumentos
args = parser.parse_args();

# Programa
dict = vars(args) # Convierte el objeto en un diccionario

if(len(sys.argv) > 1): # Si hay argumentos
	for i in dict: # Por cada argumento en el diccionario 
		if(dict[i] != None): # Si el argumento es distinto de None
			print("i: ", i, "\tvalor: ", dict[i]) # Muestra el argumento
