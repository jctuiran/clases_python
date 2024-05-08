import math
# Pedir el Radio de la Circunferencia
radio = float(input("Digite el Radio de la Circunferencia en mm: "))
# pi = 3.1416
#area = pi*radio*radio
area = math.pi* radio**2
# Mostrar el resultado
print("\n=== Resultado ===")
print("Radio:", radio, "mm")
print("El Radio de la Circunferencia es:", area, "mm")