from selenium import webdriver
import time
# Khởi tạo trình duyệt Chrome
browser = webdriver.Chrome()

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

time.sleep(2)
# Đóng trình duyệt
browser.quit()
