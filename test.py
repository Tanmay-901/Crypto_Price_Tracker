from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time


# coins = list(input('Enter coins to be tracked: ').strip().split())
driver_path = r'C:\Users\tanma\PycharmProjects\chromedriver.exe'
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("--window-size=1440, 900")
# options.add_argument("disable-gpu")
options.add_argument("uaser-data-dir=C:\\Users\\tanma\\AppData\\Local\\Google\\Chrome\\User Data - Copy")
driver = webdriver.Chrome(executable_path=driver_path, options=options)  # selenium 4 prefers "options"
wait = WebDriverWait(driver, 600)
driver.maximize_window()

driver.get('https://web.whatsapp.com/')
driver.save_screenshot("screenshot1.png")
search_box = driver.find_element_by_xpath('//div[@class="_2_1wd.copyable-text.selectable-text"]')
driver.save_screenshot("screenshot2.png")
driver.close()
