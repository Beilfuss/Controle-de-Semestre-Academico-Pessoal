import PySimpleGUI as sg

class TelaAtividade():

    def __init__(self, controlador_atividade):
        self.__controlador_atividade = controlador_atividade
        self.__janela = None

    def inicializar_componentes(self):
        layout = [
            [sg.Text("atividade.nome")],
            [sg.Text("atividade.disciplina.nome")],
            [sg.Text("atividade.tipo")],
            [sg.Text("Data de entrega: atividade.data")],
            [sg.Text("Peso: atividade.peso")],
            [sg.Text("Nota: atividade.nota"), sg.Submit("Alterar nota", key="bt_alterar_nota")],
            [sg.Text("Priorizar: priorizar.boolean"), sg.Button("Priorizar", key="bt_priorizar")],
            [sg.Submit("Alterar atividade", key="bt_alterar_atividade"), sg.Submit("Voltar", key="bt_voltar")]
        ]
        self.__janela = sg.Window("Dados da atividade", element_justification="c").Layout(layout)

    def abrir(self):
        self.inicializar_componentes()
        evento, valores = self.__janela.Read()
        print(evento, valores)
        return evento, valores

    def fechar(self):
        self.__janela.Close()