import csv
from Clase_Organismo_del_estado import Estado
class Lista_organismos:
    __organismos : list

    def __init__(self):
        self.__organismos = []

    def cargadatos(self):
        archivo = open('Organismos-del-Estado.csv')
        reader = csv.reader(archivo,delimiter=(';'))
        next(reader)
        for fila in reader:
            nombre = fila[0]
            domicilio = fila[1]
            localidad = fila[2]
            telefono = fila[3]
            estado = Estado(nombre,domicilio,localidad,telefono)
            self.__organismos.append(estado)
        archivo.close()

    def getlista(self):
        return self.__organismos

    def contarexeptuados(self,exeptuados):
        for organismos in self.__organismos:
            contedad = 0
            contenfermedad = 0
            for exeptuado in exeptuados:
                if organismos.getnombre() == exeptuado.getorganismo():
                    if exeptuado.getfactor() == 'edad':
                        contedad = contedad + 1
                    elif exeptuado.getfactor() == 'enfermedad pre-existente':
                        contenfermedad = contenfermedad + 1
            print("""
{}
Exeptuados por edad: {}
Exeptuados por enfermedad persistente : {}""".format(organismos.getnombre(),contedad,contenfermedad))




