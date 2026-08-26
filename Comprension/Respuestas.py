from Memoria.Guardados import *
from Pensamiento.Redes.Lenguaje import *

def Inicio(dato):
    Control()
    v = dato
    HacerResp(v)


def HacerResp(dato):
    vec = Cargar()
    for lin in vec:
        if "," in lin :
            clave, valor = lin.strip().split(",",1)
            if clave.lower()== dato.lower():
                return f"respuesta: {valor}"

    LeerDiccionario(dato)


