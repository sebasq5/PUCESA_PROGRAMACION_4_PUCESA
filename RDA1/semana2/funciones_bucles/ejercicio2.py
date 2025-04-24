n1=int(input("Ingrese el primer numero menor: "))
n2=int(input("Ingrese el segundo numero mayor: "))
while n2>=n1:
    if n2%2==0:
        print(n2,"es par")
    else:
        print(n2,"es impar")

    n2=n2-1