print("BIENVENIDO AL JUEGO DE ADIVIDAR EL NUMERO ENTRE EL 1 Y 100")
import random
numero_secreto = random.randint(1,100)
print(numero_secreto)
numero = int(input("Cúal es el Numero en Memoria: "))
while numero != numero_secreto:
    print(" Te equivocaste")
    numero = int(input("Digita otro Numero: "))
print("Adivinaste el numero es: ", numero)