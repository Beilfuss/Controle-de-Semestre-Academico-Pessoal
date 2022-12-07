class MissingDateException(ValueError):
    def __init__(self, err_msg="É necessário preencher a data de entrega"):
        super().__init__(err_msg)
