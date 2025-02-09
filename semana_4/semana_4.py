5# 1. string + string → ? # ---> Succeded
# print("Hola" + "Hola")
# 2. string + int → ? # ---> Error (TypeError: can only concatenate str (not "int") to str)
# print ("Hola" + 1)  
# 3. int + string → ? # ---> Error (TypeError: unsupported operand type(s) for +: 'int' and 'str')
# print(10 + "texto") 
# 4. list + list → ? # ---> Succeded
# lista_1 = ["perro", "gato", "tortuga"]
# lista_2 = ["bmw", "honda", "toyota"]
# print(lista_1 + lista_2)
# 5. string + list → ? # ---> Error  (TypeError: can only concatenate str (not "list") to str)
# lista_1 = ["perro", "gato", "tortuga"]
# text = "this is a text"
# print(text + lista_1)
# 6. float + int → ? # ---> Succeded
# print(1.5 + 1)
# 7. bool + bool → ?
# print(True + True) # ---> Succeded

# 8. string * int → ? # ---> Succeded
# print ("Hola" * 5)
# 9. int * string → ? # ---> Succeded
# print (5 * "Hola")
# 10. int * Boolean → ? # ---> Succeded
# print (5 * False)
# 11. int * Boolean → ? # ---> Succeded
# lista_1 = ["perro", "gato", "tortuga"]
# print(2 * lista_1)

#----------------------------------------------------------------------------

# 2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y
# muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

# nombre = input("Escribe tu nombre: ")
# apellido = input("Escribe tu apellido: ")
# nombre_completo = f"{nombre} {apellido}"
# edad = int(input("Escribe tu edad: "))
# if edad < 2:
#     print(f"Hola {nombre_completo}, de acuerdo a tu edad eres un bebé")
# elif edad < 10:
#     print(f"Hola {nombre_completo}, de acuerdo a tu edad eres un niño")
# elif edad < 18:
#     print(f"Hola {nombre_completo}, de acuerdo a tu edad eres un adolescente")
# elif edad < 25:
#     print(f"Hola {nombre_completo}, de acuerdo a tu edad eres un adulto joven")
# elif edad < 65:
#     print(f"Hola {nombre_completo}, de acuerdo a tu edad eres un adulto")
# elif edad >=65:
#     print(f"Hola {nombre_completo}, de acuerdo a tu edad eres un adulto mayor")
    
#----------------------------------------------------------------------------

# 3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#   3.1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

# import random

# while True:
#     lista_numero_secreto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     numero_secreto = random.choice(lista_numero_secreto)
#     numero_usuario = int(input("Elige entre 1 y 10: "))
#     if numero_usuario == numero_secreto:
#         print("Correcto!")
#         break
#     elif numero_usuario != numero_secreto:
#         print("Sigue intentando!")

#----------------------------------------------------------------------------

# 4. Cree un programa que le pida tres números al usuario y muestre el mayor.

# print("Escoge tres numeros, te digo cual es el mas alto: 10")
# numero_1 = int(input("primer numero: "))
# numero_2 = int(input("Segundo numero: "))
# numero_3 = int(input("Tercer numero: "))

# if numero_1 > numero_2 and numero_1 > numero_3:
# 	print(f"El primero es el mas alto: {numero_1}")
# elif numero_2 > numero_1 and numero_2 > numero_3:
# 	print(f"El segundo es el mas alto: {numero_2}")
# elif numero_3 > numero_1 and numero_3 > numero_2:
# 	print(f"El tercero es el mas alto: {numero_3}")


#----------------------------------------------------------------------------

# 5. Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70).
#     2. Cuantas notas tiene desaprobadas (menor a 70).
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.

# cantidad_de_notas_aprobadas = 0
# promedio_de_notas_aprobadas = 0 
# cantidad_de_notas_desaprobadas = 0 
# promedio_de_notas_desaprobadas = 0 
# promedio_de_notas_total = 0
# contador_de_nota = 1 

# total_de_notas = int(input("Ingrese la cantidad de notas: "))
# while contador_de_nota <= total_de_notas:
#     nota_actual = int(input(f"Ingrese la nota numero {contador_de_nota}: "))
#     if nota_actual < 70:
#         cantidad_de_notas_desaprobadas = cantidad_de_notas_desaprobadas + 1
#         promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
#         contador_de_nota = contador_de_nota + 1
#         promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
    
#     else:
#         cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
#         promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
#         contador_de_nota = contador_de_nota + 1
#         promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas
        

#     promedio_de_notas_total = promedio_de_notas_total + (nota_actual / total_de_notas)


# print(f"El estudiante tiene esta cantidad de notas aprobadas: {cantidad_de_notas_aprobadas}")
# print(f"Este es el promedio de notas aprobadas {promedio_de_notas_aprobadas}")
# print(f"El estudiante tiene esta cantidad de notas desaprobadas: {cantidad_de_notas_desaprobadas} ")
# print(f"Este es el promedio de notas desaprobadas {promedio_de_notas_desaprobadas}")
# print(f"Este es el promedio total de notas {promedio_de_notas_total}")


#----------------------------------------------------------------------------
#Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    # 1. Si el precio es menor a 100, el descuento es del 2%.
    # 2. Si el precio es mayor o igual a 100, el descuento es del 10%.

# precio_producto = input("¿Cuál es el precio del producto? :  ")
# precio_producto = int(precio_producto)
# if precio_producto < 100:
# 	descuento = precio_producto * 0.02
# 	precio_final = precio_producto - descuento
# 	print(precio_final)
# elif precio_producto >= 100:
# 	descuento = precio_producto * 0.1
# 	precio_final = precio_producto - descuento
# 	print(precio_final)

#----------------------------------------------------------------------------

#Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.

# tiempo_en_segundos = input("¿Cuál es el tiempo en segundos? ")
# tiempo_en_segundos = int(tiempo_en_segundos)
# if tiempo_en_segundos < 600:
# 	diferencia = tiempo_en_segundos - 600
# 	print(f"La diferencia es {diferencia} segundos")
# elif tiempo_en_segundos > 600:
# 	print("Es mayor!")

#----------------------------------------------------------------------------
#Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número

# numero_positivo = int(input("Pida un numero: "))
# numero = 0
# sumando = 0
# while numero < numero_positivo:
#     numero  = numero + 1
#     sumando = sumando + numero
#     print(sumando)

#----------------------------------------------------------------------------
# Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (primero y segundo) y los ordene de menor a mayor en dichas variables

# primero = int(input("Favor dar el primer numero "))
# segundo = int(input("Favor dar el segundo numero "))
# if primero > segundo:
# 	print(f"{primero}, {segundo}")
# elif segundo > primero:
# 	print(f"{segundo}, {primero}")

#----------------------------------------------------------------------------
# Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.

# velocidad_km_hora = int(input("Introduzca la velocidad que desea convertir "))
# velocidad_mts_seg = velocidad_km_hora * 1000 / 3600
# print(velocidad_mts_seg)

#----------------------------------------------------------------------------
# Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, 
# ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.

# total_hombres = 0
# total_mujeres = 0
# contador = 0 
# while contador < 6:
# 	contador = contador + 1
# 	sexo = int(input("Ingrese el sexo de una persona; marque 1 si es hombre o marque 2 si es mujer: "))
# 	if sexo == 1:
# 		sexo = 1 * 100 / 6
# 		total_hombres = total_hombres + sexo 
# 	elif sexo == 2:
# 		sexo = 1 * 100 / 6
# 		total_mujeres = total_mujeres + sexo
# print(f"hombres:{total_hombres}, mujeres {total_mujeres}")