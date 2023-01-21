def IndicarElMayorNumero(a,b):
    if a<b:
        print(f"El mayor es {b}")
    else:
        print(f"El mayor es {a}")


a=int(input("Digite el primer numero => "))
b=int(input("Digite el segundo numero => "))
IndicarElMayorNumero(a,b)