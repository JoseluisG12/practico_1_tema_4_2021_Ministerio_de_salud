import csv
from Clase_Personal_exeptuado import Personal
class Lista_Exeptuados:
    __exeptuados : list

    def __init__(self):
        self.__exeptuados = []

    def cargadatos(self):
        archivo = open('Personal-exceptuado.csv')
        reader = csv.reader(archivo,delimiter=(';'))
        next(reader)
        for fila in reader:
            nombre = fila[0]
            apellido = fila[1]
            direccion = fila[2]
            dni = fila[3]
            edad = fila[4]
            telefono = fila[5]
            factor = fila[6]
            organismo = fila[7]
            exeptuado = Personal(nombre,apellido,direccion,dni,edad,telefono,factor,organismo)
            self.__exeptuados.append(exeptuado)
        archivo.close()

    def getlista(self):
        return self.__exeptuados

    def listarexeptuados(self):
        nombre = input("ingrese el nombre del organismo a listar sus exeptuados\n")
        lista_exeptuados = []
        for exeptuado in self.__exeptuados:
            if exeptuado.getorganismo() == nombre and exeptuado.getedad() < 60:
                lista_exeptuados.append(exeptuado)
        lista_exeptuados.sort()
        print("""
organismo {}
""".format(nombre))
        for exeptuado in lista_exeptuados:
            print("""
Nombre:{}
Apellido:{}
Dni:{}
Edad:{}""".format(exeptuado.getnombre(),exeptuado.getapellido(),exeptuado.getdni(),exeptuado.getedad()))
