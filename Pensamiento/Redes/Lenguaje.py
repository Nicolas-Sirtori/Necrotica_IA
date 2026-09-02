import os
#from Librerias.Propias.CrearNodos import rutas
check= False

def Control():
   ruta = "Diccionario.txt"
   if os.path.exists(ruta):
       check = True
   else:
       CrearDiccionario()
       

def Inicial(valor):
    Control()
    while check == True:
        LeerDiccionario(valor)
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

def LeerDiccionario(valor):
    existente = Cargar()
    palabrasRevisar= valor.split()
    for p in palabrasRevisar:
        pLimpia = p.strip(",.").lower()
        if pLimpia not in existente:
            ampliar(pLimpia)
            existente.add(pLimpia)
    
def recuperar(valor):
    existente = Cargar()
    return existente
def ErrorExistente():
    return None

def leerSignos():
    return None