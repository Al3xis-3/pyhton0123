import main.main as main
import os
try:
    a=int(input("Digite el primer valor => "))
    b=int(input("Digite el segundo valor => "))
    main.Division(a,b)
    n=int(input("Digite la cantidad de valores => "))
    main.Suma(n)
except Exception as e:
    print(e)
else:
    if __name__=='__main__':
        print("Archivo principal")
        print(os.getcwd())
finally:
    print("Proceso Terminado!!!")