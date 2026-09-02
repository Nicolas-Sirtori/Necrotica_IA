from Memoria.Guardados import *
from Pensamiento.Redes.Lenguaje import *

resultado=""
def RecibirDar(valor):
    vector = Cargar()
    palabra = valor
    for p in vector:
        plimpia = p.strip(",.").lower()
        if palabra in plimpia:
            resultado = palabra
            return resultado
        else:
            resultado = "no se encontro"
            return resultado

def guardado(dato):
    Comparar(resultado, "busqueda")