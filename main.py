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
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
options.add_argument(r'--user-data-dir=C:\\Users\\tanma\\AppData\\Local\\Google\\Chrome\\User Data\\wtsp')  # here is no <Default>!
driver = webdriver.Chrome(executable_path=driver_path, options=options)  # selenium 4 prefers "options"
# driver.maximize_window()
wait = WebDriverWait(driver, 600)
i = 0
name = "Crypto Price tracker"
search_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
while 1:
    i += 1
    driver.get("https://coinswitch.co/coins/dogecoin/dogecoin-to-inr")
    time.sleep(3)
    print('{}: coinswitch website accessed'.format(i))
    g = driver.find_elements_by_class_name('assets__price')
    a = 'Doge: ' + g[20].text
    print(a)
    driver.get("https://web.whatsapp.com/")
    time.sleep(5)
    # search_box = WebDriverWait(driver, 500).until(EC.presence_of_element_located(
    #     (By.CLASS_NAME, '_2_1wd.copyable-text.selectable-text')))
    # search_box = driver.find_element_by_xpath(search_xpath)
    search_box = driver.find_element_by_class_name('_2_1wd.copyable-text.selectable-text')
    pyperclip.copy(name)
    search_box.send_keys(Keys.CONTROL + "v")
    group = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    # time.sleep(10)
    group.click()
    print('Whatsapp group found')
    msg_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    time.sleep(3)
    msg_box.clear()
    msg_box.send_keys(a)
    msg_box.send_keys(Keys.ENTER)
    # button = driver.find_element_by_class_name('_1E0Oz')
    # button.click()
    print('Price sent')
    time.sleep(60)
driver.close()
