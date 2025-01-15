from PyQt6.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QTextEdit
from gui.main_window_ui import Ui_menu
from utils.database import conectar, executar_consulta, desconectar
import os
from datetime import datetime

class MainWindow(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adicionar_item.clicked.connect(self.adicionar_produto)
        self.ver_estoque.clicked.connect(self.mostrar_estoque)
        self.remove_item.clicked.connect(self.remover_produto)
        self.ver_relatorios.clicked.connect(self.abrir_relatorios)

    def log_acao(self, acao):
        log_path = os.path.join(os.path.dirname(__file__), '../db/log.txt')
        with open(log_path, 'a') as log_file:
            log_file.write(f"{datetime.now()}: {acao}\n")

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
        consulta_verificar = "SELECT nome_produto, quantidade, preco FROM estoque WHERE codigo = ?"
        cursor = conexao.cursor()
        cursor.execute(consulta_verificar, (codigo,))
        resultado = cursor.fetchone()

        if not resultado:
            nome, ok = QInputDialog.getText(self, "Nome do Produto", "Digite o nome do produto:")
            if not ok or not nome:
                QMessageBox.warning(self, "Erro", "Nome do produto deve ser preenchido")
                desconectar(conexao)
                return

            consulta_inserir = "INSERT INTO estoque (codigo, nome_produto, quantidade, preco) VALUES (?, ?, ?, ?)"
            parametros = (codigo, nome, quantidade, preco)
            executar_consulta(conexao, consulta_inserir, parametros)
            self.log_acao(f"Adicionado novo produto: {codigo}, {nome}, {quantidade}, {preco}")
            QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso")
        else:
            nome, quantidade_existente, preco_existente = resultado
            nova_quantidade = quantidade_existente + quantidade

            if preco != preco_existente:
                resposta = QMessageBox.question(self, "Preço Diferente", f"O preço atual é {preco_existente}. Deseja atualizar para {preco}?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if resposta == QMessageBox.StandardButton.Yes:
                    consulta_atualizar = "UPDATE estoque SET quantidade = ?, preco = ? WHERE codigo = ?"
                    parametros = (nova_quantidade, preco, codigo)
                    self.log_acao(f"Atualizado produto: {codigo}, nova quantidade: {nova_quantidade}, novo preço: {preco}")
                else:
                    consulta_atualizar = "UPDATE estoque SET quantidade = ? WHERE codigo = ?"
                    parametros = (nova_quantidade, codigo)
                    self.log_acao(f"Atualizado produto: {codigo}, nova quantidade: {nova_quantidade}, preço mantido: {preco_existente}")
            else:
                consulta_atualizar = "UPDATE estoque SET quantidade = ? WHERE codigo = ?"
                parametros = (nova_quantidade, codigo)
                self.log_acao(f"Atualizado produto: {codigo}, nova quantidade: {nova_quantidade}, preço mantido: {preco_existente}")

            executar_consulta(conexao, consulta_atualizar, parametros)
            QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso")

        desconectar(conexao)
        self.codigo.clear()
        self.quantidade.clear()
        self.preco.clear()

    def remover_produto(self):
        codigo = self.codigo.text()
        quantidade = self.quantidade.text()

        if not codigo or not quantidade:
            QMessageBox.warning(self, "Erro", "Código e quantidade devem ser preenchidos")
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Quantidade deve ser um número inteiro")
            return

        conexao = conectar()
        consulta_verificar = "SELECT quantidade FROM estoque WHERE codigo = ?"
        cursor = conexao.cursor()
        cursor.execute(consulta_verificar, (codigo,))
        resultado = cursor.fetchone()

        if not resultado:
            QMessageBox.warning(self, "Erro", "Produto não encontrado no estoque")
        else:
            quantidade_existente = resultado[0]
            nova_quantidade = quantidade_existente - quantidade

            if nova_quantidade < 0:
                QMessageBox.warning(self, "Erro", "Quantidade a remover excede a quantidade em estoque")
            elif nova_quantidade == 0:
                consulta_remover = "DELETE FROM estoque WHERE codigo = ?"
                executar_consulta(conexao, consulta_remover, (codigo,))
                self.log_acao(f"Removido produto: {codigo}, quantidade removida: {quantidade}")
                QMessageBox.information(self, "Sucesso", "Produto removido do estoque")
            else:
                consulta_atualizar = "UPDATE estoque SET quantidade = ? WHERE codigo = ?"
                parametros = (nova_quantidade, codigo)
                executar_consulta(conexao, consulta_atualizar, parametros)
                self.log_acao(f"Atualizado produto: {codigo}, quantidade removida: {quantidade}, nova quantidade: {nova_quantidade}")
                QMessageBox.information(self, "Sucesso", "Quantidade do produto atualizada com sucesso")

        desconectar(conexao)
        self.codigo.clear()
        self.quantidade.clear()

    def mostrar_estoque(self):
        self.tabela_window = TabelaWindow()
        self.tabela_window.show()

    def abrir_relatorios(self):
        self.rel_window = RelatoriosWindow()
        self.rel_window.show()

class TabelaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estoque")
        self.setGeometry(100, 100, 600, 400)
        self.pushButton = QPushButton("Voltar", self)
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

class RelatoriosWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relatórios")
        self.setGeometry(100, 100, 600, 400)
        self.textEdit = QTextEdit(self)
        self.pushButton = QPushButton("Voltar", self)
        self.pushButton.clicked.connect(self.voltar)
        self.carregar_relatorios()

    def carregar_relatorios(self):
        log_path = os.path.join(os.path.dirname(__file__), '../db/log.txt')
        
        # Verifica se o arquivo existe, se não, cria o arquivo
        if not os.path.exists(log_path):
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            with open(log_path, 'w') as log_file:
                log_file.write('')

        with open(log_path, 'r') as log_file:
            conteudo = log_file.read()
        self.textEdit.setText(conteudo)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def voltar(self):
        self.close()