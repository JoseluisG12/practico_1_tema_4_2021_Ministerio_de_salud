from Manejador_organismos import Lista_organismos
from Manejador_exeptuados import  Lista_Exeptuados
from Clase_Menu import  Menu
if __name__=='__main__':
    organismos = Lista_organismos()
    exeptuados = Lista_Exeptuados()
    organismos.cargadatos()
    exeptuados.cargadatos()
    lista_organismos = organismos.getlista()
    lista_exeptuados = exeptuados.getlista()
    menu = Menu()
    menu.run(lista_exeptuados,lista_organismos,organismos,exeptuados)

