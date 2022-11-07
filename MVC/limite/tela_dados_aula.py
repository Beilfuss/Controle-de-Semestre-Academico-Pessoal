import PySimpleGUI as sg


class TelaDadosAula():

    def __init__(self, controlador_aula):
        self.__controlador_aula = controlador_aula
        self.__janela = None
        self.inicializar_componentes(dados_aula={"sala": "", "dia": "", "horarios": "", "alteracao": False})

    def inicializar_componentes(self, dados_aula):

        horarios = dados_aula['horarios']
        dados_tabela = []
        for horario in horarios:
            dados_tabela.append([dados_aula['dia'], horario])

        layout = [
            [sg.Text('Cadastro de Aula', font="bold", justification="center", expand_x=True)],
            [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"],
                                                          key='sala', tooltip="Ex.: CTC304")],
            [sg.Text('Horários:', font="bold", justification="center", expand_x=True)],
            [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", size=(10, 1), key='Segunda-feira'), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira', size=(10, 1)), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira'), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira'), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira'), sg.Radio('Sábado', "RADIO1", key='Sábado')],

            [sg.Text('Horário*'), sg.Combo(['07:30 - 08:20', '08:20 - 09:10', '09:10 - 10:10', '10:10 - 11:00', '11:00 - 11:50',
                                            '13:30 - 14:20', '14:20 - 15:10', '15:10 - 16:20', '16:20 - 17:10', '17:10 - 18:00',
                                            '18:30 - 19:20', '19:20 - 20:20', '20:20 - 21:10', '21:10 - 22:00'], key="horario")],

            [sg.Submit(button_text="Adicionar Horário")],

            [sg.Table(dados_tabela, headings=[
                "Dia", "Horário", "Sala"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            
            [sg.Submit(button_text="Excluir Horário")],
            [sg.Cancel(button_text="Cancelar", button_color="red"),
             sg.Submit(button_text="Cadastrar Aula")]
        ]

        if dados_aula['dia'] == 'Segunda-feira':
            if dados_aula['alteracao'] == False:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304", disabled=True)]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira', default = True, disabled=True), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira', disabled=True), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira', disabled=True), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira', disabled=True), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira', disabled=True), sg.Radio('Sábado', "RADIO1", key='Sábado', disabled=True)]
            else:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304")]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira', default = True), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira'), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira'), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira'), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira'), sg.Radio('Sábado', "RADIO1", key='Sábado')]
        elif dados_aula['dia'] == 'Quarta-feira':
            if dados_aula['alteracao'] == False:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304", disabled=True)]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira', disabled=True), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira', default = True, disabled=True), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira', disabled=True), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira', disabled=True), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira', disabled=True), sg.Radio('Sábado', "RADIO1", key='Sábado', disabled=True)]
            else:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304")]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira'), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira', default = True), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira'), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira'), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira'), sg.Radio('Sábado', "RADIO1", key='Sábado')]
        elif dados_aula['dia'] == 'Sexta-feira':
            if dados_aula['alteracao'] == False:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304", disabled=True)]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira', disabled=True), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira', disabled=True), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira', default = True, disabled=True), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira', disabled=True), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira', disabled=True), sg.Radio('Sábado', "RADIO1", key='Sábado', disabled=True)]
            else:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304")]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira'), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira'), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira', default = True), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira'), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira'), sg.Radio('Sábado', "RADIO1", key='Sábado')]
        elif dados_aula['dia'] == 'Terça-feira':
            if dados_aula['alteracao'] == False:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304", disabled=True)]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira', disabled=True), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira', disabled=True), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira', disabled=True), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira', default = True, disabled=True), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira', disabled=True), sg.Radio('Sábado', "RADIO1", key='Sábado', disabled=True)]
            else:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304")]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira'), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira'), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira'), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira', default = True), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira'), sg.Radio('Sábado', "RADIO1", key='Sábado')]
        elif dados_aula['dia'] == 'Quinta-feira':
            if dados_aula['alteracao'] == False:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304", disabled=True)]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira', disabled=True), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira', disabled=True), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira', disabled=True), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira', disabled=True), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira', default = True, disabled=True), sg.Radio('Sábado', "RADIO1", key='Sábado', disabled=True)]
            else:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304")]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira'), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira'), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira'), sg.Radio('Terça-feira', "RADIO1", key='Terça-feira'), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira', default = True), sg.Radio('Sábado', "RADIO1", key='Sábado')]
        elif dados_aula['dia'] == 'Sábado':
            if dados_aula['alteracao'] == False:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304", disabled=True)]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira', disabled=True), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira', disabled=True), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira', disabled=True), sg.Radio('Sábado', "RADIO1", key='Terça-feira', disabled=True), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira', disabled=True), sg.Radio('Sábado', "RADIO1", key='Sábado', default = True, disabled=True)]
            else:
                layout[1] = [sg.Text("Sala*", size=(10, 1)), sg.InputText(dados_aula["sala"], key='sala', tooltip="Ex.: CTC304")]
                layout[3] = [sg.Text("Dia*"), sg.Radio('Segunda-feira', "RADIO1", key='Segunda-feira'), sg.Radio('Quarta-feira', "RADIO1", key='Quarta-feira'), sg.Radio('Sexta-feira', "RADIO1", key='Sexta-feira'), sg.Radio('Sábado', "RADIO1", key='Terça-feira'), sg.Radio('Quinta-feira', "RADIO1", key='Quinta-feira'), sg.Radio('Sábado', "RADIO1", key='Sábado', default = True)]
                
        self.__janela = sg.Window('Dados da Aula').Layout(layout)

    def abrir(self, dados_aula):
        self.inicializar_componentes(dados_aula)
        botao, valores = self.__janela.Read()
        return botao, valores

    def fechar(self):
        self.__janela.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)