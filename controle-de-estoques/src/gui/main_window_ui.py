# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(510, 454)
        icon = QtGui.QIcon.fromTheme("applications-other")
        menu.setWindowIcon(icon)
        menu.setToolTipDuration(2)
        self.centralwidget = QtWidgets.QWidget(parent=menu)
        self.centralwidget.setToolTipDuration(6)
        self.centralwidget.setObjectName("centralwidget")
        self.ver_estoque = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ver_estoque.setGeometry(QtCore.QRect(40, 320, 111, 41))
        self.ver_estoque.setObjectName("ver_estoque")
        self.ver_relatorios = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ver_relatorios.setGeometry(QtCore.QRect(160, 320, 91, 41))
        self.ver_relatorios.setObjectName("ver_relatorios")
        self.adicionar_item = QtWidgets.QPushButton(parent=self.centralwidget)
        self.adicionar_item.setGeometry(QtCore.QRect(260, 320, 91, 41))
        self.adicionar_item.setObjectName("adicionar_item")
        self.remove_item = QtWidgets.QPushButton(parent=self.centralwidget)
        self.remove_item.setGeometry(QtCore.QRect(360, 320, 101, 41))
        self.remove_item.setObjectName("remove_item")
        self.codigo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(140, 150, 221, 31))
        self.codigo.setObjectName("codigo")
        self.quantidade = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.quantidade.setGeometry(QtCore.QRect(140, 181, 221, 31))
        self.quantidade.setObjectName("quantidade")
        self.preco = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.preco.setGeometry(QtCore.QRect(140, 210, 221, 31))
        self.preco.setObjectName("preco")
        self.label_codigo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_codigo.setGeometry(QtCore.QRect(60, 160, 61, 20))
        self.label_codigo.setObjectName("label_codigo")
        self.label_preco = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_preco.setGeometry(QtCore.QRect(60, 220, 57, 14))
        self.label_preco.setObjectName("label_preco")
        self.label_quantidade = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_quantidade.setGeometry(QtCore.QRect(60, 190, 71, 20))
        self.label_quantidade.setObjectName("label_quantidade")
        menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 19))
        self.menubar.setObjectName("menubar")
        menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=menu)
        self.statusbar.setObjectName("statusbar")
        menu.setStatusBar(self.statusbar)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Controle de Estoques Python"))
        self.ver_estoque.setText(_translate("menu", "Ver estoque"))
        self.ver_relatorios.setText(_translate("menu", "Ver relatórios"))
        self.adicionar_item.setText(_translate("menu", "Adicionar item"))
        self.remove_item.setText(_translate("menu", "Remover item"))
        self.label_codigo.setText(_translate("menu", "Código"))
        self.label_preco.setText(_translate("menu", "Preço"))
        self.label_quantidade.setText(_translate("menu", "Quantidade"))
