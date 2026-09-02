from DarValores import *
tipo = ""
razon = [""]
def leerNodo():
    for i in range(Nodos):
        razon.append(Conjunto[i][1])
        i=i+1


def ComprobacionDeTipo():
    match tipo:
        case "Pregunta":
            return None
        