#-*-coding: utf-8-*-
# Form implementation generated from reading ui file 'dialogcharts.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDateEdit, QDateTimeEdit
from api_control import currency_list
from api_control import Currency
from datetime import date
from dialogopenchart import Ui_DialogOpenChart
from PyQt6.QtGui import QPixmap

class Ui_DialogCharts(object):
    def setupUi(self, DialogCharts):
        DialogCharts.setObjectName("DialogCharts")
        DialogCharts.resize(400, 300)
        DialogCharts.setMaximumSize(QtCore.QSize(400, 300))
        DialogCharts.setMinimumSize(QtCore.QSize(400, 300))
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=DialogCharts)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 381, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_choice = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_choice.setFont(font)
        self.label_choice.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_choice.setObjectName("label_choice")
        self.horizontalLayout.addWidget(self.label_choice)
        self.combo_choice = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.combo_choice.setFont(font)
        self.combo_choice.setObjectName("combo_choice")
        self.horizontalLayout.addWidget(self.combo_choice)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_start = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_start.setFont(font)
        self.label_start.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_start.setObjectName("label_start")
        self.horizontalLayout_2.addWidget(self.label_start)
        self.label_end = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_end.setFont(font)
        self.label_end.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_end.setObjectName("label_end")
        self.horizontalLayout_2.addWidget(self.label_end)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date_edit_start = QtWidgets.QDateEdit(parent=self.verticalLayoutWidget)
        self.date_edit_start.setObjectName("date_edit_start")
        self.horizontalLayout_3.addWidget(self.date_edit_start)
        self.date_edit_end = QtWidgets.QDateEdit(parent=self.verticalLayoutWidget)
        self.date_edit_end.setObjectName("date_edit_end")
        self.horizontalLayout_3.addWidget(self.date_edit_end)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=DialogCharts)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 210, 381, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_okay = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.button_okay.setObjectName("button_okay")
        self.horizontalLayout_4.addWidget(self.button_okay)
        self.button_back = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.button_back.setObjectName("button_back")
        self.horizontalLayout_4.addWidget(self.button_back)

        self.retranslateUi(DialogCharts)
        QtCore.QMetaObject.connectSlotsByName(DialogCharts)

        #set start
        self.date_edit_end.setDate(date.today())
        #set end one year before
        self.date_edit_start.setDate(date.today().replace(year=date.today().year-1))
        self.date_edit_end.setMinimumDate(self.date_edit_start.date())
        self.date_edit_end.setMaximumDate(date.today())
        self.date_edit_start.setMaximumDate(date.today())
        for i in currency_list:
            self.combo_choice.addItem(i.iso)
        #connect buttons and data change
        self.button_back.clicked.connect(DialogCharts.close)
        self.button_okay.clicked.connect(self.okay_clicked)
        #set min date for end date, year after start date
        self.date_edit_start.dateChanged.connect(self.changed_start)
        #disable date_edit_end


    def retranslateUi(self, DialogCharts):
        _translate = QtCore.QCoreApplication.translate
        DialogCharts.setWindowTitle(_translate("DialogCharts", "Charts"))
        self.label_choice.setText(_translate("DialogCharts", "Select currency:"))
        self.label_start.setText(_translate("DialogCharts", "Select start:"))
        self.label_end.setText(_translate("DialogCharts", "Select end:"))
        self.date_edit_start.setDisplayFormat(_translate("DialogCharts", "yyyy.MM.dd"))
        self.date_edit_end.setDisplayFormat(_translate("DialogCharts", "yyyy.MM.dd"))
        self.button_okay.setText(_translate("DialogCharts", "Okay"))
        self.button_back.setText(_translate("DialogCharts", "Back"))

    def okay_clicked (self):
        #get date as ISO format
        start = self.date_edit_start.date().toString("yyyy-MM-dd")
        end = self.date_edit_end.date().toString("yyyy-MM-dd")
        choice = self.combo_choice.currentText().lower()
        chart_path = Currency.get_chart_data(choice, start, end)
        if chart_path == None:
            self.label_choice.setText("Data not found!")
            return
        else:
            new_dialog = QtWidgets.QDialog()
            new_dialog.ui = Ui_DialogOpenChart()
            new_dialog.ui.setupUi(new_dialog)
            new_dialog.ui.label_picture.setPixmap(QPixmap(chart_path))
            new_dialog.exec()

    def changed_start(self):
        self.date_edit_end.setMinimumDate(self.date_edit_start.date())
        if self.date_edit_start.date().year() == date.today().year or self.date_edit_start.date().year() == date.today().year-1:
            self.date_edit_end.setMaximumDate(date.today())
        else:
            self.date_edit_end.setMaximumDate(self.date_edit_start.date().addYears(1))
            self.date_edit_end.setDate(self.date_edit_start.date().addYears(1))