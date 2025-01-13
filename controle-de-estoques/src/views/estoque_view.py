def mostrar_produtos(produtos):
    for produto in produtos:
        print(f'ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}, Preço: {produto.preco}')

def mostrar_mensagem(mensagem):
    print(mensagem)