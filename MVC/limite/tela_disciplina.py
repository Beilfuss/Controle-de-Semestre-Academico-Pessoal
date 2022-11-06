import PySimpleGUI as sg


class TelaDisciplina():

    def __init__(self, controlador_disciplina):
        self.__controlador_disciplina = controlador_disciplina
        self.__janela = None
        self.inicializar_componentes()

    def inicializar_componentes(self, dados_disciplinas=None):
        if dados_disciplinas is None:
            dados_disciplinas = {'nome': '', 'codigo': '', 'professor': '', 'numAulas': '',
                                 0: '', 1: '', 'rec': '', 'aulas': ''}
            
        aulas = dados_disciplinas['aulas']
        dados_tabela = []
        for aula in aulas:
            for horario in aula['horario']:
                dados_tabela.append([aula['dia'], horario[0], aula['sala']])

        layout = [
            [sg.Text("{codigo} - {nome}".format(codigo=dados_disciplinas['codigo'], nome=dados_disciplinas['nome']), font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Professor: {professor}".format(
                professor=dados_disciplinas['professor']))],
            [sg.Text("Recuperação: {rec}".format(
                rec=dados_disciplinas['rec']))],
            [sg.Text("Média Parcial: ")],
            [sg.Text("Faltas Remanescentes: ")],
            [sg.Submit(button_text="Encerrar Disciplina", button_color="red"), sg.Submit(
                button_text="Colegas"), sg.Submit(button_text="Registrar Falta")],
            [sg.Text("")],
            [sg.Text("Lista de Atividades")],
            [sg.Table([['Trabalho de APS', '03/10/2022', 'Trabalho', '40%', 'Sim', 10], ], ['Atividade',
                      'Data de Entrega', 'Tipo', 'Peso', 'Grupo', 'Prioridade'], num_rows=2, justification='left')],
            [sg.Submit(button_text="Ver Atividade"), sg.Submit(
                button_text="Cadastrar Atividade")],
            [sg.Text("")],
            [sg.Text("Aulas")],

            [sg.Table(dados_tabela, headings=[
                "Dia", "Horário", "Sala"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
                      
            [sg.Submit(button_text="Excluir Aula", button_color="red"), sg.Submit(button_text="Alterar Aula"), sg.Submit(button_text="Cadastrar Aula")],
            [sg.Text("")],
            [sg.Submit(button_text="Excluir Disciplina", button_color="red"), sg.Submit(button_text="Alterar Disciplina"),
             sg.Submit(button_text="Voltar")]
        ]

        self.__janela = sg.Window(
            "TelaDisciplina", default_element_size=(40, 1)).Layout(layout)

    def abrir(self, dados_disciplina=[]):
        self.inicializar_componentes(dados_disciplina)
        botao, valores = self.__janela.Read()
        return botao, valores

    def fechar(self):
        self.__janela.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
