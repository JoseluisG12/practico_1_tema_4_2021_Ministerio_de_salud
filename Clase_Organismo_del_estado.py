
class Estado:
    __nombre : str
    __domicilio : str
    __localidad : str
    __telefono : int

    def __init__(self,nombre,domicilio,localidad,telefono):
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__localidad = localidad
        self.__telefono = telefono

    def getnombre(self):
        return self.__nombre
