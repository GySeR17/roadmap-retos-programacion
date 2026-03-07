"""
Funciones integradas (Built-in Functions)
"""

#Algunas de las mas usadas pueden ser:
print("Hola")   #Muestra informacion en pantalla
len("Python")   #Retorna la longitud de un objeto
type(5)         #Muestra el tipo de dato
type("Hello!")
int("10")       #Convierte a entero
float("2.3")    #Convierte a decimal
str(1234)       #Convierte a texto  
#input("Introduzca su nombre:\n")    #Recibe datos del usuario
sum(range(5), 2)                    #Suma elementos
max(1, 2, 5, 9, 4, 8, 3, 6, 36)     #Retorna el maximo
max(-6, 2, 5, 9, 4, 8, 3, 6, 36)    #Retorna el minimo
range(2, 15)                        #Genera secuencias de numeros

"""
Funciones definidas por el usuario
"""
# simple

def saludo():
    print("Hola, Python!")

saludo()

#Con recepcion de parametros:
print("\nCon 1 parametro")

def cuadrado(num):
    print(num ** 2)

cuadrado(3)


print("\nCon varios parametros")

def sumar(a, b, c):
    return a + b + c

total = sumar(2, 5, 9)
print(total)

def mult(a, b, c):
    return a * b * c

total_2 = mult(2, 5, 9)
print(total_2)

"""
Funciones dentro de funciones (HOF - Funciones de Orden Superior)
"""