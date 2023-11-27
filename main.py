#-*-coding: utf-8-*-
import sys
import api_control
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCompleter,
    QTableWidget
)


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')
        self.setGeometry(100, 100, 320, 210)
        currency_list = ['usd', 'eur', 'czk', 'aud', 'huf', 'chf']
        common_currencies = QCompleter(currency_list)


        #set grid
        main_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()

        self.setLayout(main_layout)

        #set widgets
        self.actual_price = QLabel()
        self.chosen_curr = QLineEdit(self)
        self.chosen_curr.setMaxLength(3)
        self.chosen_curr.setCompleter(common_currencies)
        self.chosen_curr.setPlaceholderText("Enter currency")
        pb_exit = QPushButton("Exit")
        pb_choose = QPushButton("Choose")

        #set table
        self.tab_currency = QTableWidget(self)
        self.tab_currency.setColumnCount(4)
        self.tab_currency.setHorizontalHeaderLabels(["ISO", "Currency", "Sell", "Buy"])

        #add objects
        main_layout.addWidget(self.chosen_curr)
        main_layout.addWidget(self.actual_price)
        main_layout.addWidget(self.tab_currency)
        buttons_layout.addWidget(pb_choose)
        buttons_layout.addWidget(pb_exit)
        main_layout.addLayout(buttons_layout)
        #create signals
        pb_exit.clicked.connect(MainWindow.exit_clicked)
        pb_choose.clicked.connect(self.choose_clicked)
        self.show()

    def choose_clicked(self):
        currency = api_control.get_one_currency(self.chosen_curr.text())
        if currency[0] == 404:
            self.actual_price.setText("Error")
            return
        else:
            self.actual_price.setText("Succes")



    def exit_clicked():
        sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window and display it
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())


    def delete(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Warning', 'Please select a record to delete')

        button = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure that you want to delete the selected row?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)