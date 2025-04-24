print("Calculadora")

print("1. Sumar")
print("2. Restar") 
print("3. Multiplicar")
print("4. Dividir")
eleccion = int(input("Elige una opción correcta: "))

if eleccion <=1 or eleccion >=4:
    num1=float(input("Introduce el primer numero: "))
    num2=float(input("Ingresa el segundo número"))
    if eleccion==1:
        print("La suma es : ", )
    elif eleccion==2:
        print("La resta es: ")
    elif eleccion  == 3:
        print("La multiplicacion es: ", num1*num2)
    elif eleccion == 4:
        print("La division es: ",num1/num2)
else: 
    print("Opción no válida")
