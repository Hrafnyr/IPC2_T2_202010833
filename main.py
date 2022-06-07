
from os import system
from Lista import listaNumeros

numeros = listaNumeros()

opcion = ""

while opcion != "N":
    system("cls")
    opcion = input('Ingrese números y presione N para continuar\n')

    if opcion.isdigit():
        numeros.insertarFinal(opcion)
    elif opcion == "N":
        pass
    else:
        print('Valor no válido')

numeros.mostrarDatos()

num = input('Seleccione un número:\n')
numeros.buscar(num)