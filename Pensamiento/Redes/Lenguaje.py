import os
#from Librerias.Propias.CrearNodos import rutas
check= False

def Control():
   ruta = "Diccionario.txt"
   if os.path.exists(ruta):
       check = True
   else:
       CrearDiccionario()
       

def Inicial():
    Control()
    while check == True:
        LeerDiccionario()
        check=False
    return None

def CrearDiccionario():
    with open("Diccionario.txt", "a")as Dicc:
        Dicc.write(("hola")+",")
        check=True

def ampliar(Palabra):
    with open("Diccionario.txt", "a+") as Dicc:
        if Palabra not in Dicc:
            Dicc.write(Palabra+",")
            
def Cargar():
    with open("Diccionario.txt", "r") as Dicc:
        contenido=Dicc.read()
        Carga= [Linea.strip().split(",") for Linea in Dicc]
        return set (Carga)  

def LeerDiccionario():
    existente = Cargar()
    palabrasRevisar= existente.split()
    for p in palabrasRevisar:
        pLimpia = p.strip(",.").lower()
        if pLimpia not in existente:
            ampliar(pLimpia)
            existente.add(pLimpia)

def ErrorExistente():
    return None

def leerSignos():
    return None