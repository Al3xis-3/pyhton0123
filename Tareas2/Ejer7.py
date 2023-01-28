class Producto:
    def __init__(self, pais,lote,año): 
        self.pais=pais
        self.lote=lote
        self.año=año
    
    def __str__(self):
        return '{}({})'.format(self.pais, self.lote)

class Catalogo:
    Prod=[]
    def __init__(self, Prod=[]):
        self.Prod=Prod
    def agregar(self,p):
        self.Prod.append(p)
    def mostrar(self):
        for p in self.Prod:
            print(p)
p=Producto('Peru','0001','2023')
c=Catalogo([p])
c.mostrar()