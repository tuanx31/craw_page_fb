import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Khởi tạo trình duyệt Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scroll_to_bottom(driver):
    # Lấy chiều cao ban đầu của trang
    current_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Cuộn trang đến cuối
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # Sử dụng explicit wait để chờ cho sự kiện tải dữ liệu hoàn thành
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//footer")))
        except:
            break

        # Lấy chiều cao mới của trang
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        # Kiểm tra xem đã cuộn đến cuối trang hay chưa
        if new_height == current_height:
            break

        # Cập nhật chiều cao hiện tại
        current_height = new_height

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")

browser = webdriver.Chrome(options=chrome_options)
# browser.set_window_size(2000,4000)
# Truy cập vào trang đăng nhập Facebook
browser.get("https://www.facebook.com")
time.sleep(2)
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

# Kiểm tra xem đã đăng nhập thành công chưa
# Ở đây, ví dụ kiểm tra xem tiêu đề trang có chứa tên người dùng hay không
if "Facebook" in browser.title:
    print("Đăng nhập thành công!")
else:
    print("Đăng nhập thất bại!")
wait = WebDriverWait(browser, 10)

link = "https://www.facebook.com/minhkinh2888?mibextid=ZbWKwL"
if link == "":
    pass
else:
    browser.get(link)
    # try:
    # a = browser.find_element(By.XPATH,"//a[@class = 'x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x18o3ruo x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1heor9g x1ypdohk xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1vjfegm x3nfvp2 xrbpyxo xng8ra x16dsc37']")
    # a.click()
    # time.sleep(2)
    # a = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class = 'x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x18o3ruo x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1heor9g x1ypdohk xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1vjfegm x3nfvp2 xrbpyxo xng8ra x16dsc37']")))
    a = browser.find_element(By.XPATH,"//a[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x18o3ruo x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1heor9g x1ypdohk xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1vjfegm x3nfvp2 xrbpyxo xng8ra x16dsc37']")
    a.click()

    # except:
    #     pass
    link = browser.current_url
    print(link)
    browser.quit()
