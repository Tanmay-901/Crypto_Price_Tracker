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


class Editlist:

    def __init__(self):
        self.coinlist_action = ""
        self.coinlist = []
        self.edit = 0
        self.removable = ""
        self.main_list = ['Zilliqa', 'Band Protocol', 'Algorand', 'Theta Network', 'iExec RLC', 'Cosmos',
                          'DigiByte', 'Chiliz', 'Terra', 'Theta Fuel', 'Waves', 'Nano', 'IOST', 'Tezos',
                          'VeChain', 'DOT', 'Elrond', 'NEM', 'Filecoin', 'Bitcoin', 'Ethereum', 'Dogecoin',
                          'Ripple', 'Tron', 'Binance Coin', 'Cardano', 'Bitcoin Cash', 'EOS', 'GAS', 'NEO',
                          'Litecoin', 'Chainlink', 'Tether', 'Dash', 'Aave', 'Uniswap', 'True USD', 'USD Coin',
                          'Compound', '0x', 'AdEx', 'Augur', 'Bancor', 'Basic Attention Token', 'Civic', 'Enjin Coin',
                          'Fetch.ai', 'Golem', 'Kyber Network', 'Metal', 'OmiseGO', 'Paxos Standard Token', 'Power Ledger',
                          'DIA', 'Sushi', 'Quantstamp', 'Numeraire', 'yearn.finance', 'Dai', 'Loopring', 'AirSwap',
                          'Republic Protocol', 'Maker', 'QuarkChain', 'Swipe', 'Synthetix Network Token', 'Stellar',
                          'DFI.money', 'Ripio Credit Network', 'Status', 'Storj', 'aelf', 'district0x']

    def take_input(self):
        while 1:
            c = input("\nEnter New Coin or 'N' to Proceed: ")
            if c == "n":
                break
            else:
                if c in self.main_list and c not in self.coinlist:
                    self.coinlist.append(c)
                    c = ""
                elif c not in self.main_list:
                    print("\nInvalid Input!!!   Please check the spelling and enter Case sensitive input :)")
                    continue
                elif c in self.coinlist:
                    print("\nCoin Already Present")
                    continue
        self.send_price_to_file()

    def new_list(self):
        self.coinlist = []
        self.take_input()

    def add_coin(self):
        self.take_input()

    def remove_coin(self):
        print("\nCOIN LIST =>", *self.coinlist)
        while 1:
            self.removable = input("\nEnter coin name from the list to be removed or enter 'n' if done: ")
            if self.removable == 'n':
                break
            elif self.removable in self.coinlist:
                self.coinlist.remove(self.removable)
                print("\nCOIN LIST =>", *self.coinlist)
            else:
                continue
        self.send_price_to_file()

    def edit_list(self):
        print("\nCOIN LIST =>", *self.coinlist)
        while 1:
            self.coinlist_action = input("\nEnter 1 to add coin || 2 to remove coin || 3 to proceed: ")
            if self.coinlist_action == "1":
                self.add_coin()
            elif self.coinlist_action == "2":
                self.remove_coin()
            elif self.coinlist_action == "3":
                self.coinlist_action = ""
                break
        return self.coinlist

    def get_price_from_file(self):
        self.coin_record = open("coins.txt", "r")
        ls = self.coin_record.readlines()
        for item in ls:
            self.coinlist.append(item.strip())
        self.coin_record.close()
        print("\nCOIN LIST =>", *self.coinlist)
        return self.coinlist

    def send_price_to_file(self):
        self.coin_record = open("coins.txt", "w+")
        for item in self.coinlist:
            self.coin_record.write(item + '\n')
        self.coin_record.close()


def access_website(url, counter):
    while 1:
        try:
            driver.get(url)
            break
        except:
            pass
    counter += 1
    print('\n{}:'.format(counter), end=" -> ")
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
    current_time = time.strftime("%H:%M", x)
    print('Price sent at ', current_time, end=": ")
    driver.get('https://www.google.com/')
    try:                                   # Catching "leave site?" alert
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        usertext, timer = timedKey(" | press 'Q' to quit | 'E' to edit coin list | 'F' to force rerun | "
                                   "or wait to auto-run: "
                                   , allowCharacters=['q', 'Q', 'e', 'E', 'f', 'F'], timeOut=280)
        if usertext == 'e' or usertext == 'E':
            edit_list = 2
        elif usertext == 'q' or usertext == 'Q':
            driver.close()
            quit()
        if usertext == 'f' or usertext == 'F':
            edit_list = 1
            return edit_list
        elif timer:
            edit_list = 1
            pass
    except RuntimeError:
        time.sleep(280)
    finally:
        return edit_list


if __name__ == "__main__":
    i = 0
    j = 0
    t = 280
    coin = ""
    REMOTE_SERVER = "one.one.one.one"
    print('checking connectivity', end="..")
    is_connected(REMOTE_SERVER, j)
    print('internet connected\n')
    a = Editlist()
    try:
        coins = a.get_price_from_file()
        coinlist_action = int(input("\nEnter 1 to proceed with  previous coins or 2 to Change: "))
        if coinlist_action == 1:
            pass
        elif coinlist_action == 2:
            coins = a.edit_list()
    except FileNotFoundError:
        coins = []
        print("Running script 1st time, Need to add coins")
        a.add_coin()
        coinlist_action = 1
        a.send_price_to_file()
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
            recipients = ['Crypto Price tracker']
            url = "https://coinswitch.co/coins/dogecoin/dogecoin-to-inr"
            i = access_website(url, i)
            prices = fetch_price(coins)
            access_wtsp()
            # driver.save_screenshot("screenshot.png")
            send_price(recipients, prices)
            # print(prices)
            coinlist_action = cooldown_period(t, coinlist_action)
            if coinlist_action == 1:
                pass
            elif coinlist_action == 2:
                coins = a.edit_list()
            # break
        except:
            print('\nError occurred... Handling the error...\n')
            pass
    driver.close()
