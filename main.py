from PyQt6.QtCore import QObject
from PyQt6 import QtCore , QtGui,QtWidgets,uic
from PyQt6.QtWidgets import QApplication , QMainWindow,QLineEdit,QPushButton,QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dialog import *
import MySQLdb
def convert_views_to_number(views_str):
    views_str = views_str.replace(" views", "")  # Loại bỏ " views" từ chuỗi
    if "K" in views_str:
        views_str = views_str.replace("K", "")
        views = float(views_str) * 1000
    else:
        views = int(views_str)
    return int(views)
ban = 0
user = "MinhKinh"
try:
    mydb = MySQLdb.connect('103.97.126.28','deuszjyg_d-t-dowloader','123456','deuszjyg_d-t-dowloader')

    query = mydb.cursor()
    query.execute("SELECT * FROM `craw` WHERE `user` LIKE 'MinhKinh'")
    kt = query.fetchone()

    ban = kt[1]
except:
    pass
print(ban)

HEIGHT = 526
WIDTH = 1040

solink = 0

class Crawdata(QMainWindow):
    def __init__(self):
        
        super(Crawdata,self).__init__()
        uic.loadUi('crawdata.ui',self)
        self.tableWidget.setColumnWidth(0,250)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,110)
        self.tableWidget.setColumnWidth(3,110)
        self.tableWidget.setColumnWidth(4,110)
        self.tableWidget.setColumnWidth(5,110)
        self.list_link = []
        self.thread = {}
        self.start.clicked.connect(self.startt)
        self.stop.clicked.connect(lambda : self.opendialog())
        self.current_row = 0
    def opendialog(self):
        button = self.sender()
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                cell_widget = self.tableWidget.cellWidget(row, col)
                if cell_widget == button:
                    self.current_row = row
                    break
        print(self.current_row)
        self.window = QtWidgets.QDialog()
        ui.setupUi(self.window)
        self.window.show()  
        ui.setthuoctinh(str(self.current_row))
    def setthuoctinh(self,l):
        global solink
        self.tableWidget.setRowCount(solink+1)
        lst = l.split('|')
        self.link = QLineEdit()
        self.tableWidget.setCellWidget(solink,0,self.link)
        self.link.setText(lst[0])
        
        self.quocgia = QLineEdit()
        self.tableWidget.setCellWidget(solink,1,self.quocgia)
        self.quocgia.setText(lst[1])


        self.fle = QLineEdit()
        self.tableWidget.setCellWidget(solink,2,self.fle)
        self.fle.setText(lst[2])

        self.soluong = QLineEdit()
        self.tableWidget.setCellWidget(solink,3,self.soluong)
        self.soluong.setText(lst[3])

        self.tongview = QLineEdit()
        self.tableWidget.setCellWidget(solink,4,self.tongview)
        self.tongview.setText(lst[4])
        self.xem = QPushButton()

        self.tableWidget.setCellWidget(solink,5,self.xem)
        self.xem.setText("xem thông tin vdeo")
        self.xem.clicked.connect(lambda : self.opendialog())
        solink+=1
    def setlist(self):
        links = self.textcraw.toPlainText()
        self.list_link = links.split('\n')
    def startt(self):
        if ban !=0:
            QMessageBox.information(self,"thong bao ", "bạn đã bị ban ")
        else:
            self.setlist()
            thr = ThreadClass(parent=None,index=1)
            thr.setlistlink(self.list_link)
            self.thread[1]= thr
            self.thread[1].start()
            self.thread[1].signal.connect(self.thongbao)
            self.thread[1].siganal.connect(self.setthuoctinh)

            self.start.setDisabled(True)
            self.stop.setEnabled(True)
    def thongbao(self,u):
        self.label_2.setText(u)
    def stopp(self):
        self.thread[1].stop()
        self.start.setEnabled(True)
        self.stop.setDisabled(True)
    def closeEvent(self, event):
        # Gửi tín hiệu yêu cầu kết thúc luồng
        self.thread[1].stop()
        event.accept()





class ThreadClass(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    siganal = QtCore.pyqtSignal(str)



    def __init__(self, parent=None ,index = 0):
        super(ThreadClass,self).__init__(parent)
        self.listlink = []
        self.index = index
        self.is_running = True
        self.follows = ''
        self.location = ['']
        self.viewss = 0
        self.soluongvd = 0
        self.viewvideo = []
        self.titlevideo = []
        self.likevideo = []
        self.linkvideo = []
        self.timevideo = []
        self.infoline = ''
    def setlistlink(self,listlink):
        self.listlink= listlink
    def run(self):
        self.signal.emit("Đang craw dữ liệu , vui lòng đợi")
        print("start thread ",self.index)
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        browser.set_window_size(800,1000)
        def chay(input):
            time.sleep(2)
            try:
                cl = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                cl.click()
                time.sleep(4)
            except:
                pass
            browser.get(self.listlink[i]+input+'about')
            time.sleep(2)
            try:
                cl = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                cl.click()
                time.sleep(3)
            except:
                pass
            try:
                follows = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]')))
                self.follows = follows.text
            except:
                pass

            browser.get(self.listlink[i]+input+'about_profile_transparency')
            time.sleep(2)
            try:
                cl = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                cl.click()
                time.sleep(4)
            except:
                pass
            browser.execute_script("window.scrollTo(0,500)")
            time.sleep(2)
            semore = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[6]/div")
            semore.click()
            time.sleep(3)
            try:
                location = browser.find_elements(By.XPATH,"//div[@class = 'x120dzms x1y1aw1k']")
                for l in location :
                    sss = l.text
                    self.location.append(sss)
                # print(self.location)
            except:
                pass
            browser.get(self.listlink[i]+input+'videos_by')
            time.sleep(2)
            try:
                cl = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                cl.click()
                time.sleep(2)
            except:
                pass            
            current_height = browser.execute_script("return document.documentElement.scrollHeight ")

            # Cuộn trang đến cuối
            browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

            # Lặp lại quá trình cuộn cho đến khi chiều cao trình duyệt không thay đổi
            while True:
                # Đợi một khoảng thời gian để trang tải nội dung mới (tuỳ chọn)
                time.sleep(1.5)
                
                # Lấy chiều cao mới của trình duyệt
                new_height = browser.execute_script("return document.documentElement.scrollHeight")
                
                # Kiểm tra xem đã cuộn đến cuối trang hay chưa
                if new_height == current_height:
                    break
                # Cập nhật chiều cao hiện tại và tiếp tục cuộn
                current_height = new_height
                browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(3)
            #tim div video
            videos = browser.find_element(By.XPATH,'//div[@class = "x1qjc9v5 x1lq5wgf xgqcy7u x30kzoy x9jhf4c x78zum5 xdt5ytf x1l90r2v xyamay9 xjl7jj"]')
            #tim tat ca video
            time.sleep(2)
            info_vd = videos.find_elements(By.XPATH, './/div[@class = "x9f619 x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6"]')
            print(f"co {len(info_vd)} video")
            self.soluongvd = len(info_vd)
            for inf in info_vd:
                try:
                    like = inf.find_element(By.XPATH,".//div[@class = 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz x1heor9g x78zum5 x6ikm8r x10wlt62']")
                    # print(like.text)
                    self.likevideo.append(like.text)
                    title = inf.find_element(By.XPATH,".//span[@class = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6']")
                    #tieu de video
                    self.titlevideo.append(title.text)
                    view = inf.find_elements(By.XPATH,".//div[@class = 'xt0e3qv']")
                    tm = view[0].text
                    self.timevideo.append(tm)    
                    views = view[1].text
                    # print(views)
                    self.viewvideo.append(views)
                    #tong so viewvideo 
                    self.viewss += convert_views_to_number(views)
                    hreff = inf.find_element(By.XPATH,".//a[@class ='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv']")
                    link = hreff.get_attribute("href")
                    self.linkvideo.append(link)
                    tme = inf.find_element(By.XPATH,"span[@class = 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm x12scifz x1yc453h']")
                    self.timevideo.append(tme.text)

                except:
                    pass
        print(' tong co ',str(len(self.listlink)),'link')
        for i in range(len(self.listlink)):
            print(self.listlink[i])
            with open(str(i)+'.txt',mode='w',encoding='utf8') as f:
                f.write('')
            if '?id=' not in self.listlink[i]:
                try:
                    
                    a = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                    a.click()

                except:
                    pass
                chay('/')

                for o in range(len(self.viewvideo)):
                    with open(str(i)+'.txt',mode='a',encoding='utf8') as f:
                        f.write(self.linkvideo[o]+'|'+self.titlevideo[o]+'|'+self.likevideo[o]+'|'+self.timevideo[o]+'|'+self.viewvideo[o])
                        f.write('\n')
                qg = ''
                for a in self.location:
                    # print(a)
                    qg+=a+','
                # print(qg)
                
                self.infoline += self.listlink[i]+'|'+self.follows+'|'+qg+'|'+str(self.soluongvd)+'|'+str(self.viewss)
                self.siganal.emit(self.infoline)
                self.viewss = 0
                self.infoline = ''
                self.viewvideo = []
                self.titlevideo = []
                self.likevideo = []
                self.linkvideo = []
                self.timevideo = []
            else:

                try:
                    
                    a = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                    a.click()
                except:
                    pass
                chay('&sk=')
                # print(i)
                for o in range(len(self.viewvideo)):
                    with open(str(i)+'.txt',mode='a',encoding='utf8') as f:
                        f.write(self.linkvideo[o]+'|'+self.titlevideo[o]+'|'+self.likevideo[o]+'|'+self.timevideo[o]+'|'+self.viewvideo[o])
                        f.write('\n')
                qg = ''
                for a in self.location:
                    # print(a)
                    qg+=a+','
                # print(qg)

                self.infoline += self.listlink[i]+'|'+self.follows+'|'+qg+'|'+str(self.soluongvd)+'|'+str(self.viewss)
                self.siganal.emit(self.infoline)
                self.viewss = 0
                self.infoline = ''
                self.viewvideo = []
                self.titlevideo = []
                self.likevideo = []
                self.linkvideo = []
                self.timevideo = []
        
        self.signal.emit("Đã craw xong du lieu")


    def stop(self):
        self.is_running = False
        print("stop thread : ", self.index)
        self.terminate()



app = QApplication(sys.argv)
icon = QIcon("logo.png")
app.setWindowIcon(icon)
widget = QtWidgets.QStackedWidget()
caw = Crawdata()
widget.addWidget(caw)
ui = Ui_Dialog()
# mainwd.show()
widget.setFixedHeight(HEIGHT)
widget.setFixedWidth(WIDTH)
widget.show()
app.exec()