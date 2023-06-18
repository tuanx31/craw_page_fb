from PyQt6.QtCore import QObject
from PyQt6 import QtCore , QtGui,QtWidgets,uic
from PyQt6.QtWidgets import QApplication , QMainWindow,QLineEdit,QPushButton,QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dialog import *
import MySQLdb
from reels import Reels
def get_smallest_number(a, b):
    smallest = min(a, b)
    return a if smallest == a else b
def convert_views_to_number(views_str):
    views_str = views_str.replace(" lượt xem", "")  # Loại bỏ " lượt xem" từ chuỗi
    if "K" in views_str:
        if ',' in views_str:
            views_str = views_str.replace(",", "")
            views_str = views_str.replace("K", "")
            views = float(views_str) * 100
        else:
            views_str = views_str.replace("K", "")
            views = float(views_str) * 1000
    else:
        views = int(views_str)
    return int(views)
def convert_to_number(string):
    if 'K' in string:
        a = string.replace('K', '')
        a = a.replace(',', '.')  # Thay dấu phẩy bằng dấu chấm
        number = float(a) * 1000
    else:
        a = string.replace(',', '.')  # Thay dấu phẩy bằng dấu chấm
        number = float(a)
    return int(number)

ban = 0
user = "MinhKinh"
try:
    mydb = MySQLdb.connect('103.97.126.28','deuszjyg_d-t-dowloader','123456','deuszjyg_d-t-dowloader')

    query = mydb.cursor()
    query.execute("SELECT * FROM `crawl` WHERE `user` LIKE 'MinhKinh'")
    kt = query.fetchone()

    ban = kt[1]
except:
    pass
print(ban)

HEIGHT = 463
WIDTH = 1500

solink = 0

class crawldata(QMainWindow):
    def __init__(self):
        
        super(crawldata,self).__init__()
        uic.loadUi('crawldata.ui',self)
        self.tableWidget.setColumnWidth(0,230)
        self.tableWidget.setColumnWidth(1,280)
        self.tableWidget.setColumnWidth(2,220)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setColumnWidth(5,100)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setColumnWidth(7,100)
        self.tableWidget.setColumnWidth(8,100)        
        self.tableWidget.setColumnWidth(9,100)        
        self.list_link = []
        self.thread = {}
        self.start.clicked.connect(self.startt)
        self.stop.clicked.connect(self.stopp)
        self.current_row = 0
        self.dem = 1
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
    }
""")
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
    def openreels(self):
        reels = Reels()
        button = self.sender()
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                cell_widget = self.tableWidget.cellWidget(row, col)
                if cell_widget == button:
                    self.current_row = row
                    break
        print(self.current_row)
        self.window = QtWidgets.QDialog()
        reels.setupUi(self.window)
        reels.setthuoctinh(str(self.current_row))
        self.window.show()

    def setthuoctinh(self,l):
        global solink
        self.tableWidget.setRowCount(solink+1)
        lst = l.split('|')
        self.link = QLineEdit()
        self.tableWidget.setCellWidget(solink,0,self.link)
        self.link.setText(lst[0])
        
        self.tenpage = QLineEdit()
        self.tableWidget.setCellWidget(solink,1,self.tenpage)
        self.tenpage.setText(lst[5])

        self.quocgia = QLineEdit()
        self.tableWidget.setCellWidget(solink,2,self.quocgia)
        self.quocgia.setText(lst[2])

        self.fle = QLineEdit()
        self.tableWidget.setCellWidget(solink,3,self.fle)
        self.fle.setText(lst[1])

        self.soluong = QLineEdit()
        self.tableWidget.setCellWidget(solink,4,self.soluong)
        self.soluong.setText(lst[3])

        self.tongview = QLineEdit()
        self.tableWidget.setCellWidget(solink,5,self.tongview)
        self.tongview.setText(lst[4])
        self.xem = QPushButton()

        self.tableWidget.setCellWidget(solink,8,self.xem)
        self.xem.setText("xem tt vdeo")
        self.xem.clicked.connect(lambda : self.opendialog())

        self.xemreels = QPushButton()
        self.tableWidget.setCellWidget(solink,9,self.xemreels)
        self.xemreels.setText("xem tt reels")
        self.xemreels.clicked.connect(lambda:self.openreels())

        self.soluongreels = QLineEdit()
        self.tableWidget.setCellWidget(solink,6,self.soluongreels)
        self.soluongreels.setText(lst[6])

        self.viewreels = QLineEdit()
        self.tableWidget.setCellWidget(solink,7,self.viewreels)
        self.viewreels.setText(lst[7])

        solink+=1
    def setlist(self):
        links = self.textcrawl.toPlainText()
        self.list_link = links.split('\n')
    def startt(self):
        if ban !=0:
            QMessageBox.information(self,"thong bao ", "bạn đã bị ban ")
        else:
            selected_item = self.comboBox.currentText()
            self.setlist()
            thr = ThreadClass(selected_item,parent=None,index=1)
            thr.setlistlink(self.list_link)
            self.thread[1]= thr
            self.thread[1].start()
            self.thread[1].signal.connect(self.thongbao)
            self.thread[1].siganal.connect(self.setthuoctinh)
            self.thread[1].tbao.connect(self.settbao)
            self.thread[1].fb.connect(self.setfb)
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
    def settbao(self,ssss):
        self.label_3.setText(ssss)
    def setfb(self,ii):
        self.label_5.setText(ii)



class ThreadClass(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    siganal = QtCore.pyqtSignal(str)
    tbao = QtCore.pyqtSignal(str)
    fb = QtCore.pyqtSignal(str)

    def __init__(self,selectitem, parent=None ,index = 0):
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
        self.tenpage = ''
        self.linkreels=[]
        self.viewreels = []
        self.tongviewreels = 0
        self.tongreels = 0
        self.select_item = selectitem
    def setlistlink(self,listlink):
        self.listlink= listlink

    def run(self):
        self.signal.emit("Đang crawl dữ liệu , vui lòng đợi")
        print("start thread ",self.index)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Tắt hiển thị hình ảnh
        chrome_options.add_argument("--disable-extensions")  # Tắt các tiện ích mở rộng
        # chrome_options.add_argument("--disable-gpu")  # Tắt GPU
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument('--headless')
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cache_dir = os.path.join(current_dir, "dulieu")
        chrome_options.add_argument(f"--user-data-dir={cache_dir}")
        browser = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(browser, 10)
        browser.set_window_size(2000,4000)
        def loginfb():
            self.fb.emit("đang login facebook")
            browser.get("https://www.facebook.com")

            # Đặt cookie

            with open("cookie.txt","r") as f:
                a = f.readline()
                f.close()

            cookie_str = a[:-1]
            # cookie_str = "sb=-CJ2YzTcmh-ztJmZCRcPqs8w;locale=vi_VN;c_user=100052160731642;wd=1278x951;datr=DemNZAxFXbhsDO3WVGYDzJWN;xs=41%3ATp3gCKSEoLA-aQ%3A2%3A1686639603%3A-1%3A6301%3A%3AAcWW2WsywBQ4VE0p6nNMDmujdpa_HNR4FCVCIZU07w;fr=0rBW8NevxIsZUjZm7.AWWMBolNZgsKltLxolCWP7qFrKo.BkjekQ.wH.AAA.0.0.BkjekQ.AWW1DeWW1cw"

            # Tách chuỗi cookie thành từng cặp key-value
            cookie_list = cookie_str.split(";")

            # Tạo dictionary lưu trữ các cookie
            cookies = {}
            for cookie in cookie_list:
                key, value = cookie.split("=")
                cookies[key.strip()] = value.strip()

            # Thiết lập cookie cho trình duyệt
            for key, value in cookies.items():
                browser.add_cookie({'name': key, 'value': value})

            # Refresh trang để áp dụng cookie
            browser.refresh()
            if "Facebook" in browser.title:
                print("Đăng nhập thành công!")
                self.fb.emit("Đăng nhập thành công!")
            else:
                print("Đăng nhập thất bại!")
                self.fb.emit("Đăng nhập thất bại!")

        def getvideos(input):
            self.tbao.emit("đang crawl video")
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
            time.sleep(1.5)
            # Lặp lại quá trình cuộn cho đến khi chiều cao trình duyệt không thay đổi
            while True:
                # Đợi một khoảng thời gian để trang tải nội dung mới (tuỳ chọn)
                time.sleep(2)
                # Lấy chiều cao mới của trình duyệt
                new_height = browser.execute_script("return document.documentElement.scrollHeight")
                time.sleep(1.5)
                # Kiểm tra xem đã cuộn đến cuối trang hay chưa
                if new_height == current_height:
                    break
                # Cập nhật chiều cao hiện tại và tiếp tục cuộn
                current_height = new_height
                browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            self.tbao.emit("đang crawl thong tin ")
            try:
                    #tim div video
                videos = browser.find_element(By.XPATH,'//div[@class = "x1qjc9v5 x1lq5wgf xgqcy7u x30kzoy x9jhf4c x78zum5 xdt5ytf x1l90r2v xyamay9 xjl7jj"]')
                #tim tat ca video
                time.sleep(1)
                #tim tat ca tag video
                info_vd = videos.find_elements(By.XPATH, './/div[@class = "x9f619 x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6"]')
                
                self.soluongvd = len(info_vd)
                print(f"co {self.soluongvd} video")
                for inf in info_vd:                    
                    try:
                        like = inf.find_element(By.XPATH,".//div[@class = 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz x1heor9g x78zum5 x6ikm8r x10wlt62']")
                        # print(like.text)
                        self.likevideo.append(like.text)
                    except:
                        self.likevideo.append('0')
                    title = inf.find_element(By.XPATH,".//span[@class = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6']")
                    #tieu de video
                    self.titlevideo.append(title.text)
                    view = inf.find_elements(By.XPATH,".//div[@class = 'xt0e3qv']")
                    tm = view[0].text
                    self.timevideo.append(tm)    
                    try:
                        views = view[1].text
                    except:
                        views = '0 lượt xem'
                        print(views)
                    # print(views)
                    self.viewvideo.append(views)
                    self.viewss += convert_views_to_number(views)
                    hreff = inf.find_element(By.XPATH,".//a[@class ='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv']")
                    link = hreff.get_attribute("href")
                    self.linkvideo.append(link)
                    tme = inf.find_element(By.XPATH,".//span[@class = 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm x12scifz x1yc453h']")
                    
                    self.timevideo.append(tme.text)


            except:
                # self.likevideo.append('none')
                # self.titlevideo.append('none')
                # self.timevideo.append('none')
                self.viewvideo.append('0')
                # self.linkvideo.append('none')
        def getreels(input):
            self.tbao.emit("đang crawl reels")
            if input == '&sk=':
                browser.get(self.listlink[i]+input+'reels_tab')

            if input == '/':
                browser.get(self.listlink[i]+input+'reels/')
            current_height = browser.execute_script("return document.documentElement.scrollHeight ")
            # Cuộn trang đến cuối
            browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            # Lặp lại quá trình cuộn cho đến khi chiều cao trình duyệt không thay đổi
            while True:
                # Đợi một khoảng thời gian để trang tải nội dung mới (tuỳ chọn)
                time.sleep(4)                
                # Lấy chiều cao mới của trình duyệt
                new_height = browser.execute_script("return document.documentElement.scrollHeight")
                time.sleep(1.5)
                # Kiểm tra xem đã cuộn đến cuối trang hay chưa
                if new_height == current_height:
                    break
                # Cập nhật chiều cao hiện tại và tiếp tục cuộn
                current_height = new_height
                browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(1)
            try:
                reel = browser.find_element(By.XPATH,"//div[@class = 'xod5an3']")

                #tab reels

                tabreels = reel.find_elements(By.XPATH,".//div[@class = 'x9f619 x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6']")
                self.tongreels = len(tabreels)
                # print(self.tongreels)
                for tab in tabreels:
                    #link reels
                    hreff = tab.find_element(By.XPATH,".//a[@class = 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq xqitzto x1n2onr6 xh8yej3']")
                    link = hreff.get_attribute("href")
                    # print(link)
                    self.linkreels.append(link)
                    view = tab.find_element(By.XPATH,".//span[@class = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']")
                    # print(view.text)
                    self.viewreels.append(view.text)
                    self.tongviewreels+=convert_to_number(view.text)
            except:
                self.linkreels.append('none')
            
        def gettenpage():
            self.tbao.emit("đang crawl tên page")
            try:
                tenpage = browser.find_element(By.XPATH,"//h1[@class = 'x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz']")
                self.tenpage = tenpage.text
            except:
                pass
        def getfollows(input):
            self.tbao.emit("đang crawl follow")
            try:
                cl = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                cl.click()
                time.sleep(1)
            except:
                pass
            browser.get(self.listlink[i]+input+'about')
            time.sleep(1.5)
            try:
                cl = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                cl.click()
                time.sleep(1.5)
            except:
                pass
            
            try:
                follows = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1s688f"]')))
            # self.follows = follows.text
                for fl in follows:
                    if " người theo dõi" in fl.text:
                        self.follows = fl.text
                        print(self.follows)
            except:
                self.follows = "page khong hien thi follows"
        def getquocgia(input):
            self.tbao.emit("đang crawl quốc gia")
            try:
                browser.get(self.listlink[i]+input+'about_profile_transparency')
            except:
                pass
            time.sleep(1.5)
            try:
                cl = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                cl.click()
                time.sleep(1.5)
            except:
                pass
            # browser.execute_script("window.scrollTo(0,500)")


            semore = browser.find_element(By.XPATH,"//div[@aria-label='See All']")
            semore.click()
            time.sleep(2)
            try:
                location = browser.find_elements(By.XPATH,"//div[@class = 'x120dzms x1y1aw1k']")
                for l in location :
                    sss = l.text
                    self.location.append(sss)
                print(self.location)
            except:
                self.tbao.emit("trang web khong public quoc gia")
        def chay(input):            
            getfollows(input)            
            gettenpage()
            getquocgia(input)
            getreels(input)
            getvideos(input)
            self.tbao.emit("đã crawl xong")
        def chifollows(input):
            getfollows(input)            
            gettenpage()
            getquocgia(input)
            # self.likevideo.append('none')
            # self.titlevideo.append('none')
            # self.timevideo.append('none')
            self.viewvideo.append('0')
            # self.linkvideo.append('none')
            # self.timevideo.append('none')
            # self.linkreels.append('none')
            self.tbao.emit("đã crawl xong")
        def chiquetvideo(input):
            getfollows(input)            
            gettenpage()
            getquocgia(input)
            getvideos(input)
            self.tbao.emit("đã crawl xong")
        def chiquetreels(input):
            getfollows(input)            
            gettenpage()
            getquocgia(input)
            getreels(input)
            self.tbao.emit("đã crawl xong")
        def quet10(input):
            getfollows(input)            
            gettenpage()
            getquocgia(input)
            # browser.execute_script("window.scrollTo(0,500)")
            self.tbao.emit("đang crawl reels")
            if input == '&sk=':
                browser.get(self.listlink[i]+input+'reels_tab')

            if input == '/':
                browser.get(self.listlink[i]+input+'reels/')
            time.sleep(2)
            try:
                reel = browser.find_element(By.XPATH,"//div[@class = 'xod5an3']")

                #tab reels

                tabreels = reel.find_elements(By.XPATH,".//div[@class = 'x9f619 x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6']")
                self.tongreels = len(tabreels)
                print(len(tabreels))
                for tab in tabreels:
                    #link reels
                    hreff = tab.find_element(By.XPATH,".//a[@class = 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq xqitzto x1n2onr6 xh8yej3']")
                    link = hreff.get_attribute("href")
                    # print(link)
                    self.linkreels.append(link)
                    view = tab.find_element(By.XPATH,".//span[@class = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']")
                    # print(view.text)
                    self.viewreels.append(view.text)
                    self.tongviewreels+=convert_to_number(view.text)
            except:
                self.linkreels.append('none')


        def ghifile():
            for o in range(get_smallest_number(len(self.linkreels),len(self.viewreels))):
                    with open("crawlreels/"+str(i)+'reels.txt',mode='a',encoding='utf8') as f:
                        f.write(self.linkreels[o]+'|'+str(self.viewreels[o]))
                        f.write('\n')
                        f.close()

                
            for o in range(len(self.linkvideo)):
                with open("crawlvideo/"+str(i)+'video.txt',mode='a',encoding='utf8') as f:
                    f.write(self.linkvideo[o]+'|'+self.titlevideo[o]+'|'+self.likevideo[o]+'|'+self.timevideo[o]+'|'+self.viewvideo[o])
                    f.write('\n')
                    f.close()
            qg = ''
            for a in self.location:
                    # print(a)
                    qg+=a+','
                # print(qg)
            print("có reels : ",self.tongreels)
            self.infoline += self.listlink[i]+'|'+self.follows+'|'+qg+'|'+str(len(self.linkvideo))+'|'+str(self.viewss)+'|'+self.tenpage+'|'+str(get_smallest_number(len(self.linkreels),len(self.viewreels)))+'|'+str(self.tongviewreels)
            print(self.infoline)
            self.siganal.emit(self.infoline)
            self.viewss = 0
            self.infoline = ''
            self.viewvideo = []
            self.titlevideo = []
            self.likevideo = []
            self.linkvideo = []
            self.timevideo = []
            self.timevideo = []
            self.infoline = ''
            self.tenpage = ''
            self.linkreels=[]
            self.viewreels = []
            self.tongviewreels = 0  
            self.location = []
        # print(' tong co ',str(len(self.listlink)),'link')
        loginfb()
        for i in range(len(self.listlink)):
            # print(self.listlink[i])
            with open("crawlvideo/"+str(i)+'video.txt',mode='w',encoding='utf8') as f:
                f.write('')
                f.close()
            with open("crawlreels/"+str(i)+'reels.txt',mode='w',encoding='utf8') as f:
                f.write('')
                f.close()
            if '?id=' not in self.listlink[i]:
                try:                    
                    a = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                    a.click()

                except:
                    pass
                if self.select_item == 'quét full page':
                    chay('/')
                elif self.select_item == 'chỉ quét follow':
                    chifollows('/')
                elif self.select_item == 'chỉ quét video':
                    chiquetvideo('/')
                elif self.select_item =='chỉ quét reels':
                    chiquetreels('/')
                elif self.select_item == 'quét 10 video/reels gần nhất':
                    quet10('/')
                ghifile()
                
            else:

                try:
                    
                    a = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
                    a.click()
                except:
                    pass
                if self.select_item == 'quét full page':
                    chay('&sk=')
                elif self.select_item == 'chỉ quét follow':
                    chifollows('&sk=')
                elif self.select_item == 'chỉ quét video':
                    chiquetvideo('&sk=')
                elif self.select_item =='chỉ quét reels':
                    chiquetreels('&sk=')
                elif self.select_item == 'quét 10 video/reels gần nhất':
                    quet10('&sk=')
                ghifile()
        browser.quit()
        self.signal.emit("Đã crawl xong du lieu")


    def stop(self):
        self.is_running = False
        print("stop thread : ", self.index)
        self.terminate()



app = QApplication(sys.argv)
icon = QIcon("logo.png")
app.setWindowIcon(icon)
widget = QtWidgets.QStackedWidget()
caw = crawldata()
widget.addWidget(caw)
ui = Ui_Dialog()
# mainwd.show()
widget.setFixedHeight(HEIGHT)
widget.setFixedWidth(WIDTH)
widget.show()
app.exec()