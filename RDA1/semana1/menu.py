print("Calculadora")

print("1. Sumar")
print("2. Restar") 
print("3. Multiplicar")
print("4. Dividir")
eleccion = int(input("Elige una opción correcta: "))

if eleccion == 1:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("La suma es:", num1+num2)

elif eleccion == 2:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("La resta es:", num1-num2)

elif eleccion == 3:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("La multiplicación es:", num1* num2)

elif eleccion == 4:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if num2 != 0:
        print("La división es:", num1 / num2,)
    else:
        print("Error: No se puede dividir para cero.")

else:
    print("Debes elegir una opción correcta.")
