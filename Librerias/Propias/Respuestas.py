import DarValores

Z=[]
i=0
def Elaborador():
    Z = DarValores.combinacionLetras()
    for i in range(len(Z)):
        print(Z[i][1])

Elaborador()