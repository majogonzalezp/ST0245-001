def guardarchivoCSV(nombre):
    documento = open(nombre, "r")
    linea = documento.readlines()
    return linea
nombredelarchivo = input("ingrese el nombe del archivo CSV que desea leer")
#prueba1:
print(guardarchivoCSV(nombredelarchivo))
