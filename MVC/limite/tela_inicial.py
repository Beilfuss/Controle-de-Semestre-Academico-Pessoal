from turtle import bgcolor
import PySimpleGUI as sg
sg.theme('Reddit')


class TelaInicial():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__janela = None
        self.inicializar_componentes()

    def inicializar_componentes(self, dados_disciplinas=[]):

        cartoes = self.gerar_cartoes(dados_disciplinas)

        layout = [
            [sg.Text('Sistema de Gestão Acadêmica', font="bold",
                     justification="center", expand_x=True)],
            [sg.Text('Olá, [Aluno]! O que vamos fazer hoje?')],
            [sg.Text("Disciplinas")],
            cartoes,
            [sg.Button('Emitir Relatório'), sg.Button(
                'Cadastrar Disciplina'),  sg.Button('Finalizar Sistema', button_color="red")]
           
        ]

        self.__janela = sg.Window(
            'TelaInicial', default_element_size=(40, 1)).Layout(layout)

    def abrir(self, dados_disciplinas=[]):
        self.inicializar_componentes(dados_disciplinas)
        botao, valores = self.__janela.Read()
        return botao

    def close(self):
        self.__janela.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def gerar_cartoes(self, dados_disciplinas):

        frame_rows = []

        for index, disciplina in enumerate(dados_disciplinas):

            if disciplina['ativo'] == "Sim":
                frame_rows.append(sg.Frame(disciplina["nome"], [
                    [sg.Text("")],
                    [sg.Text("Média Parcial: -")],
                    [sg.Text("Faltas Remanescentes: -")],
                    [sg.Text("Risco de Reprovação: -")],
                    [sg.Text("Próxima Entrega: -")],
                    [sg.Button("Ver mais", key=index)]],
                    size=(200, 200),
                    relief="raised",  # raised, ridge, solid
                    element_justification="center",
                    vertical_alignment="center"))

        return frame_rows
