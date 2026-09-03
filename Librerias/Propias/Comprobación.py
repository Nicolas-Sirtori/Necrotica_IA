from DarValores import *
tipo = []
razon = [""]
def leerNodo():
    for i in range(Nodos):
        razon.append(Conjunto[i][1])
        i=i+1


def ComprobacionDeTipo(valor):
    match tipo:
        case "Pregunta":
            tipo=list(valor)
            if "?" in tipo & "¿" in tipo:
                return True

