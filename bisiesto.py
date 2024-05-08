anio = int(input("Digite el año a Verificar si es Bisiesto:  "))
if anio % 4 == 0:
    if anio % 100 != 0:
        if anio % 400 == 0 :
          print(anio,"Es un Año Bisiesto")
        else:
          print(anio,"Es un Año NO Bisiesto")
    else:
       print(anio,"Es un Año NO Bisiesto")
else:
 print(anio, "Es un Año NO Bisiesto")
