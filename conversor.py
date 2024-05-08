Temperatura = float(input("Digite la Temperatura"))
escala = input("Es Fahrenheit(F) o Celsius(C)?").lower()
if escala == "f":
    celsius = (Temperatura-32)* 5/9
    print("Fahrenheit a Celsius:", celsius)
elif escala == "c":
    Fahrenheit = (Temperatura*1.8)+32
    print("Celsius a Fahrenheit:", Fahrenheit)
else:
    print("Temperatura No Valida")