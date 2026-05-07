
class Produto:

    def __init__(self,id_produto:int,nome:str,marca:str,id_fornecedor:int,valor:float=None):
        self.__id_produto=id_produto
        self.__nome=nome
        self.__marca=marca
        self.__id_fornecedor = id_fornecedor
        self.__valor=valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self,marca):
        self.__marca=marca

    @property
    def id_produto(self):
        return self.__id_produto

    @property
    def id_fornecedor(self):
        return self.__id_fornecedor

    def __eq__(self, other):
        return self.__id_produto==other.id_produto

    def produtoDict(self):
        return{
            "id":self.__id_produto,
            "nome":self.__nome,
            "marca":self.__marca,
            "id_fornecedor":self.__id_fornecedor,
            "valor":self.__valor
        }

    @staticmethod
    def dict_to_object(data):
        return Produto(
            data["id"],
            data["nome"],
            data["marca"],
            data["id_fornecedor"],
            data["valor"]
        )