import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui',self)
        self.con = sqlite3.connect("coffee.db")
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM coffee2""").fetchall()        
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()        
 

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())