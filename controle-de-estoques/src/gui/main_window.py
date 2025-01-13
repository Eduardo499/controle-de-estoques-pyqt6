from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controle de Estoque")
        self.setFixedSize(800, 600)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
