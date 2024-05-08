"""
PROGRAMA QUE LLAMA A LAS FUNCIONES QUE ESTÁN EN EL ARCHIVO 
FUNCIONES.PY
"""
import funciones as fu

print("Programa que hace esto con 2 Numero")
print("Suma,Resta,Multiplica,Divide,Módulo y Compara")
x = int(input("Ingrese el Primer Número:"))
y = int(input("Ingrese el Segundo Número:"))

suma=fu.Sumar(x,y)
resta=fu.Restar(x,y)
multi=fu.Multiplicar(x,y)
divi=fu.Dividir(x,y)
residuo=fu.Residuo(x,y)
mayor=fu.Mayor(x,y)


print("La Suma de",x,"mas",y,"es:",suma)
print("La Resta de",x,"menos",y,"es:",resta)
print("La Multiplicación de",x,"por",y,"es:",multi)
print("La División de",x,"entre",y,"es:",divi)
print("El Residuo de",x,"entre",y,"es:",residuo)
print("El mayor entre", x, "y",y, "es:",mayor)

# fu.pedir_datos() Se puede utilizar para Pedir los Datos