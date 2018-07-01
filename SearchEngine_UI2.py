# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchEngine_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:  #E1E2E1;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queryText = QtWidgets.QLineEdit(self.centralwidget)
        self.queryText.setGeometry(QtCore.QRect(60, 230, 481, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.queryText.setFont(font)
        self.queryText.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top: 1px solid #ddd;\n"
"border-bottom: 1px solid #ddd;\n"
"border-left: 1px solid #ddd;\n"
"border-right: 1px solid #ddd;\n"
"color: rgb(0, 8, 132);")
        self.queryText.setObjectName("queryText")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(560, 230, 201, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color:  #01579b;\n"
"border-top: 1px solid #ddd;\n"
"border-bottom: 1px solid #ddd;\n"
"border-left: 1px solid #ddd;\n"
"border-right: 1px solid #ddd;\n"
"color: #ECEFF1;")
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.boolean_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.boolean_2.setGeometry(QtCore.QRect(550, 340, 131, 20))
        self.boolean_2.setStyleSheet("color: rgb(0, 8, 132);")
        self.boolean_2.setObjectName("boolean_2")
        self.vectoriel = QtWidgets.QRadioButton(self.centralwidget)
        self.vectoriel.setEnabled(True)
        self.vectoriel.setGeometry(QtCore.QRect(560, 300, 141, 20))
        self.vectoriel.setStyleSheet("color: rgb(0, 8, 132);")
        self.vectoriel.setIconSize(QtCore.QSize(16, 16))
        self.vectoriel.setCheckable(True)
        self.vectoriel.setObjectName("vectoriel")
        self.freqWeightWisget = QtWidgets.QWidget(self.centralwidget)
        self.freqWeightWisget.setGeometry(QtCore.QRect(60, 290, 481, 161))
        self.freqWeightWisget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.freqWeightWisget.setObjectName("freqWeightWisget")
        self.termEdit = QtWidgets.QLineEdit(self.freqWeightWisget)
        self.termEdit.setGeometry(QtCore.QRect(10, 40, 141, 41))
        self.termEdit.setObjectName("termEdit")
        self.documentEdit = QtWidgets.QLineEdit(self.freqWeightWisget)
        self.documentEdit.setGeometry(QtCore.QRect(10, 110, 141, 41))
        self.documentEdit.setObjectName("documentEdit")
        self.resultWidget = QtWidgets.QWidget(self.freqWeightWisget)
        self.resultWidget.setGeometry(QtCore.QRect(210, 30, 261, 121))
        self.resultWidget.setStyleSheet("border-top: 1px solid #01579b;\n"
                                        "border-bottom: 1px solid #01579b;\n"
                                        "border-left: 1px solid #01579b;\n"
                                        "border-right: 1px solid #01579b;")
        self.resultWidget.setObjectName("resultWidget")
        self.freqLabel = QtWidgets.QLabel(self.resultWidget)
        self.freqLabel.setGeometry(QtCore.QRect(10, 40, 121, 31))
        self.freqLabel.setObjectName("freqLabel")
        self.weightLabel = QtWidgets.QLabel(self.resultWidget)
        self.weightLabel.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.weightLabel.setObjectName("weightLabel")
        self.calculatButton = QtWidgets.QPushButton(self.resultWidget)
        self.calculatButton.setGeometry(QtCore.QRect(150, 80, 101, 31))
        self.calculatButton.setObjectName("calculatButton")
        self.termLabel = QtWidgets.QLabel(self.freqWeightWisget)
        self.termLabel.setGeometry(QtCore.QRect(10, 20, 59, 14))
        self.termLabel.setObjectName("termLabel")
        self.documentLabel = QtWidgets.QLabel(self.freqWeightWisget)
        self.documentLabel.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.documentLabel.setObjectName("documentLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search Engine"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.boolean_2.setText(_translate("MainWindow", "Boolean Model"))
        self.vectoriel.setText(_translate("MainWindow", "Vectoriel Model"))
        self.freqLabel.setText(_translate("MainWindow", "Frequence"))
        self.weightLabel.setText(_translate("MainWindow", "Weight"))
        self.calculatButton.setText(_translate("MainWindow", "PushButton"))
        self.termLabel.setText(_translate("MainWindow", "Term"))
        self.documentLabel.setText(_translate("MainWindow", "Document"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

