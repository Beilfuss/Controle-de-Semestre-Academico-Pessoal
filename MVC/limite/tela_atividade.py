import PySimpleGUI as sg


class TelaAtividade:

    def __init__(self, controlador_atividade):
        self.__controlador_atividade = controlador_atividade
        self.__janela = None
