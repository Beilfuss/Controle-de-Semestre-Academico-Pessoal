class JaExistenteException(Exception):
    def __init__(self):
        super().__init__('Ops, já existe uma entidade com esse nome!')