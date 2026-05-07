
class Fornecedor:

    def __init__(self,id_fornecedor:int=None,nome:str=None):
        self.__id_fornecedor=id_fornecedor
        self.__nome=nome

    @property
    def id_fornecedor(self):
        return self.__id_fornecedor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    def __eq__(self, other):
        return self.__id_fornecedor==other.id_fornecedor

    def fornecedor(self):
        return{
            "id_fornecedor":self.__id_fornecedor,
            "nome":self.__nome
        }

    @staticmethod
    def dict_to_object(data):
        return Fornecedor(
            data["nome"],
            data["id_fornecedor"]
        )