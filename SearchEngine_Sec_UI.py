# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchEngine_Sec_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:  #E1E2E1;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queryTextSec = QtWidgets.QLineEdit(self.centralwidget)
        self.queryTextSec.setGeometry(QtCore.QRect(30, 50, 481, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.queryTextSec.setFont(font)
        self.queryTextSec.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"                                    border-top: 1px solid #ddd;\n"
"                                    border-bottom: 1px solid #ddd;\n"
"                                    border-left: 1px solid #ddd;\n"
"                                    border-right: 1px solid #ddd;\n"
"                                    color: rgb(0, 8, 132);")
        self.queryTextSec.setObjectName("queryTextSec")
        self.searchButtonSec = QtWidgets.QPushButton(self.centralwidget)
        self.searchButtonSec.setGeometry(QtCore.QRect(550, 50, 181, 51))
        self.searchButtonSec.setStyleSheet("background-color:  #01579b;\n"
"                                        border-top: 1px solid #01579b;\n"
"                                        border-bottom: 1px solid #01579b;\n"
"                                        border-left: 1px solid #01579b;\n"
"                                        border-right: 1px solid #01579b;\n"
"                                        color: #ECEFF1;")
        self.searchButtonSec.setObjectName("searchButtonSec")
        self.docNameLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.docNameLabel1.setGeometry(QtCore.QRect(50, 140, 441, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.docNameLabel1.setFont(font)
        self.docNameLabel1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.docNameLabel1.setStyleSheet("color: rgb(0, 8, 132);")
        self.docNameLabel1.setObjectName("docNameLabel1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 120, 501, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 240, 501, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.docNameLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.docNameLabel2.setGeometry(QtCore.QRect(50, 260, 441, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.docNameLabel2.setFont(font)
        self.docNameLabel2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.docNameLabel2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.docNameLabel2.setStyleSheet("color: rgb(0, 8, 132);")
        self.docNameLabel2.setObjectName("docNameLabel2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(550, 130, 181, 121))
        self.widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.radioBooleanSec = QtWidgets.QRadioButton(self.widget)
        self.radioBooleanSec.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.radioBooleanSec.setStyleSheet("color: rgb(0, 8, 132);")
        self.radioBooleanSec.setObjectName("radioBooleanSec")
        self.radioVectorielSec = QtWidgets.QRadioButton(self.widget)
        self.radioVectorielSec.setGeometry(QtCore.QRect(10, 40, 100, 20))
        self.radioVectorielSec.setStyleSheet("color: rgb(0, 8, 132);")
        self.radioVectorielSec.setObjectName("radioVectorielSec")
        self.comboFunctionChoice = QtWidgets.QComboBox(self.widget)
        self.comboFunctionChoice.setGeometry(QtCore.QRect(30, 70, 121, 31))
        self.comboFunctionChoice.setStyleSheet("border-top: 1px solid #ddd;\n"
"border-bottom: 1px solid #ddd;\n"
"border-left: 1px solid #ddd;\n"
"border-right: 1px solid #ddd;\n"
"")
        self.comboFunctionChoice.setObjectName("comboFunctionChoice")
        self.colloctionList = QtWidgets.QListWidget(self.centralwidget)
        self.colloctionList.setGeometry(QtCore.QRect(550, 260, 181, 181))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.colloctionList.setFont(font)
        self.colloctionList.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-top: 1px solid #ddd;\n"
                                            "border-bottom: 1px solid #ddd;\n"
                                            "border-left: 1px solid #ddd;\n"
                                            "border-right: 1px solid #ddd;\n"
                                            "color: rgb(0, 8, 132);")
        self.colloctionList.setObjectName("colloctionList")
        self.evaluateButton = QtWidgets.QPushButton(self.centralwidget)
        self.evaluateButton.setGeometry(QtCore.QRect(550, 540, 181, 51))
        self.evaluateButton.setStyleSheet("background-color:  #01579b;\n"
"                                        border-top: 1px solid #01579b;\n"
"                                        border-bottom: 1px solid #01579b;\n"
"                                        border-left: 1px solid #01579b;\n"
"                                        border-right: 1px solid #01579b;\n"
"                                        color: #ECEFF1;")
        self.evaluateButton.setObjectName("evaluateButton")
        self.evaluationWidget = QtWidgets.QWidget(self.centralwidget)
        self.evaluationWidget.setGeometry(QtCore.QRect(550, 450, 181, 81))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.evaluationWidget.setFont(font)
        self.evaluationWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-top: 1px solid #ddd;\n"
                                            "border-bottom: 1px solid #ddd;\n"
                                            "border-left: 1px solid #ddd;\n"
                                            "border-right: 1px solid #ddd;\n"
                                            "color: rgb(0, 8, 132);")
        self.evaluationWidget.setObjectName("evaluationWidget")
        self.rappelLabel = QtWidgets.QLabel(self.evaluationWidget)
        self.rappelLabel.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.rappelLabel.setFont(font)
        self.rappelLabel.setObjectName("rappelLabel")
        self.precisionLabel = QtWidgets.QLabel(self.evaluationWidget)
        self.precisionLabel.setGeometry(QtCore.QRect(10, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.precisionLabel.setFont(font)
        self.precisionLabel.setObjectName("precisionLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchButtonSec.setText(_translate("MainWindow", "PushButton"))
        self.docNameLabel1.setText(_translate("MainWindow", "TextLabel"))
        self.docNameLabel2.setText(_translate("MainWindow", "TextLabel"))
        self.radioBooleanSec.setText(_translate("MainWindow", "Boolean"))
        self.radioVectorielSec.setText(_translate("MainWindow", "Vectoriel"))
        self.evaluateButton.setText(_translate("MainWindow", "Evaluate"))
        self.rappelLabel.setText(_translate("MainWindow", "TextLabel"))
        self.precisionLabel.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

