# Crypto_Price_Tracker
----------------------
## Tracks crypto price on a platform and sends them to your whatsapp
For this project, the prices are tracked on [Coinswitch website](https://coinswitch.co/coins/dogecoin/dogecoin-to-inr)(because that's what we were using for crypto transactions).  
-----------------------
## Pre-requisites:  
* Selenium must be installed in python `pip install selenium`.  
* Chromedriver with same version as of chrome must be installed and location be updated in code [click here](https://chromedriver.chromium.org/downloads).  
* Install pytimedinput package `pip install pytimedinput`.  
* Install pyperclip `pip install pyperclip`.  

-----------------------
## Keep in mind:  
1. **It's best to run the program using command prompt**  
2. If you want the program not to interfere with your default chrome window, you can make a copy  of the user data of google chrome *(Instructions to be added soon)* .  
3. The program is made to be as interactable as possible from command prompt window, but since it is still new there may be chances of some bugs which
you may report in the Issues section.  
-----------------------
## CMD Interface:  
![CMD Interface](https://github.com/Tanmay-901/Important-details/blob/master/Images/Screenshot%20(312).png)
(ignore the devtools listening processing, it is return from selenium starting to scrap data)  

## Steps to use:
1. First the script will check for internet connectivity.  
2. Then it'll check for any pre-saved list of coins and if you're running for the first time you need to add coins first. 
3. Press "1" to proceed with the pre-saved Coin List (if there's any) or "2" to change the list.  
4. If you're runnning the script for the first time or want to change the list of coins follow the below steps:-  
    * If editing the list, select if you want to add or remove coins. If running for the first time directly start adding coin names.  
    * Once you're done adding the coins, enter 'n' to proceed further.  
    * It'll again ask if you want to do any further changes about adding or removing coins, press "3" if you're done.  
    * After that the program will begin to scrap data of the website and send them to your whatsapp through whatsapp web.  
----------------------------------
  
## Working Status(can be modified as per convinience):
![Working status](https://github.com/Tanmay-901/Important-details/blob/master/Images/Crypto_price_tracker_working_status.png)  
  
1. Here you'll the the number of times and the time at which the prices were sent.  
2. After each iteration (each value sent) you'll have following options(case insensitive):- 
   * Press 'Q' to exit the program.  
   * Press 'E' to edit the coin list.  
   * Press 'F' to force run the program to send the value immediately again.
   * Wait for the timer to end and Re-run the program automatically with the same coin list approximately at 5 minutes interval.  
     (can vary because of different reasons such as processor speed, network speed etc.)
