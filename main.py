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


def access_website(url, counter):
    while 1:
        counter += 1
        try:
            driver.get(url)
            break
        except:
            pass
    print('{}: coinswitch website accessed'.format(counter))


def fetch_price(coins):
    prices = ""
    for coin in coins:
        g = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@data-asset="{}"]'.format(coin)))).text
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
    print("Whatsapp accessed")
    time.sleep(5)


def send_price(names, prices):
    for name in names:
        # search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        #         (By.XPATH, '//div[@class="_2_1wd copyable-text selectable-text"]')))
        search_box = driver.find_element_by_xpath('//div[@class="_2_1wd.copyable-text.selectable-text"]')
        time.sleep(5)
        pyperclip.copy(name)
        search_box.send_keys(Keys.CONTROL + "v")
        print("search initiated...")
        group = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//span[@title = "{}"]'.format(name))))
        group.click()
        print('Whatsapp group found')
        msg_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')))
        msg_box.clear()
        pyperclip.copy(prices)
        msg_box.send_keys(Keys.CONTROL + "v")
        time.sleep(10)
        msg_box.send_keys(Keys.ENTER)


def cooldown_period(timer):
    x = time.localtime()
    current_time = time.strftime("%H:%M:%S", x)
    print('Price sent at ', current_time)
    driver.get('https://www.google.com/')
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    time.sleep(timer)


# if __name__ == "__main__":
i = 0
t = 280
while 1:
    # try:
        recipients = ['Crypto Price tracker']
        url = "https://coinswitch.co/coins/dogecoin/dogecoin-to-inr"
        access_website(url, i)
        coins = ['Dogecoin', 'DigiByte', 'Nano', 'NEM', 'VeChain']  # fixed tracking
        prices = fetch_price(coins)
        access_wtsp()
        send_price(recipients, prices)
        # print(prices)
        cooldown_period(t)
        # break
    # except:
    #     print('Error occurred... Handling the error')
    #     pass
driver.close()
