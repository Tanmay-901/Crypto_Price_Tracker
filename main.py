from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

driver_path = r'C:\Users\tanma\PycharmProjects\chromedriver.exe'
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("--window-size=1440, 900")
# options.add_argument("disable-gpu")
options.add_argument("user-data-dir=C:\\Users\\tanma\\AppData\\Local\\Google\\Chrome\\dataset")
driver = webdriver.Chrome(executable_path=driver_path, options=options)  # selenium 4 prefers "options"
# driver.maximize_window()
wait = WebDriverWait(driver, 600)
i = 0
t = time.localtime()
name = "Crypto Price tracker"
while 1:
    try:
        i += 1
        while 1:
            try:
                driver.get("https://coinswitch.co/coins/dogecoin/dogecoin-to-inr")
                break
            except:
                pass
        print('{}: coinswitch website accessed'.format(i))
        g = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@data-asset="Dogecoin"]'))).text
        price = g[:4] + ':' + g[10:]
        print(price)
        while 1:
            try:
                driver.get("https://web.whatsapp.com/")
                break
            except:
                pass
        search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.CLASS_NAME, '_2_1wd.copyable-text.selectable-text')))
        pyperclip.copy(name)
        search_box.send_keys(Keys.CONTROL + "v")
        group = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//span[@title = "{}"]'.format(name))))
        group.click()
        print('Whatsapp group found')
        msg_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')))
        msg_box.clear()
        msg_box.send_keys(price)
        msg_box.send_keys(Keys.ENTER)
        time.sleep(2)
        current_time = time.strftime("%H:%M:%S", t)
        print('Price sent at ', current_time)
        driver.get('https://www.google.com/')
        time.sleep(60)
    except:
        print("Going into error handling mode")
        continue
driver.close()
