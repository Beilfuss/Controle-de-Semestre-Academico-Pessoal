from limite.tela_colega import TelaColega


class ControladorColega:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela_colega = TelaColega(self)
        self.__colegas = []

    @property
    def colegas(self):
        return self.__nome
