"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 """

# Creacion de cadenas de caracteres: pueden ser con 3 tipos de comillas: simples, dobles o triples. Las triples permiten crear 
# cadenas multilínea.
print("1. Creación de cadenas de caracteres:")
nombre = "Sergio"
apellido = 'García'
mensaje = """Hola me llamo Sergio García 
y estoy aprendiendo Python"""

# Conversion de datos a otros tipos:
print("2. Conversión de datos a otros tipos:")
edad = 29
print(edad)
print(type(edad))
texto_edad = str(edad) # Convertimos la edad a cadena de caracteres
print(texto_edad)
print(type(texto_edad))

decimal = 3.1416
print(decimal)
print(type(decimal))

decimal_texto = str(decimal) # Convertimos el decimal a cadena de caracteres
print(decimal_texto)
print(type(decimal_texto))

#Acceso a caracteres específicos:
print("3. Acceso a caracteres específicos:")

ejemplo_1 = "Persona"
print(ejemplo_1)  # Muestra la cadena completa
print(ejemplo_1[0])  # Acceso al primer carácter
print(len(ejemplo_1))  # Longitud de la cadena

print(ejemplo_1[-1])  # Acceso al último carácter
print(ejemplo_1[-2])  # Acceso al penúltimo carácter

print("4. Acceso a subcadenas (slicing):") # cadena[inicio:fin:paso], el final no se incluye, el paso es opcional y por defecto es 1.
print(ejemplo_1[:4]) #Desde el inicio hasta el índice 4 (sin incluirlo)
print(ejemplo_1[2:5])  # Acceso a una subcadena
print(ejemplo_1[-1:3:-1])  # Acceso a una subcadena en orden inverso ejemplo_1(desde el final(-1), hasta el índice 3, en reversa (-1))
print(ejemplo_1[::2])  # Acceso a caracteres en posiciones pares
print(ejemplo_1[1:])    #Hasta el final desde el índice 1

print("5. Copiar una cadena:")
ejemplo_2 = ejemplo_1[:]  # Copia la cadena
print(ejemplo_2)
ejemplo_3 = ejemplo_1[1:5]  # Copia una subcadena 
print(ejemplo_3)

print("6 Longitud de la cadena:")
print(len(ejemplo_1))  # Longitud de la cadena
print(len(ejemplo_3))  # Longitud de la subcadena copiada
ejemplo_4 = "Hola Mundo!"
print(len(ejemplo_4))  # Longitud cuenta espacios

print("7. Concatenación de cadenas:")
saludo = "Hola"
nombre = "Sergio"
mensaje = saludo + ", me llamo " + nombre + "." #La concatenación se hace con el operador + y se deben ubicar los espacios manualmente
mensaje_2 = f"{saludo}, me llamo {nombre}." #La concatenación se hace con f-strings y se ubican los espacios automáticamente
print(mensaje)
print(mensaje_2)
print("Hola",saludo,", me llamo",nombre,".") #La concatenación se puede hacer con comas pero no se puede usar +. Ademas los espacios se ubican automáticamente.

print("8. Repetición de cadenas:")
print(ejemplo_1 * 4)  # Repite la cadena 4 veces unidas y sin saltos de linea

print("9. Pertenencia:") #Verificar que algo existe dentro(in) o no(!in) dentro de una cadena de caracteres
ejemplo_5 = "Python"
print("P" in ejemplo_5)  # Verifica si 'P' está en la cadena
print("Pyth" in ejemplo_5)  # Verifica si 'Pyth' está en la cadena
print("taza" in ejemplo_5)  # Verifica si 'taza' está en la cadena
print("ton" in ejemplo_5)  # Verifica si 'ton' está en la cadena

print("taza" not in ejemplo_5)  # Verifica si 'taza' no está en la cadena
print("ton" not in ejemplo_5)  # Verifica si 'ton' no está en la cadena


"""
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""