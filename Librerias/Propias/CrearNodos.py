import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pensamiento.Redes.Lenguaje import *
rutaLargo=0
limite = 10
palabra =""
Conjunto = {}
Lectura = []
Oracion = ""

def creardor():
    while limite !=0:
        clave = "Nodo"+str(limite)
        Conjunto[clave]=[0, "", 2]
        limite = limite-1
    return Conjunto

def cargadorNodos():
    creardor()
    va = ""
    for i in range(len(Conjunto)):
        va = Conjunto["Nodo"+str(i)]
        va= [1, Cargar(), 1]
        Lectura.append(va[1])
        i=i+1
    


#esquema del nodo => "valor", "contenido", "estado 0-1-2"
#estado 0 = desaprobado, 1 aprobado, 2 vacio