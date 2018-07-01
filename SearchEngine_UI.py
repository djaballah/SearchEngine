# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchEngine_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import boolean_model
import vectoriel_model
import inverted_index
from os import listdir
from os.path import join
import evaluation
import functools

NO_DOCUMENTS_MESSAGE = "No Documents !!!!!!!!!!!!!!!!!"
NO_DOCUMENTS_INFO = "There are no documents that \n responds to your query"
NO_DOCUMENTS_TITLE = "No Results"

SYNTAX_ERR_MESSAGE = "Syntax Error"
SYNTAX_ERR_INFO = "You Request doesn't respect the \n syntax of the boolean query"
SYNTAX_ERR_TITLE = "Sntax Error"

NO_SELECTED_DOC_MESSAGE = "No Pertinent Document Selected"
NO_SELECTED_DOC_INFO = "You did not select any pertinent document from the collection"
NO_SELECTED_DOC_TITLE = "No pertinent document"

EVALUATION_ERR_MESSAGE = "Evaluation just for Vectoriel Model"
EVALUATION_ERR_INFO = "You can only \n evaluate Vectoriel model"
EVALUATION_ERR_TITLE = "Evaluation Error"

collection_path = "/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/collection"


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
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        font.setPointSize(14)
        self.queryText.setFont(font)
        self.queryText.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-top: 1px solid #ddd;\n"
                                    "border-bottom: 1px solid #ddd;\n"
                                    "border-left: 1px solid #ddd;\n"
                                    "border-right: 1px solid #ddd;\n"
                                    "color: rgb(0, 8, 132);")
        self.queryText.setObjectName("queryText")
        self.queryText.setGraphicsEffect(self.shadow)
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
                                        "border-top: 1px solid #01579b;\n"
                                        "border-bottom: 1px solid #01579b;\n"
                                        "border-left: 1px solid #01579b;\n"
                                        "border-right: 1px solid #01579b;\n"
                                        "color: #ECEFF1;")
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(True)
        self.searchButton.setObjectName("searchButton")
        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(15)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.searchButton.setGraphicsEffect(self.shadow2)
        self.searchButton.clicked.connect(self.search)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGraphicsEffect(self.shadow)
        self.widget.setGeometry(QtCore.QRect(560, 290, 201, 131))
        self.widget.setStyleSheet("\n"
                                  "background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.boolean_2 = QtWidgets.QRadioButton(self.widget)
        self.boolean_2.setGeometry(QtCore.QRect(10, 10, 120, 20))
        self.boolean_2.setEnabled(True)
        self.boolean_2.setStyleSheet("color: rgb(0, 8, 132);")
        self.boolean_2.setObjectName("boolean_2")
        self.boolean_2.clicked.connect(self.hideFunction)
        self.vectoriel = QtWidgets.QRadioButton(self.widget)
        self.vectoriel.setEnabled(True)
        self.vectoriel.setChecked(True)
        self.vectoriel.setGeometry(QtCore.QRect(10, 40, 120, 20))
        self.vectoriel.setStyleSheet("color: rgb(0, 8, 132);")
        self.vectoriel.setIconSize(QtCore.QSize(16, 16))
        self.vectoriel.setCheckable(True)
        self.vectoriel.setObjectName("vectoriel")
        self.vectoriel.clicked.connect(self.displayFunction)
        self.vectorielFunction = QtWidgets.QComboBox(self.widget)
        self.vectorielFunction.setGeometry(QtCore.QRect(10, 70, 140, 35))
        self.vectorielFunction.setStyleSheet("color: rgb(0, 8, 132);")
        vecFunctions = ['Inner Product',
                        'Dice Coefficient',
                        'Cosinus Measure',
                        'Jackard Measure']
        self.vectorielFunction.addItems(vecFunctions)

        ###
        self.updateIndexBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateIndexBtn.setGeometry(QtCore.QRect(560, 440, 201, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.updateIndexBtn.setFont(font)
        self.updateIndexBtn.setStyleSheet("background-color:  #01579b;\n"
                                        "border-top: 1px solid #01579b;\n"
                                        "border-bottom: 1px solid #01579b;\n"
                                        "border-left: 1px solid #01579b;\n"
                                        "border-right: 1px solid #01579b;\n"
                                        "color: #ECEFF1;")
        self.updateIndexBtn.setDefault(False)
        self.updateIndexBtn.setFlat(True)
        self.updateIndexBtn.setObjectName("updateIndexBtn")
        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(15)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.updateIndexBtn.setGraphicsEffect(self.shadow2)
        self.updateIndexBtn.setText("Update Index")
        self.updateIndexBtn.clicked.connect(self.update_index)

        ##
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.freqWeightWisget = QtWidgets.QWidget(self.centralwidget)
        self.freqWeightWisget.setGraphicsEffect(self.shadow)
        self.freqWeightWisget.setGeometry(QtCore.QRect(60, 290, 481, 131))
        self.freqWeightWisget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.freqWeightWisget.setObjectName("freqWeightWisget")
        self.termEdit = QtWidgets.QLineEdit(self.freqWeightWisget)
        self.termEdit.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.termEdit.setObjectName("termEdit")
        self.documentEdit = QtWidgets.QLineEdit(self.freqWeightWisget)
        self.documentEdit.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.documentEdit.setObjectName("documentEdit")
        self.resultWidget = QtWidgets.QWidget(self.freqWeightWisget)
        self.resultWidget.setGeometry(QtCore.QRect(210, 10, 261, 111))
        self.resultWidget.setObjectName("resultWidget")
        self.resultWidget.setStyleSheet("QWidget#resultWidget{border-top: 1px solid #01579b;\n"
                                        "border-bottom: 1px solid #01579b;\n"
                                        "border-left: 1px solid #01579b;\n"
                                        "border-right: 1px solid #01579b;}")

        self.freqLabel = QtWidgets.QLabel(self.resultWidget)
        self.freqLabel.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.freqLabel.setObjectName("freqLabel")
        self.freqLabel.setStyleSheet("QWidget#freqLabel{border-top: 1px solid #01579b;\n"
                                        "border-bottom: 1px solid #01579b;\n"
                                        "border-left: 1px solid #01579b;\n"
                                        "border-right: 1px solid #01579b;}")
        self.freqLabel.setText("Frequence")
        self.weightLabel = QtWidgets.QLabel(self.resultWidget)
        self.weightLabel.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.weightLabel.setObjectName("weightLabel")
        self.weightLabel.setStyleSheet("QWidget#weightLabel{border-top: 1px solid #01579b;\n"
                                        "border-bottom: 1px solid #01579b;\n"
                                        "border-left: 1px solid #01579b;\n"
                                        "border-right: 1px solid #01579b;}")
        self.weightLabel.setText("Weight")
        self.calculatButton = QtWidgets.QPushButton(self.resultWidget)
        self.calculatButton.setGeometry(QtCore.QRect(150, 70, 101, 31))
        self.calculatButton.setObjectName("calculatButton")
        self.calculatButton.setStyleSheet("background-color:  #01579b;\n"
                                        "color: #ECEFF1;")
        self.calculatButton.setText("Calculate")
        self.calculatButton.clicked.connect(self.getFreAndWeight)
        self.termLabel = QtWidgets.QLabel(self.freqWeightWisget)
        self.termLabel.setGeometry(QtCore.QRect(10, 10, 59, 14))
        self.termLabel.setObjectName("termLabel")
        self.termLabel.setText("Term")
        self.documentLabel = QtWidgets.QLabel(self.freqWeightWisget)
        self.documentLabel.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.documentLabel.setObjectName("documentLabel")
        self.documentLabel.setText("Document")

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

    def search(self):
        """
        Execute a search using the query
        :return: list of documents
        """

        retrived = None
        try:
            query = self.queryText.text()
            boolean = self.boolean_2.isChecked()
            response = None
            model = None
            if (boolean):
                response = boolean_model.respond_to_query(query)
                model = 'boolean'
                print('Boolean')
            else:
                print('Vectoriel')
                model = 'vectoriel'
                measureFunction = self.vectorielFunction.currentText()
                response = vectoriel_model.respond_to_query(query, measureFunction)
                retrived = [item[0] for item in response]
                print(measureFunction, " is being used")
                response = [item[0] + "  :" + "%.2f" % item[1] for item in response]

            print(response)
            if (len(response) == 0):
                self.popup(NO_DOCUMENTS_MESSAGE, NO_DOCUMENTS_INFO, NO_DOCUMENTS_TITLE)
            else:
                # self.centralwidget.hide()
                self.show_secondary(MainWindow)
                self.display_response(response)
                self.displayCollection("/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/collection")
                self.retrieved_doc = retrived
                self.model_used = model
        except SyntaxError:
            self.popup(SYNTAX_ERR_MESSAGE, SYNTAX_ERR_INFO, SYNTAX_ERR_TITLE)

    def searchSec(self):
        """
        Execute a search using the query
        :return: list of documents
        """
        retrived = None
        try:
            query = self.queryTextSec.text()
            boolean = self.radioBooleanSec.isChecked()
            response = None
            model = None
            if (boolean):
                response = boolean_model.respond_to_query(query)
                print('Boolean')
                model = 'boolean'
            else:
                print('Vectoriel')
                model = 'vectoriel'
                measureFunction = self.comboFunctionChoice.currentText()
                response = vectoriel_model.respond_to_query(query, measureFunction)
                print(measureFunction, " is being used")
                retrived = [item[0] for item in response]
                response = [item[0] + "  :" + "%.2f" % item[1] for item in response]
                print(len(response))
            if (len(response) == 0):
                for lab in self.labels:
                    lab.hide()
                for line in self.lines:
                    line.hide()
                self.lines = []
                self.labels = []
                self.retrieved_doc = []
                self.popup(NO_DOCUMENTS_MESSAGE, NO_DOCUMENTS_INFO, NO_DOCUMENTS_TITLE)
            else:
                # self.centralwidget.hide()
                #self.show_secondary(MainWindow)
                for lab in self.labels:
                    lab.hide()
                for line in self.lines:
                    line.hide()
                self.lines = []
                self.labels = []
                self.display_response(response)
                self.retrieved_doc = retrived
                self.model_used = model
        except SyntaxError:
            self.popup(SYNTAX_ERR_MESSAGE, SYNTAX_ERR_INFO, SYNTAX_ERR_TITLE)


    def getFreAndWeight(self):
        try:
            doc = self.documentEdit.text()
            term = self.termEdit.text()

            freq = inverted_index.frequence(term, doc + ".txt")
            weight = inverted_index.weight(term, doc + ".txt")
            self.freqLabel.setText('Frequence ' + str(freq))
            self.weightLabel.setText('Weight %.2f' % weight)
        except FileNotFoundError:
            self.popup("No document found", "There is no document in the collectin with that name",
                       "No document Found")


    def popup(self, error_message, error_info, error_title):
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setFont(font)
        msg.setStyleSheet("background-color:  #E1E2E1;\n"
                          "color: rgb(0, 8, 132);\n")

        msg.setText(error_message)
        msg.setInformativeText(error_info)
        msg.setWindowTitle(error_title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()


    def hideFunction(self):
        self.vectorielFunction.hide()

    def displayFunction(self):
        self.vectorielFunction.setVisible(True)

    def hideFunctionSec(self):
        self.comboFunctionChoice.hide()
        #self.evaluateButton.setDisabled(True)

    def displayFunctionSec(self):
        self.comboFunctionChoice.setVisible(True)
        #self.evaluateButton.setDisabled(False)

    def show_secondary(self, MainWindow):
        last_query = ""
        self.model_used = None
        try:
            last_query = self.queryText.text()
        except RuntimeError:
            pass
        self.retrieved_doc = []
        self.collectionItems = []
        self.secondwidget = QtWidgets.QWidget(MainWindow)
        self.secondwidget.setObjectName("secondwidget")
        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(15)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.queryTextSec = QtWidgets.QLineEdit(self.secondwidget)
        self.queryTextSec.setGraphicsEffect(self.shadow2)
        self.queryTextSec.setGeometry(QtCore.QRect(30, 30, 481, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.queryTextSec.setFont(font)
        self.queryTextSec.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-top: 1px solid #ddd;\n"
                                        "border-bottom: 1px solid #ddd;\n"
                                        "border-left: 1px solid #ddd;\n"
                                        "border-right: 1px solid #ddd;\n"
                                        "color: rgb(0, 8, 132);")
        self.queryTextSec.setObjectName("queryTextSec")
        self.queryTextSec.setText(last_query)
        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(15)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.searchButtonSec = QtWidgets.QPushButton(self.secondwidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.searchButtonSec.setFont(font)
        self.searchButtonSec.setGraphicsEffect(self.shadow)
        self.searchButtonSec.setGeometry(QtCore.QRect(550, 30, 181, 51))
        self.searchButtonSec.setStyleSheet("background-color:  #01579b;\n"
                                           "border-top: 1px solid #01579b;\n"
                                           "border-bottom: 1px solid #01579b;\n"
                                           "border-left: 1px solid #01579b;\n"
                                           "border-right: 1px solid #01579b;\n"
                                           "color: #ECEFF1;")
        self.searchButtonSec.setObjectName("searchButtonSec")
        self.searchButtonSec.clicked.connect(self.searchSec)
        #self.docNameLabel1 = QtWidgets.QLabel(self.secondwidget)
        #self.docNameLabel1.setGeometry(QtCore.QRect(50, 140, 441, 51))
        #font = QtGui.QFont()
        #font.setFamily("DejaVu Serif")
        #font.setPointSize(18)
        #self.docNameLabel1.setFont(font)
        #self.docNameLabel1.setFocusPolicy(QtCore.Qt.NoFocus)
        #self.docNameLabel1.setStyleSheet("color: rgb(0, 8, 132);")
        #self.docNameLabel1.setObjectName("docNameLabel1")
        self.lines = []
        #self.line = QtWidgets.QFrame(self.secondwidget)
        #self.line.setGeometry(QtCore.QRect(30, 120, 480, 20))
        #font = QtGui.QFont()
        #font.setBold(False)
        #font.setWeight(50)
        #self.line.setFont(font)
        #self.line.setFrameShape(QtWidgets.QFrame.HLine)
        #self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.line.setObjectName("line")
        #self.line_2 = QtWidgets.QFrame(self.secondwidget)
        #self.line_2.setGeometry(QtCore.QRect(30, 240, 480, 20))
        #font = QtGui.QFont()
        #font.setBold(False)
        #font.setWeight(50)
        #self.line_2.setFont(font)
        #self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        #self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.line_2.setObjectName("line_2")
        #self.docNameLabel2 = QtWidgets.QLabel(self.secondwidget)
        #self.docNameLabel2.setGeometry(QtCore.QRect(50, 260, 441, 51))
        #font = QtGui.QFont()
        #font.setFamily("DejaVu Serif")
        #font.setPointSize(18)
        #self.docNameLabel2.setFont(font)
        #self.docNameLabel2.setFocusPolicy(QtCore.Qt.NoFocus)
        #self.docNameLabel2.setStyleSheet("color: rgb(0, 8, 132);")
        #self.docNameLabel2.setObjectName("docNameLabel2")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.widget = QtWidgets.QWidget(self.secondwidget)
        self.widget.setGraphicsEffect(self.shadow)
        self.widget.setGeometry(QtCore.QRect(550, 100, 181, 121))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          )
        self.widget.setObjectName("widget")
        self.radioBooleanSec = QtWidgets.QRadioButton(self.widget)
        self.radioBooleanSec.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.radioBooleanSec.setStyleSheet("color: rgb(0, 8, 132);")
        self.radioBooleanSec.setObjectName("radioBooleanSec")
        self.radioBooleanSec.setText("Boolean")
        self.radioBooleanSec.clicked.connect(self.hideFunctionSec)
        self.radioVectorielSec = QtWidgets.QRadioButton(self.widget)
        self.radioVectorielSec.setGeometry(QtCore.QRect(10, 40, 100, 20))
        self.radioVectorielSec.setStyleSheet("color: rgb(0, 8, 132);")
        self.radioVectorielSec.setObjectName("radioVectorielSec")
        self.radioVectorielSec.setText("Vectoriel")
        self.radioVectorielSec.setChecked(True)
        self.radioVectorielSec.clicked.connect(self.displayFunctionSec)
        self.comboFunctionChoice = QtWidgets.QComboBox(self.widget)
        self.comboFunctionChoice.setGeometry(QtCore.QRect(10, 70, 140, 35))
        self.comboFunctionChoice.setStyleSheet("color: rgb(0, 8, 132);")
        self.comboFunctionChoice.setObjectName("comboFunctionChoice")
        vecFunctions = ['Inner Product',
                        'Dice Coefficient',
                        'Cosinus Measure',
                        'Jackard Measure']
        self.comboFunctionChoice.addItems(vecFunctions)
        self.labels = []

        #To Test
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.colloctionList = QtWidgets.QListWidget(self.secondwidget)
        self.colloctionList.setGraphicsEffect(self.shadow)
        self.colloctionList.setGeometry(QtCore.QRect(550, 240, 181, 185))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.colloctionList.setFont(font)
        self.colloctionList.setStyleSheet("background-color: rgb(255, 255, 255);\n"

                                          "color: rgb(0, 8, 132);")
        self.colloctionList.setObjectName("colloctionList")
        self.colloctionList.setSpacing(2)

        #
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.evaluateButton = QtWidgets.QPushButton(self.secondwidget)
        self.evaluateButton.setFont(font)
        self.evaluateButton.setGraphicsEffect(self.shadow)
        self.evaluateButton.setGeometry(QtCore.QRect(550, 440, 181, 51))
        self.evaluateButton.setStyleSheet("background-color:  #01579b;\n"
                                           "border-top: 1px solid #01579b;\n"
                                           "border-bottom: 1px solid #01579b;\n"
                                           "border-left: 1px solid #01579b;\n"
                                           "border-right: 1px solid #01579b;\n"
                                           "color: #ECEFF1;")
        self.evaluateButton.setObjectName("evaluateButton")
        self.evaluateButton.setText("Evaluate")
        self.evaluateButton.clicked.connect(self.evaluate)
        #
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.evaluationWidget = QtWidgets.QWidget(self.secondwidget)
        self.evaluationWidget.setGraphicsEffect(self.shadow)
        self.evaluationWidget.setGeometry(QtCore.QRect(550, 500, 181, 70))
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
        self.rappelLabel.setStyleSheet("border: none;")
        self.precisionLabel = QtWidgets.QLabel(self.evaluationWidget)
        self.precisionLabel.setGeometry(QtCore.QRect(10, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.precisionLabel.setFont(font)
        self.precisionLabel.setObjectName("precisionLabel")
        self.precisionLabel.setStyleSheet("border: none;")

        ###Response

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.responseWidget = QtWidgets.QWidget(self.secondwidget)
        #self.responseWidget.setGraphicsEffect(self.shadow)
        self.responseWidget.setGeometry(QtCore.QRect(30, 100, 460, 391))
        self.responseWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  
                                          "color: rgb(0, 8, 132);")
        self.responseWidget.setObjectName("responseWidget")

        ##
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.scroll = QtWidgets.QScrollArea(self.secondwidget)
        self.scroll.setGraphicsEffect(self.shadow)
        self.scroll.setWidget(self.responseWidget)
        self.scroll.setGeometry(QtCore.QRect(30, 100, 481, 391))
        self.scroll.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-top: 1px solid #ddd;\n"
                                          "border-bottom: 1px solid #ddd;\n"
                                          "border-left: 1px solid #ddd;\n"
                                          "border-right: 1px solid #ddd;\n"
                                          "color: rgb(0, 8, 132);")
        MainWindow.setCentralWidget(self.secondwidget)
        _translate = QtCore.QCoreApplication.translate
        self.searchButtonSec.setText(_translate("MainWindow", "Search"))
        #self.docNameLabel1.setText(_translate("MainWindow", "TextLabel"))
        #self.docNameLabel2.setText(_translate("MainWindow", "TextLabel"))

    def display_response(self, doc_list):
        """
        Display documents responding to the query
        :param doc_list: List of document coresponding to the query
        :type: list
        """
        #y = 110
        #y2 = 90
        y = 10
        y2 = -10
        #self.labels.append(self.create_label(y, "djaballah"))
        #self.labels.append(self.create_label(y, "djaballah"))
        assert isinstance(doc_list, list)
        self.responseWidget.setGeometry(QtCore.QRect(30, 100, 460, 391))
        for doc in doc_list:
            lab = self.create_label(y, doc)
            line = self.createLine(y2)
            self.lines.append(line)
            self.labels.append(lab)
            y += 99
            y2 += 99
        if ( y > 391):
            self.responseWidget.setGeometry(QtCore.QRect(30, 100, 460, 391 + (y - 391)))

        if ( y < 391):
            self.responseWidget.setGeometry(QtCore.QRect(30, 100, 460, 391 - (391 - y)))
        for lab in self.labels:
            lab.setVisible(True)
        for line in self.lines:
            line.setVisible(True)

    def create_label(self, y, name):
        """
        Return a label object
        :param y: the y cordinate of the labem
        :type: int
        :param name: name of the Object label
        :type: str
        :return: label object
        :type: Qlabel
        """
        #label = QtWidgets.QLabel(self.secondwidget)
        #label.setGeometry(QtCore.QRect(50, y, 441, 51))
        label = QtWidgets.QLabel(self.responseWidget)
        label.setGeometry(QtCore.QRect(20, y, 400, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        label.setFont(font)
        label.setFocusPolicy(QtCore.Qt.NoFocus)
        label.setStyleSheet("color: rgb(0, 8, 132);\n"
                            "border: none;")
        label.setObjectName(name)
        _translate = QtCore.QCoreApplication.translate
        label.setText(_translate("MainWindow", name))
        label.mousePressEvent = functools.partial(self.openDocument, source_object=label)
        label.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        return label

    def openDocument(self, event, source_object=None):
        print("djaballah :", source_object.text())
        import subprocess
        filte_path = join(collection_path, source_object.text().split(':')[0].strip())
        proc = subprocess.Popen(['gedit', filte_path])

    def createLine(self, y):
        """
        Create a line in the window
        :param y: The y cordinate of the line
        :type: int
        :return: QtWidgets.QFrame
        """
        #line = QtWidgets.QFrame(self.secondwidget)
        #line.setGeometry(QtCore.QRect(30, y, 480, 20))
        line = QtWidgets.QFrame(self.responseWidget)
        #line.setStyleSheet("border: none;")
        line.setGeometry(QtCore.QRect(0, y, 480, 2))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        line.setFont(font)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line" + str(y))
        return line

    def displayCollection(self, path_to_collection):
        """
        Display The collection's documents in the listWidget
        :param path_to_collection: Path to the collection's directory
        :type: str
        """
        document_list = listdir(path_to_collection)
        for doc in document_list:
            item = QtWidgets.QListWidgetItem(self.colloctionList)
            item.setText(doc)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.collectionItems.append(item)

    def evaluate(self):

        if self.model_used != 'vectoriel':
            self.popup(EVALUATION_ERR_MESSAGE, EVALUATION_ERR_INFO, EVALUATION_ERR_TITLE)
            self.rappelLabel.setText("Rappel :" + "-")
            self.precisionLabel.setText("Precision :" + "-")
            return

        retrived_documents = self.retrieved_doc
        pertinent_documents = [item.text() for item in self.collectionItems if item.checkState()]

        nb_pertinent_retrived_docu = evaluation.nb_pertinent_retrived_doc(retrived_documents,
                                                                          pertinent_documents)

        rappel = precision = None
        try:
            rappel = evaluation.rappel(nb_pertinent_retrived_docu, len(pertinent_documents))
        except ZeroDivisionError:
            self.popup(NO_SELECTED_DOC_MESSAGE, NO_SELECTED_DOC_INFO, NO_SELECTED_DOC_TITLE)
            self.rappelLabel.setText("Rappel :" + "-" )
            self.precisionLabel.setText("Precision :" + "-")
        try:
            precision = evaluation.precision(nb_pertinent_retrived_docu, len(retrived_documents))
        except:
            self.popup(NO_DOCUMENTS_MESSAGE, NO_DOCUMENTS_INFO, NO_DOCUMENTS_TITLE)
            self.rappelLabel.setText("Rappel :" + "-")
            self.precisionLabel.setText("Precision :" + "-")

        if rappel != None and precision != None:
            self.rappelLabel.setText("Rappel :" + "%.2f" % rappel)
            self.precisionLabel.setText("Precision :" + "%.2f" % precision)


    def update_index(self):

        import document
        import inverted_index
        from os import listdir
        from os.path import join

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(),
                                                            "QtWidgets.QFileDialog.getOpenFileName()", "",
                                                            "Text Files (*.txt);;",
                                                            options=options)
        data = None
        with open(fileName, "r", encoding="utf-8") as fp:
            data = fp.read()
            print(data)
        fileName = fileName.split('/')[-1]
        collection_path = "/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/collection"
        collection = [f for f in listdir(collection_path)]

        if fileName not in collection:
            with open(join(collection_path, fileName), "w") as fp:
                fp.write(data)
        collection = [f for f in listdir(collection_path)]
        for document_name in collection:
            print(document_name)
            doc = document.Document(join(collection_path, document_name))
            inverted_index.construct_index(doc)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

