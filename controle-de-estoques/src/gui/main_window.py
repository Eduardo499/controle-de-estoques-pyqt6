from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QApplication
from gui.main_window_ui import Ui_menu

class MainWindow(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)