from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pytimedinput import timedKey
import pyperclip
import time
import socket


def is_connected(hostname, j=0):
    print('1')
    print('.', end=" ")
    pass
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        j = 0
        print("\n")
        return True
    except:
        pass
    if not j:
        j += 1
        print("No Internet, trying", end=" ")
        is_connected(REMOTE_SERVER, j)
    else:
        print(".", end=" ")
        time.sleep(1)
        is_connected(REMOTE_SERVER, j)


def editlist(edit):
    main_list = ['Zilliqa', 'Band Protocol', 'Algorand', 'Theta Network', 'iExec RLC', 'Cosmos',
            'DigiByte', 'Chiliz', 'Terra', 'Theta Fuel', 'Waves', 'Nano', 'IOST', 'Tezos',
            'VeChain', 'DOT', 'Elrond', 'NEM', 'Filecoin', 'Bitcoin', 'Ethereum', 'Dogecoin',
            'Ripple', 'Tron', 'Binance Coin', 'Cardano', 'Bitcoin Cash', 'EOS', 'GAS', 'NEO',
            'Litecoin', 'Chainlink', 'Tether', 'Dash', 'Aave', 'Uniswap', 'True USD', 'USD Coin',
            'Compound', '0x', 'AdEx', 'Augur', 'Bancor', 'Basic Attention Token', 'Civic', 'Enjin Coin',
            'Fetch.ai', 'Golem', 'Kyber Network', 'Metal', 'OmiseGO', 'Paxos Standard Token', 'Power Ledger',
            'DIA', 'Sushi', 'Quantstamp', 'Numeraire', 'yearn.finance', 'Dai', 'Loopring', 'AirSwap',
            'Republic Protocol', 'Maker', 'QuarkChain', 'Swipe', 'Synthetix Network Token', 'Stellar',
            'DFI.money', 'Ripio Credit Network', 'Status', 'Storj', 'aelf', 'district0x']
    c = ""
    coinlist = []
    if edit == 0:
        while 1:
            check = ""
            c = input("Enter One coin at a time: ")
            if c in main_list:
                coinlist.append(c)
                c = ""
            else:
                print("Invalid Input!!!   Please check the spelling and enter Case sensitive input :)")
                continue
            check = input("Enter 'y' to add new coin or any other to proceed: ")
            if check == "y":
                continue
            else:
                print('Tracking => \n', *coinlist)
                edit = 1
                return coinlist, edit


def access_website(url, counter):
    while 1:
        try:
            driver.get(url)
            break
        except:
            pass
    counter += 1
    print('{}:'.format(counter), end=" -> ")
    return counter


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


def cooldown_period(timer, edit_list):
    x = time.localtime()
    current_time = time.strftime("%H:%M:%S", x)
    print('Price sent at ', current_time, end=": ")
    driver.get('https://www.google.com/')
    try:                                   # Catching "leave site?" alert
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        usertext, timer = timedKey(" || press 'q' to quit OR 'e' to edit coin list: ", allowCharacters=['q', 'Q','e','E'], timeOut=280)
        if timer:
            edit_list = 1
            pass
        elif usertext == 'e' or usertext == 'E':
            print("Enter New List")
            edit_list = 0
        elif usertext == 'q' or usertext == 'Q':
            driver.close()
            quit()
    except RuntimeError:
        time.sleep(280)
    finally:
        return edit_list


if __name__ == "__main__":
    i = 0
    j = 0
    t = 280
    coins = []
    coin = ""
    edit_list = 0
    REMOTE_SERVER = "one.one.one.one"
    print('checking connectivity', end="..")
    is_connected(REMOTE_SERVER, j)
    print('internet connected')
    while edit_list == 0:
        coins, edit_list = editlist(edit_list)
    else:
        pass
    driver_path = r'C:\Users\tanma\PycharmProjects\chromedriver.exe'
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument("window-size=300*170")
    # options.add_argument("disable-gpu")
    options.add_argument("user-data-dir=C:\\Users\\tanma\\AppData\\Local\\Google\\Chrome\\User Data - Copy")
    driver = webdriver.Chrome(executable_path=driver_path, options=options)  # selenium 4 prefers "options"
    wait = WebDriverWait(driver, 600)
    while 1:
        try:
            if edit_list == 0:
                coins, edit_list = editlist(edit_list)
            else:
                pass
            recipients = ['Crypto Price tracker']
            url = "https://coinswitch.co/coins/dogecoin/dogecoin-to-inr"
            i = access_website(url, i)
            prices = fetch_price(coins)
            access_wtsp()
            driver.save_screenshot("screenshot.png")
            send_price(recipients, prices)
            # print(prices)
            edit_list = cooldown_period(t, edit_list)
            # break
        except:
            print('\nError occurred... Handling the error...')
            pass
