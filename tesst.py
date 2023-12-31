from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QPushButton
import os

class Cauhinh(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(155, 218)
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 191, 211))
        self.tableWidget.setStyleSheet("background-color:rgb(43, 43, 43);color:rgb(255, 255, 255);\n"
"    QHeaderView::section {\n"
"        background-color: rgb(43, 43, 43);\n"
"        color: white;\n"
"    }\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.tableWidget.horizontalHeader().setStyleSheet("""
    QHeaderView::section {
        background-color: rgb(43, 43, 43);
        color: white;
    }
""")
        vertical_header = self.tableWidget.verticalHeader()

        # Tùy chỉnh giao diện của header của cột dọc
        vertical_header.setStyleSheet("""
    QHeaderView::section {
        background-color: rgb(43, 43, 43);
        color: white;
    };background-color: rgb(43, 43, 43);
        color: white;
""")
        self.tableWidget.setColumnWidth(0, 150)
        self.list_files = []

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "chọn cấu hình"))
        self.setthuoctinh()

    def setthuoctinh(self):
        allfiles = os.listdir('cauhinh')
        self.list_files = [fname for fname in allfiles if fname.endswith('.txt')]
        row = len(self.list_files)
        print(row)
        self.tableWidget.setRowCount(row)
        
        def handleButtonClick(row):
            print(f"Button clicked in row: {row}")
            caw.loadcauhinh(str(row))
        
        for i in range(row):
            self.chon = QPushButton()
            self.tableWidget.setCellWidget(i, 0, self.chon)
            self.chon.setText(self.list_files[i])
            self.chon.clicked.connect(lambda _, row=i: handleButtonClick(row))
