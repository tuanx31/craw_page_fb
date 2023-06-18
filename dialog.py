
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTextEdit,QLineEdit


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 500)
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1500, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.setColumnWidth(0,600)
        self.tableWidget.setColumnWidth(1,480)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,100)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "link video"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "thời gian đăng"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "lượt like"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "view"))
    def setthuoctinh(self,sss):
        
        with open('crawlvideo/'+sss+'video.txt',mode='r',encoding='utf8') as f:
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
                self.time = QLineEdit()
                self.tableWidget.setCellWidget(i,2,self.time)
                self.time.setText(inff[3])
                self.soluonglike = QLineEdit()
                self.tableWidget.setCellWidget(i,3,self.soluonglike)
                self.soluonglike.setText(inff[2])
                self.tongview = QLineEdit()
                self.tableWidget.setCellWidget(i,4,self.tongview)
                self.tongview.setText(inff[4])
