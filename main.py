#-*-coding: utf-8-*-
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from mainwindow import Ui_MainWindow
import api_control

class Menu (QtWidgets.QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.formatTable()
        self.ui.button_choose.clicked.connect(self.choose_clicked)
        self.ui.button_exit.clicked.connect(self.close)

    def print_currency(self):
        currency = self.ui.line_currency.text()
        print(api_control.get_one_currency(currency))
        self.ui.line_currency.clear()


    def formatTable(self):
        self.ui.table_data.setColumnCount(4)
        self.ui.table_data.setHorizontalHeaderLabels(["ISO", "Currency", "Sell", "Buy"])
        self.ui.table_data.horizontalHeader().setStretchLastSection(True)
#        self.ui.table_data.horizontalHeader().setSectionResizeMode(QTableWidget.ResizeMode.Stretch)

    def choose_clicked(self):
        currency = api_control.get_one_currency(self.ui.line_currency.text())
        # if currency[0] == 404:
        #     self.actual_price.setText("Error")
        #     return
        #self.actual_price.setText("Succes")
        new_row = self.ui.table_data.rowCount()
        self.ui.table_data.insertRow(new_row)
        self.ui.table_data.setItem(new_row, 0, QTableWidgetItem(currency[1]))
        self.ui.table_data.setItem(new_row, 1, QTableWidgetItem(currency[2]))
        self.ui.table_data.setItem(new_row, 2, QTableWidgetItem(str(currency[3])))
        self.ui.table_data.setItem(new_row, 3, QTableWidgetItem(str(currency[4])))
        self.ui.line_currency.clear()

def main():
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

#self.line_currency.setCompleter(QtWidgets.QCompleter(["usd", "eur", "chf", "gbp", "jpy", "czk", "dkk", "nok", "sek", "xdr"], self.line_currency))