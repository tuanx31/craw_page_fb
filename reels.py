# Form implementation generated from reading ui file 'reels.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt6.QtWidgets import QTextEdit,QLineEdit

from PyQt6 import QtCore, QtGui, QtWidgets


class Reels(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 300)
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 450, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0,300)
        self.tableWidget.setColumnWidth(1,120)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "link"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "view"))
    def setthuoctinh(self,sss):
        
        with open(sss+'reels.txt',mode='r',encoding='utf8') as f:
            str = f.readlines()
            self.tableWidget.setRowCount(len(str))
            for i in range(len(str)):
                self.tableWidget.setRowHeight(i,50)
                inff= str[i].split('|')
                self.link = QTextEdit()
                self.tableWidget.setCellWidget(i,0,self.link)
                self.link.setText(inff[0])
                self.title = QTextEdit()
                self.tableWidget.setCellWidget(i,1,self.title)
                self.title.setText(inff[1])

