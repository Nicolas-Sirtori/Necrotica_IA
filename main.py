#region Materiales
from Comprension import Menues
import os
#endregion 

#region variables
L=" "
respuesta=""
salida="exit"
#endregion

#region funciones
#endregion

#region funcion base
def main():
    L=input("¿desea iniciar?: ")
    while L != salida:
        os.system("cls")
        Valorfinal=Menues.bucle()
        respuesta="el resultado es: "+ str(Valorfinal)
        print(respuesta)
        print("exit para cerrar el programa")
        L=input("ingrese una nueva instrucción: ")
#endregion

#region clave
main()
#endregion