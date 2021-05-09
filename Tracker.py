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
options.add_argument("disable-gpu")
options.add_argument("user-data-dir=C:\\Users\\tanma\\AppData\\Local\\Google\\Chrome\\dataset")
driver = webdriver.Chrome(executable_path=driver_path, options=options)  # selenium 4 prefers "options"
wait = WebDriverWait(driver, 600)


def access_website(url, counter):
    while 1:
        counter += 1
        try:
            driver.get(url)
            break
        except:
            pass
    # print('{}: coinswitch website accessed'.format(counter))


def fetch_price(coins):
    prices = ""
    for coin in coins:
        g = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@data-asset="{}"]'.format(coin)))).text
        # print(g.index(' '), g.index('₹'))
        print((coin + ': ' + g[g.index('₹'):]))
        prices += (coin + ': ' + g[g.index('₹'):] + '\n')
    return prices


def access_wtsp():
    while 1:
        try:
            driver.get("https://web.whatsapp.com/")
            break
        except:
            pass


def send_price(names, prices):
    for name in names:

        search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
                (By.CLASS_NAME, '_2_1wd.copyable-text.selectable-text')))
        pyperclip.copy(name)
        search_box.send_keys(Keys.CONTROL + "v")
        group = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//span[@title = "{}"]'.format(name))))
        group.click()
        print('Whatsapp group found')
        # for price in prices:
        msg_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')))
        msg_box.clear()
        pyperclip.copy(prices)
        msg_box.send_keys(Keys.CONTROL + "v")
        msg_box.send_keys(Keys.ENTER)
        # time.sleep(5)
        # try:
        #     print('alert accepted')
        #     driver.switch_to.alert.accept()
        # except:
        #     pass


def cooldown_period(timer):
    x = time.localtime()
    current_time = time.strftime("%H:%M:%S", x)
    print('Price sent at ', current_time)
    # try:
    #     print('alert accepted')
    #     driver.switch_to.alert.accept()
    # except:
    #     pass
    driver.get('https://www.google.com/')
    try:
        # print('alert accepted')
        driver.switch_to.alert.accept()
    except:
        pass
    time.sleep(timer)


i = 0
t = 120
coins = list(input('Enter coins to be tracked: ').split())
while 1:
    try:
        recipients = ['Crypto Price tracker']
        url = "https://coinswitch.co/coins/dogecoin/dogecoin-to-inr"
        access_website(url, i)
        # coins = ['Dogecoin', 'IOST', 'Zilliqa', 'Nano', 'NEM', 'VeChain'] # fixed tracking
        prices = fetch_price(coins)
        access_wtsp()
        send_price(recipients, prices)
        # print(prices)
        cooldown_period(t)
    except:
        print('Error occurred... Handling the error')
        pass
