# Solicitar al usuario que ingrese su peso y altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (altura ** 2)

# Mostrar el resultado
print("\n=== Resultado ===")
print("Peso:", peso, "kg")
print("Altura:", altura, "m")
print("Índice de Masa Corporal (IMC):", imc)

# Interpretar el IMC
if imc < 18.5:
    print("Estado: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Estado: Peso normal")
elif 25 <= imc < 29.9:
    print("Estado: Sobrepeso")
else:
    print("Estado: Obesidad")
