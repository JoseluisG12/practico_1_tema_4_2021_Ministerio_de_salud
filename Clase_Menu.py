
class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {1:self.op1,
                           2:self.op2,

        }

    def run(self,lista_exeptuados,lista_organismos,organismos,exeptuados):
        band = True
        while band:
            b = int(input("""
Menu principal:
1-para saber cuantos exeptuados por edad y por enfermedad persistente hay por cada organismo del estado
2-listar por nombre de organismo a las personas exeptuadas en  orden alfabetico
3-salir
\n"""))
            func = self.__switcher.get(b)
            if func:
                func(lista_exeptuados,lista_organismos,organismos,exeptuados)
            else:
                print("saliendo...")
                band = False

    def op1(self,lista_exeptuados,lista_organismos,organismos,exeptuados):
        organismos.contarexeptuados(lista_exeptuados)

    def op2(self,lista_exeptuados,lista_organismos,organismos,exeptuados):
        exeptuados.listarexeptuados()