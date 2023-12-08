#-*-coding: utf-8-*-
# Form implementation generated from reading ui file 'dialogconvert.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from api_control import currency_list
from api_control import Currency
import re


class Ui_DialogConvert(object):
    def setupUi(self, DialogConvert):
        DialogConvert.setObjectName("DialogConvert")
        DialogConvert.resize(400, 300)
        DialogConvert.setMaximumSize(QtCore.QSize(400, 300))
        DialogConvert.setMinimumSize(QtCore.QSize(400, 300))
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=DialogConvert)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 200, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_sell = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.button_sell.setObjectName("button_sell")
        self.horizontalLayout_2.addWidget(self.button_sell)
        self.button_buy = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.button_buy.setObjectName("button_buy")
        self.horizontalLayout_2.addWidget(self.button_buy)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=DialogConvert)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 40, 381, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_1 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_3.addWidget(self.label_1)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=DialogConvert)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 381, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.combo_main = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_3)
        self.combo_main.setObjectName("combo_main")
        self.horizontalLayout_4.addWidget(self.combo_main)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.combo_result = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_3)
        self.combo_result.setObjectName("combo_result")
        self.horizontalLayout_4.addWidget(self.combo_result)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=DialogConvert)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 130, 381, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_main = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_4)
        self.line_main.setMinimumSize(QtCore.QSize(120, 0))
        self.line_main.setMaximumSize(QtCore.QSize(120, 16777215))
        self.line_main.setObjectName("line_main")
        self.line_main.setPlaceholderText("Format 'X.XX' or 'XX'")
        self.horizontalLayout_5.addWidget(self.line_main)
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_result = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.label_result.setMinimumSize(QtCore.QSize(120, 0))
        self.label_result.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_result.setBaseSize(QtCore.QSize(0, 0))
        self.label_result.setObjectName("label_result")
        self.label_result.setFont(font)
        self.horizontalLayout_5.addWidget(self.label_result)
        self.button_back = QtWidgets.QPushButton(parent=DialogConvert)
        self.button_back.setGeometry(QtCore.QRect(300, 260, 80, 18))
        self.button_back.setObjectName("button_back")
        self.label_error = QtWidgets.QLabel(parent=DialogConvert)
        self.label_error.setGeometry(QtCore.QRect(140, 170, 121, 20))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")

        self.retranslateUi(DialogConvert)
        QtCore.QMetaObject.connectSlotsByName(DialogConvert)

        self.combo_result.addItem("PLN")
        for i in currency_list:
            self.combo_result.addItem(i.iso)

        for i in currency_list:
            self.combo_main.addItem(i.iso)
        self.combo_main.addItem("PLN")
    #sort items
        self.combo_main.model().sort(0, QtCore.Qt.SortOrder.AscendingOrder)
        self.combo_result.model().sort(0, QtCore.Qt.SortOrder.AscendingOrder)

        #connect buttons
        self.button_back.clicked.connect(DialogConvert.close)
        self.button_sell.clicked.connect(self.sell_clicked)
        self.button_buy.clicked.connect(self.buy_clicked)

    def retranslateUi(self, DialogConvert):
        _translate = QtCore.QCoreApplication.translate
        DialogConvert.setWindowTitle(_translate("DialogConvert", "Converter"))
        self.button_sell.setText(_translate("DialogConvert", "Sell"))
        self.button_buy.setText(_translate("DialogConvert", "Buy"))
        self.label_1.setText(_translate("DialogConvert", "Currency 1"))
        self.label_2.setText(_translate("DialogConvert", "Currency 2"))
        self.label_3.setText(_translate("DialogConvert", "TO"))
        self.label_result.setText(_translate("DialogConvert", "Result"))
        self.button_back.setText(_translate("DialogConvert", "Back"))

    def sell_clicked(self):
        self.convert(self.combo_main.currentText(), self.combo_result.currentText(), self.line_main.text(), False)

    def buy_clicked(self):
        self.convert(self.combo_main.currentText(), self.combo_result.currentText(), self.line_main.text(), True)

    def convert(self, currency1, currency2, amount, choice):
        if re.search("[0-9]+\.[0-9]+", amount) or re.search("[0-9]+", amount):
            print("success")
            result = Currency.convert_currencies(currency1, currency2, float(amount), choice)
            self.label_result.setText(str(result))
        else:
            self.label_error.setText("Wrong amount format")