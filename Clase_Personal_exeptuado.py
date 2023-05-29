
class Personal:
    __apellido : str
    __nombre : str
    __direccion : str
    __dni : str
    __edad : int
    __telefono : int
    __factor : str
    __organismo : str

    def __init__(self,nombre,apellido,direccion,dni,edad,telefono,factor,organismo):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = int(dni)
        self.__edad = int(edad)
        self.__telefono = telefono
        self.__factor = factor
        self.__organismo = organismo

    def getorganismo(self):
        return self.__organismo

    def getfactor(self):
        return self.__factor

    def getnombre(self):
        return self.__nombre

    def getdni(self):
        return self.__dni

    def getapellido(self):
        return  self.__apellido

    def getedad(self):
        return self.__edad
    def __gt__(self, other):
        if self.__nombre > other.__nombre:
            return  True