from Logica import Matematicas
from Memoria.Guardados import *
#rehacer todo esto
pregunta= ""
salida= "retorno"

def lectura():
    ListaDeOperaciones=["Suma", "Resta", "Multi", "Div\n", "Sumas", "Restas", "Multis", "Divs"]
    for i in range(len(ListaDeOperaciones)):
        print(ListaDeOperaciones[i]+" ")
    
    send=input("ingrese lo que desea: ")
    return cuentas(send)

    
    
def cuentas(recepcion):
    match recepcion:
        case "Suma":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Suma(a,b)
            Comparar(Resultado, "Cuenta suma: ")
            return (Resultado)
        case "Resta":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Resta(a,b)
            Comparar(Resultado, "Cuenta resta: ")
            return (Resultado)
        case "Multi":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Multi(a,b)
            Comparar(Resultado, "Cuenta multiplicación: ")
            return (Resultado)
        case "Div":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Div(a,b)
            Comparar(Resultado, "Cuenta División: ")
            return (Resultado)
        case "Sumas":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Sumas(envio)
            Comparar(Resultado, "Cuenta sumas: ")
            return (Resultado)
        case "Restas":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Restas(envio)
            Comparar(Resultado, "Cuenta restas: ")
            return (Resultado)
        case "Multis":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Multis(envio)
            Comparar(Resultado, "Cuenta multiplicaciones: ")
            return (Resultado)
        case "Divs":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Divs(envio)
            Comparar(Resultado, "Cuenta diviciones: ")
            return (Resultado)