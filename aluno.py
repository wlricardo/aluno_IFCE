class Aluno:
    def __init__(self, codigo, nome, nascimento, ap1=11.0, ap2=11.0):
        self.__codigo = codigo
        self.__nome = nome
        self.__nascimento = nascimento
        self.__api = ap1
        self.__ap2 = ap2