class ValidationException(ValueError):
    def __init__(self, err_msg="Houve um erro de validação."):
        super().__init__(err_msg)