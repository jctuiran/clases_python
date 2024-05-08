# values(): Este método devuelve una vista de los valores almacenados en el diccionario.
puntuaciones = {"Juan": 85, "María": 92, "Carlos": 78}
for puntaje in puntuaciones.values():
    print(puntaje)

# items(): Este método devuelve una vista de tuplas (llave, valor) que representan los pares llave-
# llave valor en el diccionario
puntuaciones = {"Juan": 85, "María": 92, "Carlos": 78}
for nombre, puntaje in puntuaciones.items():
    print(f"{nombre} obtuvo {puntaje} puntos.")

# get(): Este método devuelve el valor asociado con una clave dada. Si la clave no está presente en el diccionario, devuelve un valor predeterminado (por defecto None).
puntuaciones = {"Juan": 85, "María": 92, "Carlos": 78}
puntaje_maria = puntuaciones.get("María")
print("El puntaje de María es:", puntaje_maria)

#pop(): Este método elimina y devuelve el valor asociado con una clave dada. Si la clave no está presente en el diccionario, se puede especificar un valor predeterminado para devolver.
puntuaciones = {"Juan": 85, "María": 92, "Carlos": 78}
puntaje_carlos = puntuaciones.pop("Carlos")
print("El puntaje de Carlos es:", puntaje_carlos)
puntuaciones = {"Juan": 85, "María": 92, "Carlos": 78}

# clear(): Este método elimina todos los elementos del diccionario.
puntuaciones.clear()
print("El diccionario de puntuaciones después de borrar todos los elementos:", puntuaciones)
