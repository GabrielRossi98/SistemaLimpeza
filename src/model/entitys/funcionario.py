class Funcionario:

    def __init__(self,id_funcionario:int=None,nome:str=None):
        self.__id_funcionario=id_funcionario
        self.__nome=nome

    @property
    def id_funcionario(self):
        return self.__id_funcionario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    def __eq__(self, other):
        return self.__id_funcionario==other.id_funcionario

    def funcionario(self):
        return {
            "id_funcionario":self.__id_funcionario,
            "nome": self.__nome
        }

    @staticmethod
    def dict_to_object(data):
        return Funcionario(
            data["id_funcionario"],
            data["nome"]
        )