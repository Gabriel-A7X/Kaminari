# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Funcionario.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Funcionario(object):
    def setupUi(self, Tela_Funcionario):
        Tela_Funcionario.setObjectName("Tela_Funcionario")
        Tela_Funcionario.resize(1356, 892)
        self.centralwidget = QtWidgets.QWidget(Tela_Funcionario)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 50, 1221, 761))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(160, 80, 179, 291))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(350, 290, 199, 24))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget_4)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(350, 80, 631, 201))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 340, 199, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 370, 296, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 370, 631, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_4.addWidget(self.lineEdit_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_4.addWidget(self.lineEdit_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_4.addWidget(self.lineEdit_5)
        self.CadEnc = QtWidgets.QPushButton(self.tab)
        self.CadEnc.setGeometry(QtCore.QRect(540, 620, 141, 51))
        self.CadEnc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CadEnc.setStyleSheet("background-color: rgb(0, 147, 0);\n"
"color: rgb(255, 255, 255);")
        self.CadEnc.setObjectName("CadEnc")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(910, 630, 291, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(730, 630, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(720, 670, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(910, 670, 291, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(90, 50, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(270, 56, 621, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(120, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(280, 110, 121, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.Info_pacote = QtWidgets.QTextBrowser(self.tab_2)
        self.Info_pacote.setGeometry(QtCore.QRect(40, 240, 531, 341))
        self.Info_pacote.setObjectName("Info_pacote")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(130, 180, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 50, 111, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(600, 270, 125, 101))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_9.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_9.addWidget(self.label_32)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(730, 260, 461, 121))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout_10.addWidget(self.lineEdit_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout_10.addWidget(self.lineEdit_21)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(886, 406, 131, 51))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1160, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        Tela_Funcionario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Funcionario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1356, 26))
        self.menubar.setObjectName("menubar")
        Tela_Funcionario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Funcionario)
        self.statusbar.setObjectName("statusbar")
        Tela_Funcionario.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Funcionario)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Tela_Funcionario)

    def retranslateUi(self, Tela_Funcionario):
        _translate = QtCore.QCoreApplication.translate
        Tela_Funcionario.setWindowTitle(_translate("Tela_Funcionario", "MainWindow"))
        self.label.setText(_translate("Tela_Funcionario", "Peso"))
        self.label_4.setText(_translate("Tela_Funcionario", "Altura"))
        self.label_3.setText(_translate("Tela_Funcionario", "Comprimento"))
        self.label_5.setText(_translate("Tela_Funcionario", "Profundidade"))
        self.label_7.setText(_translate("Tela_Funcionario", "É Frágil?"))
        self.label_8.setText(_translate("Tela_Funcionario", "Tipo de Entrega"))
        self.radioButton_2.setText(_translate("Tela_Funcionario", "Sim"))
        self.radioButton.setText(_translate("Tela_Funcionario", "Não"))
        self.radioButton_3.setText(_translate("Tela_Funcionario", "Normal"))
        self.radioButton_4.setText(_translate("Tela_Funcionario", "Expresso"))
        self.label_2.setText(_translate("Tela_Funcionario", "Nome do Remetente"))
        self.label_6.setText(_translate("Tela_Funcionario", "Nome do Destinatario"))
        self.label_9.setText(_translate("Tela_Funcionario", "Onde está sendo postado?"))
        self.label_10.setText(_translate("Tela_Funcionario", "Para onde vai?"))
        self.CadEnc.setText(_translate("Tela_Funcionario", "Cadastrar"))
        self.label_12.setText(_translate("Tela_Funcionario", "Codigo Gerado"))
        self.label_15.setText(_translate("Tela_Funcionario", "Preço Calculado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Tela_Funcionario", "Cadastrar um pacote"))
        self.label_11.setText(_translate("Tela_Funcionario", "Código de Rastreio"))
        self.label_13.setText(_translate("Tela_Funcionario", "Ler QRcode"))
        self.pushButton.setText(_translate("Tela_Funcionario", "Ler"))
        self.label_14.setText(_translate("Tela_Funcionario", "Informações sobre a encomenda"))
        self.pushButton_2.setText(_translate("Tela_Funcionario", "Buscar"))
        self.label_31.setText(_translate("Tela_Funcionario", "Chegou em:"))
        self.label_32.setText(_translate("Tela_Funcionario", "Vai para:"))
        self.pushButton_7.setText(_translate("Tela_Funcionario", "Atualizar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Tela_Funcionario", "Buscar"))
        self.pushButton_3.setText(_translate("Tela_Funcionario", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Funcionario = QtWidgets.QMainWindow()
    ui = Ui_Tela_Funcionario()
    ui.setupUi(Tela_Funcionario)
    Tela_Funcionario.show()
    sys.exit(app.exec_())
