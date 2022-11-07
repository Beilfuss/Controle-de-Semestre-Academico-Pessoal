class GrupoCheioException(ValueError):
    def __init__(self, err_msg="O grupo já está cheio!"):
        super().__init__(err_msg)
