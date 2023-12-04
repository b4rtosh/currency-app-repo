#-*-coding: utf-8-*-
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QDialog
from PyQt6.QtCore import Qt
from mainwindow import Ui_MainWindow
from api_control import Currency
from api_control import currency_list
from dialogconvert import Ui_DialogConvert
from dialogcharts import Ui_DialogCharts

class Menu (QtWidgets.QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.formatTable()
        self.add_currency("usd")
        self.add_currency("eur")
        self.add_currency("gbp")
        self.ui.button_choose.clicked.connect(self.choose_clicked) #connecting buttons
        self.ui.button_exit.clicked.connect(self.close)
        self.ui.button_convert.clicked.connect(self.convert_clicked)
        self.ui.button_charts.clicked.connect(self.charts_clicked)


    def formatTable(self):
        self.ui.table_data.setColumnCount(4)
        #set fixed width
        self.ui.table_data.setColumnWidth(0, 100)
        self.ui.table_data.setColumnWidth(1, 225)
        self.ui.table_data.setColumnWidth(2, 100)
        self.ui.table_data.setColumnWidth(3, 100)
        self.ui.table_data.setHorizontalHeaderLabels(["ISO", "Currency", "Sell", "Buy"])


    def add_currency(self, iso):
        if len(iso) != 3:
            self.ui.line_currency.clear()
            self.ui.label_status.setText("Wrong currency format!")
            return
        for i in range(self.ui.table_data.rowCount()):
            if self.ui.table_data.item(i, 0).text() == iso.upper():
                self.ui.line_currency.clear()
                return
        currency = Currency.get_one_currency(iso)
        if currency.status == 404:
            self.ui.line_currency.clear()
            self.ui.label_status.setText("Data not found!")
            return
        elif currency.status == 400:
            self.ui.line_currency.clear()
            self.ui.label_status.setText("Wrong currency!")
            return
        new_row = self.ui.table_data.rowCount()
        self.ui.table_data.insertRow(new_row)
        self.ui.table_data.setItem(new_row, 0, QTableWidgetItem(currency.iso))
        self.ui.table_data.setItem(new_row, 1, QTableWidgetItem(currency.name))
        self.ui.table_data.setItem(new_row, 2, QTableWidgetItem(str(currency.sell)))
        self.ui.table_data.setItem(new_row, 3, QTableWidgetItem(str(currency.buy)))
        self.ui.line_currency.clear()

    def convert_clicked(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_DialogConvert()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        dialog.exec()


    def choose_clicked(self):
        self.add_currency(self.ui.line_currency.text())

    def charts_clicked(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_DialogCharts()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        dialog.exec()

def main():
    Currency.get_all_currencies()
    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())

main()


    #
    # def delete(self):
    #     current_row = self.table.currentRow()
    #     if current_row < 0:
    #         return QMessageBox.warning(self, 'Warning', 'Please select a record to delete')
    #
    #     button = QMessageBox.question(
    #         self,
    #         'Confirmation',
    #         'Are you sure that you want to delete the selected row?',
    #         QMessageBox.StandardButton.Yes |
    #         QMessageBox.StandardButton.No
    #     )
    #     if button == QMessageBox.StandardButton.Yes:
    #         self.table.removeRow(current_row)

