import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
import time

browser.get('https://www.facebook.com')

us = browser.find_element(By.ID,'email')
us.send_keys("100052160731642")

pw = browser.find_element(By.ID,'pass')
pw.send_keys("89075933")

time.sleep(30)

pickle.dump(browser.get_cookie('a'),open("coookie.pkl",'wb'))
browser.close()