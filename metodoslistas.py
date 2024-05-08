lenguajes = ["Python", "C", "Javascript", "Html", "Ruby", "Php", "Java"]
lengfav = str(input("Digite un Lenguaje:  "))
Ver= (lengfav in lenguajes)
if Ver == True:
    print("El Lenguaje se encuentra en la Lista")
else:
    print("El lenguaje no se encuentra en la Lista")