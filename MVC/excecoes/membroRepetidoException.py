class MembroRepetidoException(ValueError):
    def __init__(self, err_msg="Colega já está no grupo"):
        super().__init__(err_msg)