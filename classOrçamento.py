import classItem

class Orcamento():
    def __init__(self,valor):
        self.itens = []
        self.valor = valor
    
    def add_itens(self, nome, valor):
        self.itens.append( classItem.item(nome, valor) )