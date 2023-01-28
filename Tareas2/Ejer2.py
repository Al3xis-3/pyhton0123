texto="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estandar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido uso una galeria de textos y los mezclo de tal manera que logro hacer un libro de textos especimen."

print("Split => ", texto.split(sep=" ", maxsplit=63))
print("\n")
print("\n")
print("Join => ","".join(texto))
print("\n")
print("Count => ", texto.count("de"))
print("\n")
print("Found => ", texto.find("galeria"))
print("\n")
print("\n")
print("Uppercase => ", texto.upper())
print("\n")
print("Lowercase => ", texto.lower())

