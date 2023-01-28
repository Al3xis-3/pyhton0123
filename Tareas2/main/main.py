def namefile():
    if __name__=='__main__':
        print("Archivo principal")
    else:
        print("Dependencia")

def Division(a,b):
    print(a/b)

def Suma(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)