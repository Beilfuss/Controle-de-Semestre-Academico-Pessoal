from limite.tela_dados_disciplina import TelaDadosDisciplina
from limite.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina
from dao.disciplina_dao import DisciplinaDAO
from excecoes.jaExistenteException import JaExistenteException


class ControladorDisciplina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_disciplina = TelaDisciplina(self)
        self.__tela_dados_disciplina = TelaDadosDisciplina(self)
        self.__dao = DisciplinaDAO()

    def listar_disciplinas(self):
        return [disciplina.desempacotar() for disciplina in self.__dao.buscar_todos()]

    def abrir_tela_disciplina(self, dados_disciplina):

        while(True):
            disciplina = self.__dao.obter_por_id(dados_disciplina["id"])
            #opcoes = {
            #"Voltar": self.__tela_dados_disciplina.fechar,
            #"Alterar Disciplina": self.alterar_disciplina,
            #"Excluir Disciplina": self.excluir_disciplina
            #}
        
            botao, valores = self.__tela_disciplina.abrir(dados_disciplina)
        
            #self.__tela_dados_disciplina.fechar()
            #if(botao != "Voltar"):
            #    opcoes[botao](dados_disciplina)

            if botao == "Voltar" or botao is None:
                self.__tela_disciplina.fechar()
                break;
            elif botao == "Alterar Disciplina":
                self.__tela_disciplina.fechar()
                self.alterar_disciplina(disciplina, dados_disciplina)
                break;
            elif botao == "Excluir Disciplina":
                self.__tela_disciplina.fechar()
                self.excluir_disciplina(disciplina.id)
                break;
            elif botao == "Colegas":
                self.__tela_disciplina.fechar()
                self.abrir_tela_colegas(disciplina)

    def abrir_tela_colegas(self, disciplina):


        opcoes = {0: "", 1: lambda colega: self.remover_colega(disciplina, colega), 2:lambda colega:self.incluir_colega(disciplina, colega)}

        (operacao, colega) = self.__controlador_sistema.inicializar_colegas(disciplina.nome, disciplina.colegas)

        if(operacao != 0):
            opcoes[operacao](colega)
            self.abrir_tela_colegas(disciplina)

    def incluir_disciplina(self):
        
        while True:
            
            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(dados_disciplina={"nome": "", "codigo": "", "professor": "",
                                        "numAulas": "", "rec": ""})

            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break
            
            validacao = self.verificar_validade(dados_disciplina)
            
            if validacao == True:
                self.__dao.persist_disciplina(dados_disciplina)
                break
        
        '''alteracao = False

        while True:

                #Troquei dados_disciplina != None por dados_disciplina is not None, conforme pep8:

                #https://peps.python.org/pep-0008/

                #Comparisons to singletons like None should always be done with is or is not, never the equality operators.

                #Also, beware of writing if x when you really mean if x is not None – e.g. when testing whether a variable or argument that 
                #defaults to None was set to some other value. The other value might have a type (such as a container) that could be false 
                #in a boolean context!

            if dados_disciplina is not None:
                alteracao = True
                dados_disciplina_old = dados_disciplina
                botao, dados_disciplina = self.__tela_dados_disciplina.abrir(dados_disciplina)


            else:
                botao, dados_disciplina = self.__tela_dados_disciplina.abrir(
                dados_disciplina={"nome": "", "codigo": "", "professor": "",
                                  "numAulas": "", "rec": ""})

            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break

            

                
                
                #retirados os argumentos none em conformidade com a assinatura do método alterado. Os dados aulas, colegas, atividades, etc, nunca serão 
                #conhecidos ou informados na tela de cadastro/alteração, logo acredito que não precisam estar aqui como argumentos
                
                #Troquei para enviar o próprio dicionário recebido pela tela

                sucesso = self.__dao.persist_disciplina(dados_disciplina)
                
                if not sucesso:
                    self.__tela_disciplina.mostrar_mensagem("Atenção", "Disciplina já cadastrada!")

                if alteracao == True:
                    return dados_disciplina

                break'''

    def alterar_disciplina(self, disciplina, dados_disciplina):

        while True:
        
            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(dados_disciplina)
            
            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break
            
            validacao = self.verificar_validade(dados_disciplina)
            
            if validacao == True:
                dados_disciplina['id'] = disciplina.id
                self.__dao.alterar_disciplina(dados_disciplina)
                break


        '''
            #1- Criar método alterar_disciplina no dao
            #2- Usar query: UPDATE DISCIPLINAS SET nome = ?, codigo = ?, numAulas = ?, rec = ?, professor = ? WHERE id = ? 
            #3- Setar os query_params, observando a ordem
            #4- Adaptar a query se necessário
            #5- Após atualizar o banco de dados, atualizar o objeto disciplina correspondente - usar o id para buscar no cache

        dados_disciplina_old = dados_disciplina
        dados_disciplina = self.incluir_disciplina(dados_disciplina)

        #alterado != None para is not None conforme comentário anterior
        if dados_disciplina is not None:
            if dados_disciplina['codigo'] != dados_disciplina_old['codigo']:
                self.excluir_disciplina(dados_disciplina_old['codigo'])'''
            
    def excluir_disciplina(self, id):
        #alteração para usar id no lugar de código
        self.__dao.delete_disciplina(id)

        '''
        Por enquanto você está usando código como identificador único, que deverá mudar para id posteriormente.
        Os seguintes passos devem funcionar com código e provavelmente quando trocar com id, mas podem ser necessárias adaptações
        - Passo 1: método excluir_disciplina deverá receber o código/id da disciplina como argumento. Fácil de fazer, pois o método abrir tela recebe os dados da disciplina, que incluem o código e incluirão o id
        - Passo 2: chamar o método delete disciplina do DAO, passando o código da disciplina como argumento em vez de um index. Trocar o nome do argumento para representar corretamente
        - Passo 3: excluir a linha disciplina = list(... etc, não será necessária
        - Passo 4: Corrigir a query conforme o nome da tabela. Utilizar o codigo/id da disciplina com parâmetro
        - Passo 5: Excluir a disciplina do cache, usando o codigo/id como argumento do pop
        '''

    def verificar_validade(self, dados_disciplina):
        try:
            dados_disciplina['numAulas'] = int(dados_disciplina["numAulas"])

            if dados_disciplina[0]:
                dados_disciplina["rec"] = "Sim" # Tem REC
            else:
                dados_disciplina["rec"] = "Não" # Não tem REC

            if dados_disciplina == {"nome": "", "codigo": "", "professor": "", "numero_aulas": "", "rec": ""
                    } or (not (dados_disciplina["nome"]).isalpha()) or not ((dados_disciplina["professor"]).isalpha()):
                #Nome D1cisplin4 passa na validação de nome ou nome Math3us passa na de professor.
                #ver método isalpha na documentação (https://docs.python.org/3/library/stdtypes.html#string-methods)
                #Não seria melhor usar algo do tipo  "not dados_disciplina["nome"].isalpha()"?

                #Corrigido. Pode ser assim?
                    
                raise ValueError

            disciplinas = self.__dao.buscar_todos()
            for disciplina in disciplinas:
                #Nome da disciplina é um bom critério para decidir se a disciplina já existe ou não?
                #Troquei por código. Será que "nome" e "código" ficariam melhor?
                # Id não dá para usar porque só é criado quando vai para o BD, certo?
                if disciplina.codigo == dados_disciplina['codigo']:
                    raise JaExistenteException
                
            return True

        except ValueError:
            self.__tela_disciplina.mostrar_mensagem("Atenção", "Dados inválidos. Tente novamente!")
            return False
        except JaExistenteException:
            self.__tela_disciplina.mostrar_mensagem('Atenção', 'Disciplina já existente, tente novamente!')
            return False


    def incluir_colega(self, disciplina, colega):
                
        sucesso = self.__dao.incluir_colega(disciplina, colega)

        if(not sucesso):
            self.__tela_disciplina.mostrar_mensagem("Atenção", "Colega já cadastrado!")

    def remover_colega(self, disciplina, colega):
        
        sucesso = self.__dao.remover_colega(disciplina, colega)
        return