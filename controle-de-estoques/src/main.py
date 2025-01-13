# Conteúdo do arquivo: /controle-de-estoques/controle-de-estoques/src/main.py

from controllers.estoque_controller import EstoqueController
from views.estoque_view import mostrar_produtos, mostrar_mensagem

def main():
    estoque_controller = EstoqueController()
    
    while True:
        mostrar_mensagem("Bem-vindo ao Controle de Estoques!")
        mostrar_produtos(estoque_controller.listar_produtos())
        
        opcao = input("Escolha uma opção: 1 - Adicionar Produto, 2 - Remover Produto, 3 - Sair: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            estoque_controller.adicionar_produto(nome, quantidade, preco)
            mostrar_mensagem("Produto adicionado com sucesso!")
        
        elif opcao == '2':
            produto_id = int(input("ID do produto a ser removido: "))
            estoque_controller.remover_produto(produto_id)
            mostrar_mensagem("Produto removido com sucesso!")
        
        elif opcao == '3':
            mostrar_mensagem("Saindo do sistema...")
            break
        
        else:
            mostrar_mensagem("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()