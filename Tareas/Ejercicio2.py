Biblioteca={
    'categoria':['novela','poesias','infantiles','cuentos'],
    'autores':['Clorinda Matto de Turner','Ciro Alegria','José María Arguedas','Mario Vargas Llosa','Cesar Vallejo','Blanca Valera','Enrique Verástegui','Gonzalo Moure','Carlo Collodi','Charles Perrault','Julio Ramon y Ribeyro','Abraham Vladelomar','Ricardo Palma'],
    'obras':['Aves sin nido','Herencias','Novelas Peruanas','El mundo es ancho y ajeno','Los perros hambrientos','La serpiente de oro','Los ríos profundos','El Sexto','Todas las sangres','La ciudad y los perros','Conversación en la Catedral','La guerra del fin del mundo','Trilce','Los Heraldos negros','De España aparta de mí este cáliz','A media voz','Así debe ser','Canto villano','En los Extramuros del Mundo','Terceto de Lima','El Motor del Deseo','Palabras de caramelo','Pinocho','Caperucita Roja','La palabra del mudo','Vida y obra','Tradiciones Peruanas'],               
    'usuarios':[7743,7744,7745,7746,7747,7748,7749],
}
Biblioteca2={
     'categoria':{
        'novela':{
                'autores':{
                    ' Clorinda Matto de Turner':{
                        'obras':['Aves sin nido','Herencias','Novelas Peruanas'],
                    },
                    'Ciro Alegria':{
                        'obras':['El mundo es ancho y ajeno','Los perros hambrientos','La serpiente de oro'],
                    },
                    'José María Arguedas':{
                        'obras':['Los ríos profundos','El Sexto','Todas las sangres'],
                    },
                    'Mario Vargas Llosa':{
                        'obras':['La ciudad y los perros','Conversación en la Catedral','La guerra del fin del mundo'],
                    },
                },
            },
        'poesias':{
                'autores':{
                    'Cesar Vallejo':{
                        'obras':['Trilce','Los Heraldos negros','De España aparta de mí este cáliz'],
                    },
                    'Blanca Valera':{
                        'obras':['A media voz','Así debe ser','Canto villano'],
                    },
                    'Enrique Verástegui':{
                        'obras':['En los Extramuros del Mundo','Terceto de Lima','El Motor del Deseo'],
                    },
                },
            },
        'infantiles':{
                'autores':{
                    'Gonzalo Moure':{
                        'obras':['Palabras de caramelo'],
                    },
                    'Carlo Collodi':{
                        'obras':['Pinocho'],
                    },
                    'Charles Perrault':{
                        'obras':['Caperucita Roja'],
                    },
                },
            },
        'cuentos':{
                'autores':{
                    'Julio Ramon y Ribeyro':{
                        'obras':['La palabra del mudo'],
                    },
                    'Abraham Vladelomar':{
                        'obras':['Vida y obra'],
                    },
                    'Ricardo Palma':{
                        'obras':['Tradiciones Peruanas'],
                    },
                },
            },
        },
    'usuarios':[7743,7744,7745,7746,7747,7748,7749],
}
print("ESTOS SON LOS USUARIOS: ")
print(Biblioteca2['usuarios'])
print("\t")
print("\t")
print("ESTAS SON LAS CATEGORIAS: ")
print(Biblioteca2['categoria'].keys())
print("\t")
print("\t")
print("ESTOS SON LOS AUTORES Y SUS OBRAS:")
print(Biblioteca2['categoria'].values())
print("\t")
print("\t")
resp=input("Buenas, ¿Desearia pedir prestado un libro? => ")
while resp=='si':
    ObrasTotales=Biblioteca['obras']
    ObraExistente=input("Escriba el nombre de la obra => ")
    if ObraExistente in ObrasTotales:
            ObraPrestada=ObraExistente
            print("¡¡¡Gracias por pedir prestado el libro!!!")
    else:
        print("NO EXISTE ESA OBRA")
    resp=input("¿Desea pedir otro libro? ")
    if resp=='si':
        ObraExistente=input("Escriba el nombre de la obra => ")
        if ObraExistente==ObraPrestada:
            print("El libro ya fue prestado")





