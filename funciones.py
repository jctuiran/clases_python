""" 
PROGRAMA PARA EXPLICAR EL CONCEPTO DE MODULOS
SE DEFINEN VARIAS FUNCIONES SUMA, RESTA, MAYOR, MULTIPLICACIÓN
DIVISIÓN Y RESIDUO, LAS CUALES SERÁN LLAMADAS DESDE EL ARCHIVO
LLAMARMODULO.PY
"""
# Función Suma 
def Sumar(a,b):
    suma = a+b
    return suma

# Función Resta
def Restar(a,b):
    resta = a-b
    return resta

# Función Multiplicar
def Multiplicar(a,b):
    multi=a*b
    return multi

# Función Division
def Dividir(a,b):
    divi = a/b
    return divi

# Función Residuo
def Residuo(a,b):
    modulo = a%b
    return modulo

# Función MAYOR
def Mayor(a,b):
    if a > b :
       return a
    elif b > a:
       return b    
    else:
        return "Son iguales"
    return()

def pedir_datos():
    print("Programa que hace esto con 2 Numero")
    print("Suma,Resta,Multiplica,Divide,Módulo y Compara")
    x = int(input("Ingrese el Primer Número:"))
    y = int(input("Ingrese el Segundo Número:"))

    suma=Sumar(x,y)
    resta=Restar(x,y)
    multi=Multiplicar(x,y)
    divi=Dividir(x,y)
    residuo=Residuo(x,y)
    mayor=Mayor(x,y) 
