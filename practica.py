# EJERCICIO 1
# Desarrollar algoritmo que permita mostrar en pantalla de manera
# automática (sin digitar) una secuencia de números que se incrementan
# de 1 en 1. Debe mostrar del 1 al 10.

# for i in range(1, 11, 1):
#     print(i)

# contador = 1
# while contador <= 10:
#     print(contador)
#     contador += 1


# EJERCICIO 2
# Desarrollar algoritmo que a partir de un número digitado por el usuario
# , permita mostrar en pantalla la secuencia de números hasta llegar al valor
# 1. Ejemplo: Si digita el número 5, deberá mostrar en pantalla
# "5, 4, 3, 2, 1" (un número debajo de otro). Valide que sólo se puedan
# ingresar números positivos.


# while True:
#     contador = (input("Digite el numero: "))
#     try:
#         num = int(contador)
#         if num <= 0:
#             print("Digite un numero positivo mayor o igual a 1")
#             continue
#         else:
#             break
#     except ValueError:
#         print("Digita un numero, no letras ni simbolos")
#         continue

# for i in range(num, 0, -1):
#     print(i)


# EJERCICIO 3
# Desarrollar algoritmo que permita pedir por pantalla 5 números
# y muestre la suma de ellos. Valide que los números sean positivos,
# es decir, mayores a cero.

# suma = 0
# for i in range(1, 6):
#     while True:
#         entrada = input(f"Digite el {i}° num: ")
#         try:
#             num = int(entrada)
#             if num <= 0:
#                 print("Digite un numero mayor o igual a 1 para la suma")
#                 continue
#             else:
#                 break
#         except ValueError:
#             print("Digite una numero, no una letra o simbolo")
#             continue
#     suma += num
# print(f"La suma de sus numeros es: {suma}")


# EJERCICIO 4
# Desarrollar algoritmo que permita calcular el promedio de 5 notas
# introducidas por el teclado. Valide que dichos números estén entre 1 y 7,
# presentando un mensaje de error en caso contrario

# suma = 0
# promedio = 0
# for i in range(1, 6):
#     while True:
#         entrada = input(f"Digite la {i}° nota: ")
#         try:
#             num = int(entrada)
#             if num < 1 or num > 7:
#                 print("Error: Digite un numero entre 1 y 7 ")
#                 continue
#             else:
#                 break
#         except ValueError:
#             print("Digite un numero, no letras ni simbolos")
#             continue
#     suma += num
#     promedio = suma/5

# print(f"Su promedio es: {promedio} ")


# EJERCICIO 5
# Desarrollar algoritmo que permita mostrar en pantalla de manera automática,
# valores que se sumen de 5 en 5, hasta llegar al valor 50.
# Ejemplo: 5, 10, 15, 20, 25, 30, …, 50 (un número debajo de otro).

# for i in range(5, 51, 5):
#     print(i)

# contador = 5
# while contador <= 50:
#     print(contador)
#     contador += 5


# Desarrollar algoritmo que permita pedir por pantalla el ingreso de N notas de un
# alumno. Valide que las notas estén entre 1 y 7. Imprima la siguiente .estadística:
# •	Promedio General De Notas.
# •	Promedio De Notas Azules.
# 	Promedio De Notas Rojas.

sumatotal = 0
noA = 0
sumA = 0
promA = 0
promgen = 0
noR = 0
sumR = 0
promR = 0

while True:
    entrada = input("Digite la cantidad de notas que va a proporcionar: ")
    try:
        Nnota = int(entrada)
        if Nnota <= 0:
            print("Debe digitar 1 o mas notas ")
            continue
        else:
            break
    except ValueError:
        print("Digite un numero, no letras ni simbolos")

for i in range(1, Nnota+1):
    while True:
        notas = input(f"Digite su {i}° nota: ")
        try:
            notasfloat = float(notas)
            if notasfloat <= 1.0 or notasfloat > 7.0:
                print("Digite una nota entre 1.0 y 7.0")
                continue
            else:
                break
        except ValueError:
            print("Digite un numero, no una letra ni simbolo")

    sumatotal += notasfloat

    if notasfloat <= 4.0:
        noA = noA + 1
        sumA = sumA + notasfloat
        promA = sumA / noA
    else:
        noR = noR + 1
        sumR = sumR + notasfloat
        promR = sumR / noR

promgen = sumatotal / Nnota

print(f"\nPromedio gral de notas : {round(promgen, 1)}")
print(f"Promedio de notas azules : {round(promA, 1)}")
print(f"Promedio de notas rojas  : {round(promR, 1)}")
