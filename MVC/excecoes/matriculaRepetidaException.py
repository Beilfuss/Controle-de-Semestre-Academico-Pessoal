class MatriculaRepetidaException(ValueError):
    def __init__(self, err_msg="Matrícula repetida!"):
        super().__init__(err_msg)