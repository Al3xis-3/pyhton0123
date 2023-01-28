class Catalogo:
    autopartes=[]
    def __init__(self,autopartes=[]):
        self.autopartes=autopartes
    def agregar(self,a):
        self.autopartes.append(a)
    def mostrar(self):
        for a in self.autopartes:
            print(a)
a=input("Escriba la autoparte => ")
c=Catalogo([a])
c.mostrar()