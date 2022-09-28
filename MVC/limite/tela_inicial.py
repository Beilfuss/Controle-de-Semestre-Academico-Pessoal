import PySimpleGUI as sg

class TelaInicial():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__janela = None
        self.inicializar_componentes()

    def inicializar_componentes(self):
        layout = [
            [sg.Text('Sistema de Gestão Acadêmica')],
            [sg.Text('Olá, [Aluno]! O que vamos fazer hoje?')],
            [sg.Button('Cadastrar Disciplina'),  sg.Button('Finalizar Sistema')]
        ]

        self.__janela = sg.Window('TelaInicial', default_element_size=(40, 1)).Layout(layout)

    def abrir(self):
        botao, valores = self.__janela.Read()
        return botao

    def close(self):
        self.__janela.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)