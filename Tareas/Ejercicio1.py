print("Bienvenido al menú interactivo")
print("\t")
while True:
    print("""Elige el número de la pregunta
    1) Realizar un programa que dibuje un cuadrado en una consola con *, usando bucles
    2) Realizar una iteracion de una lista de números e identificar si es múltiplo de 2 e imprimir el número
    3) Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad
    4) Salir""")
    print("\t")
    opcion=input()
    if opcion == '1':
        print("\tRealizar un programa que dibuje un cuadrado en una consola con *, usando bucles")
        lado=int(input("Ingrese el valor del lado => "))
        for i in range(lado):
            for i in range(lado):
                print("*", end="")
            print(" ")
    elif opcion == '2':
        print("\tRealizar una iteracion de una lista de números e identificar si es múltiplo de 2 e imprimir el número")
        cantidad = int(input('Cuantos números va a introducir ? '))
        lista_numeros = list()
        for item in range(1, cantidad+1):
            x = int(input(f'Ingrese el {item} número: ')) 
            lista_numeros.append(x)   
        print(lista_numeros)
        for x in lista_numeros:
            if x%2==0:
                print("Los numeros multiplos de 2 de la lista son: ")
                print(x)
    elif opcion =='3':
        print("\tIterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad")
        total = int(input('Cuantos elementos va a introducir ? '))
        lista_nombres = list()
        for i in range(1, total+1):
            x = input('Ingrese el nombre => ')
            lista_nombres.append(x)  
        lista_edades=list()
        for i in range(1, total+1):
            y = int(input('Ingrese su edad => '))
            lista_edades.append(y)
        Lista_Elementos=list([lista_nombres,lista_edades])
        print(Lista_Elementos)
        menor=y
        for a in lista_edades:
            if a < menor:
                menor=a
        print(f"La menor edad es {menor}")
    elif opcion =='4':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")





