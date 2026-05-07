import json
from json import JSONDecodeError


class GeradorID:

    def __init__(self,path_file,atributo):
        self.path_file=fr"C:\Users\gabriel.rrossi2\PycharmProjects\SistemaLimpeza\src\infrastructure\database\{path_file}"
        self.id_gerado=None
        try:
            with open(self.path_file,"r",encoding="utf-8")as file:
                lista=json.load(file)
                lista_ids=(data[atributo] for data in lista)
                self.id_gerado=max(lista_ids)+1

        except JSONDecodeError as e:
            self.id_gerado=1


if __name__ == '__main__':
    idNovo=GeradorID(r"produtos.json","id").id_gerado
    print(idNovo)