from CrearNodos import *
import random
Nodos, NComb1, NBeta=[]
n=0
e=0
def implemten():
    Nodos= creardor()
    while e in range(len(Nodos)):
        Nodos[e][1]= Cargar()[e]
        Nodos[e][2]= 1

    return Nodos

def implemtenVa():
    Nodos= creardor()
    while e in range(len(Nodos)):
        Nodos[e][1]= 0
        Nodos[e][2]= 1

    return Nodos
def combinacionLetras():
    while e in 2* range(len(implemten())):
        NComb1.add(Nodos[e])
        if(Alternar()>0):
            NComb1[e][1] = Nodos[e + 1*Alternar()][1] + " " + Nodos[e][1]
            NComb1[e][0]= n+1
            Nodos[e][0] = NComb1[e][0]
            Nodos[e][1]= NComb1[e][1]
        else:
            NComb1[e][1] = Nodos[e][1] + " " + Nodos[e + 1*Alternar()][1]
            NComb1[e][0]= n+1
            Nodos[e][0] = NComb1[e][0]
            Nodos[e][1]= NComb1[e][1]
    n=n+1
    return NComb1

def CombinacionNum():
    while e in 2*range(len(implemten())):
        NComb1.add(Nodos[e])
        if(Alternar()>0):
            NComb1[e][1] = Nodos[e + 1*Alternar()][1] + Nodos[e][1]
            NComb1[e][0]= n+1
        else:
            NComb1[e][1] = Nodos[e][1] + Nodos[e + 1*Alternar()][1]
            NComb1[e][0]= n+1

def Alternar():
    v = random.randint(1, 4)
    if(v/2 == 1):
        return -1
    
    else:
        return 1

def GenerarMatriz(valor1, valor2):
    i=0
    k=0
    while i <= valor1:
        while k<=valor2:
            implemtenVa()
            Nodos[k][1]=0
            NBeta[k]=Nodos[k]
        k = k-k
    i=0
    return NBeta
        

#necesito crear una funcion que devuelva una matriz de MxN con valor 0 vacio