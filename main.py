import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super(Coffee, self).__init__()
        uic.loadUi("main.ui", self)

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()

        self.coffee_table.setColumnCount(7)
        self.coffee_table.setRowCount(0)
        headers = [x[1] for x in cur.execute("""PRAGMA table_info("coffee")""").fetchall()]
        self.coffee_table.setHorizontalHeaderLabels(headers)
        self.coffee_table.verticalHeader().hide()

        for i, row in enumerate(data):
            self.coffee_table.setRowCount(self.coffee_table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.coffee_table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
