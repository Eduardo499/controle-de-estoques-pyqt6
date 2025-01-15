from PyQt6.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
from gui.main_window_ui import Ui_menu
from utils.database import conectar, executar_consulta, desconectar
from gui.tabela import Ui_tabela

class MainWindow(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adicionar_item.clicked.connect(self.adicionar_produto)
        self.ver_estoque.clicked.connect(self.mostrar_estoque)

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

    def mostrar_estoque(self):
        self.tabela_window = TabelaWindow()
        self.tabela_window.show()

class TabelaWindow(QWidget, Ui_tabela):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.voltar)
        self.carregar_dados()

    def carregar_dados(self):
        conexao = conectar()
        consulta = "SELECT codigo, nome_produto, quantidade, preco FROM estoque"
        cursor = conexao.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        desconectar(conexao)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(len(resultados))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Código", "Nome do Produto", "Quantidade", "Preço"])

        for i, linha in enumerate(resultados):
            for j, valor in enumerate(linha):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(valor)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def voltar(self):
        self.close()