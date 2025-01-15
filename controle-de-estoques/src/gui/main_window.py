from PyQt6.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
from gui.main_window_ui import Ui_menu
from utils.database import conectar, executar_consulta, desconectar

class MainWindow(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adicionar_item.clicked.connect(self.adicionar_produto)

    def adicionar_produto(self):
        codigo = self.codigo.text()
        quantidade = self.quantidade.text()
        preco = self.preco.text()

        if not codigo or not quantidade or not preco:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos")
            return

        try:
            quantidade = int(quantidade)
            preco = float(preco)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Quantidade deve ser um número inteiro e preço deve ser um número decimal")
            return

        conexao = conectar()
        consulta_verificar = "SELECT nome_produto FROM estoque WHERE codigo = ?"
        cursor = conexao.cursor()
        cursor.execute(consulta_verificar, (codigo,))
        resultado = cursor.fetchone()

        if not resultado:
            QMessageBox.warning(self, "Erro", "Código do produto não encontrado no banco de dados. Adicionando novo produto.")
            nome, ok = QInputDialog.getText(self, "Nome do Produto", "Digite o nome do produto:")
            if not ok or not nome:
                QMessageBox.warning(self, "Erro", "Nome do produto deve ser preenchido")
                desconectar(conexao)
                return

            consulta_inserir = "INSERT INTO estoque (codigo, nome_produto, quantidade, preco) VALUES (?, ?, ?, ?)"
            parametros = (codigo, nome, quantidade, preco)
            executar_consulta(conexao, consulta_inserir, parametros)
            QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso")
        else:
            nome = resultado[0]
            consulta_atualizar = "UPDATE estoque SET quantidade = ?, preco = ? WHERE codigo = ?"
            parametros = (quantidade, preco, codigo)
            executar_consulta(conexao, consulta_atualizar, parametros)
            QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso")

        desconectar(conexao)
        self.codigo.clear()
        self.quantidade.clear()
        self.preco.clear()