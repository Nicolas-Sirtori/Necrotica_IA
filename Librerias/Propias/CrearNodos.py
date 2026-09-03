import os
rutaLargo=0
limite = 10
palabra =""
Conjunto = {}
Lectura = []
Oracion = ""

def creardor():
    for i in range(limite):
        clave = "Nodo"+str(i)
        Conjunto[clave]=[0, "", 2]
    return Conjunto

def cargadorNodos():
    creardor()
    va = ""
    for i in range(len(Conjunto)):
        va = Conjunto["Nodo"+str(i)]
        va= [1, Cargar(), 1]
        Lectura.append(va[1])
        i=i+1
    
def Cargar():
    ruta = os.path.dirname(__file__)
    rutass = os.path.join(ruta, "..", "Pensamiento", "Redes", "Diccionario.txt")
    with open(rutass, "r") as Dicc:
        Carga= [Linea.strip().split(",") for Linea in Dicc]
        return set(tuple(Carga) for Linea in Dicc)

#esquema del nodo => "valor", "contenido", "estado 0-1-2"
#estado 0 = desaprobado, 1 aprobado, 2 vacio