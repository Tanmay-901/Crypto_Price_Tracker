import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pytimedinput import timedKey
import pyperclip
import time


# coins = list(input('Enter coins to be tracked: ').strip().split())
driver_path = r'C:\Users\tanma\PycharmProjects\chromedriver.exe'
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("--window-size=1080, 720")
options.add_argument("disable-gpu")
options.add_argument("user-data-dir=C:\\Users\\tanma\\AppData\\Local\\Google\\Chrome\\User Data - Copy")
driver = webdriver.Chrome(executable_path=driver_path, options=options)  # selenium 4 prefers "options"
wait = WebDriverWait(driver, 600)


def access_website(url, counter):
    while 1:
        try:
            driver.get(url)
            break
        except:
            pass
    print('{}:'.format(counter), end=" -> ")


def fetch_price(coins):
    prices = ""
    for coin in coins:
        g = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@data-asset="{}"]'.format(coin)))).text
        # print((coin + ': ' + g[g.index('₹'):]))
        prices += (coin + ': ' + g[g.index('₹'):] + '\n')
    return prices


def access_wtsp():
    while 1:
        try:
            driver.get("https://web.whatsapp.com/")
            break
        except:
            pass
    # print("Whatsapp accessed")


def send_price(names, prices):
    for name in names:
        # search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        #         (By.XPATH, '//div[@contenteditable="true"][@data-set="3"]')))
        search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
                (By.XPATH, '//div[@class="_2_1wd copyable-text selectable-text"]')))
        # search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-set="3"]')
        # search_box = driver.find_element_by_xpath('//div[@class="_2_1wd.copyable-text.selectable-text"]')
        pyperclip.copy(name)
        search_box.send_keys(Keys.CONTROL + "v")
        group = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//span[@title = "{}"]'.format(name))))
        group.click()
        # print('Whatsapp group found')
        msg_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')))
        msg_box.clear()
        pyperclip.copy(prices)
        msg_box.send_keys(Keys.CONTROL + "v")
        msg_box.send_keys(Keys.ENTER)


def cooldown_period(timer):
    x = time.localtime()
    current_time = time.strftime("%H:%M:%S", x)
    print('Price sent at ', current_time, end=": ")
    driver.get('https://www.google.com/')
    try:                                   # Catching "leave site?" alert
        driver.switch_to.alert.accept()
    except:
        pass
    usertext, timer = timedKey(" || press 'q' to quit: ", allowCharacters=['q', 'Q'], timeOut=280)
    if timer:
        pass
    elif usertext == 'q' or usertext == 'Q':
        driver.close()
        quit()


if __name__ == "__main__":
    i = 0
    t = 280
    while 1:
        try:
            i += 1
            recipients = ['Crypto Price tracker']
            url = "https://coinswitch.co/coins/dogecoin/dogecoin-to-inr"
            access_website(url, i)
            coins = ['Dogecoin', 'Nano', 'DigiByte', 'NEM', 'VeChain']  # fixed tracking
            prices = fetch_price(coins)
            access_wtsp()
            driver.save_screenshot("screenshot.png")
            send_price(recipients, prices)
            # print(prices)
            cooldown_period(t)
            # break
        except:
            print('\nError occurred... Handling the error...')
            pass
