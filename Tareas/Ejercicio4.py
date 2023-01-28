import sys
argumentos=sys.argv
print(type(argumentos))

def leer_Argumento(*args):
    for arg in args:
        print(arg)

leer_Argumento(*argumentos)
