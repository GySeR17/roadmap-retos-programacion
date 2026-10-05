"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""
"""
En muchos lenguajes se suele enseñar:

Por valor → se copia el dato.
Por referencia → se comparte la dirección de memoria.

Python utiliza el modlo llamado Pass by Object Reference.
Esto significa que las variables no contienen el valor directamente.

Las variables contienen una referencia(una especie de etiqueta o puntero) que apunta a un objeto en memoria.

x = 10
x ───► 10
"""

print("1. Los objetos mutables e inmutables")

print("Objetos inmutables: int, float, bool, str, tuple")
numero = 15
texto = "Python"

#Si se intenta modificarlos, Python crea un objeto nuevo en memoria y cambia la referencia de la variable a ese nuevo objeto.

print("Objetos mutables: list, dict, set")  # Pueden modificarse sin crear otro objeto.
lista = [1, 2, 3]
diccionario = {"nombre": "Sergio", "edad": 29}
conjunto = {1, 2, 3}
# Estos objetos pueden cambiar internamente sin cambiar la referencia de la variable que los contiene.

print("2. Asignacion por valor(comportamiento tipico de los objetos inmutables)")

a = 7
b = a  # Se copia el valor de a en b
print(f"Antes de modificar: a = {a}, b = {b}")  # En realidad ambos apuntan al mismo objeto inmutable 7.
# a ───► 10
# b ───► 10

b = 20  # Se crea un nuevo objeto en memoria y b apunta a él.
print(f"Después de modificar b: a = {a}, b = {b}")  # No se modificó el objeto 10. Simplemente b pasó a apuntar a otro objeto.
print(id(a))
print(id(b))
print("Diferentes objetos en memoria")


print("Comprobación de id() de los objetos:")
a = 10
b = a

print(id(a))
print(id(b))
print("Mismo objeto en memoria")

print("3. Asignacion por referencia(comportamiento tipico de los objetos mutables)")
lista1 = [1, 2, 3]
lista2 = lista1
"""
En memoria: 
lista1 ─┐
        ├──► [1, 2, 3]
lista2 ─┘
"""



 
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
"""