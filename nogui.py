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
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")

browser = webdriver.Chrome(options=chrome_options)
# browser.set_window_size(2000,4000)
# Truy cập vào trang đăng nhập Facebook
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

# Kiểm tra xem đã đăng nhập thành công chưa
# Ở đây, ví dụ kiểm tra xem tiêu đề trang có chứa tên người dùng hay không
if "Facebook" in browser.title:
    print("Đăng nhập thành công!")
else:
    print("Đăng nhập thất bại!")

browser.get("https://www.facebook.com/profile.php?id=100090960481247&sk=reels_tab")



scroll_to_bottom(browser)

print("da thoat vong lap")
time.sleep(5)

l  = []
v = []
#ô# real chứa reall
reel = browser.find_element(By.XPATH,"//div[@class = 'xod5an3']")

#tab reels

tabreels = reel.find_elements(By.XPATH,".//div[@class = 'x9f619 x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6']")

print(len(tabreels))
for tab in tabreels:
    #link reels
    hreff = tab.find_element(By.XPATH,".//a[@class = 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq xqitzto x1n2onr6 xh8yej3']")
    link = hreff.get_attribute("href")
    # print(link)
    l.append(link)
    view = tab.find_element(By.XPATH,".//span[@class = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']")
    # print(view.text)
    v.append(view.text)


