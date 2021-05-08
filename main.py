from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver_path = r'C:\Users\tanma\PycharmProjects\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
options.add_argument(r'--user-data-dir=C:\\Users\\tanma\\AppData\\Local\\Google\\Chrome\\User Data\\wtsp')  # here is no <Default>!
driver = webdriver.Chrome(executable_path=driver_path, options=options)  # selenium 4 prefers "options"
wait = WebDriverWait(driver, 600)
i = 0
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
    name = "Crypto Price tracker"
    group = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    time.sleep(10)
    group.click()
    print('Whatsapp group found')
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    time.sleep(3)
    msg_box.clear()
    msg_box.send_keys(a)
    button = driver.find_element_by_class_name('_1E0Oz')
    button.click()
    print('Price sent')
    time.sleep(60)
driver.close()
