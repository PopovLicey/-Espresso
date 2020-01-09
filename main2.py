import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QInputDialog

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui',self)
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
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton.clicked.connect(self.add_elem)
        self.titles = [description[0] for description in cur.description]
        self.modified = {}
        self.p = i + 1
        
    def add_elem(self):
        if True:
            cur = self.con.cursor()
            self.id_ = QInputDialog.getText(self, "Введите id",
                                     "id")[0] 
            self.a = QInputDialog.getText(self, "Введите название марки",
                                     "Название марки")[0]
            self.s = QInputDialog.getText(self, "Введите название сорта",
                                     "Название сорта")[0]
            self.d = QInputDialog.getText(self, "Введите степень обжарки",
                                     "Степень обжарки")[0]
            self.f = QInputDialog.getText(self, "Молотый или в зёрнах",
                                     "Молотый или в зёрнах")[0]
            self.g = QInputDialog.getText(self, "Введите описание вкуса",
                                     "Описание вкуса")[0]
            self.h = QInputDialog.getText(self, "Цена",
                                     "Цена")[0]
            self.j = QInputDialog.getText(self, "Введите объём",
                                     "Объём")[0]
            wer = [self.id_, self.a, self.s, self.d, self.f, self.g, self.h, self.j]
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for i in range(len(wer)):
                self.tableWidget.setItem(self.p, i, QTableWidgetItem(wer[i]))
            self.p += 1
            self.tableWidget.resizeColumnsToContents()
            self.con.commit()
        
    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()    
 

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())