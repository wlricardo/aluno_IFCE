class Aluno:
    def __init__(self, codigo, nome, nascimento, ap1=11.0, ap2=11.0):
        self.__codigo = codigo
        self.__nome = nome
        self.__nascimento = nascimento
        if 0.0 <= ap1 <= 10.0:
            self.__ap1 = ap1
        else:
            self.__ap1 = 11.0
        if 0.0 <= ap2 <= 10.0:
            self.__ap1 = ap1
        else:
            self.__ap2 = 11.00
            
        def get_nascimento:
            return self.__nascimento
        
        
        def get_ap1:
            return self.__ap1
        
        def get_ap2:
            return self.__ap2