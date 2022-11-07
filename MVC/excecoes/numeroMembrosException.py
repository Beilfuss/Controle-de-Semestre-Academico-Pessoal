class NumeroMembrosException(ValueError):
    def __init__(self, err_msg="O número de membros informado é inferior a 2 ou ao número de membros já cadastrados"):
        super().__init__(err_msg)
