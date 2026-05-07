from src.model.erros.erroValue import ErroValue,ErroValorNegativo
class Valor:

    def __init__(self,valor:float):
        self.__valor=valor


    def validarValor(self):

        if isinstance(self.__valor,float):
            if self.__valor>0:
                return self.__valor
            else:
                raise ErroValorNegativo("O valor deve ser positivo")


        else:
            raise ErroValue("Você deve digitar um valor decimal")