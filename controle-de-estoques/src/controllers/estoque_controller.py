f

class EstoqueController:
    def __init__(self):


    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto_id):
        self.produtos = [p for p in self.produtos if p.id != produto_id]

    def listar_produtos(self):
        return self.produtos