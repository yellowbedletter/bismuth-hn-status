from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Creates a headless chrome session for the Hypernodes page
# Make sure you have the correct chromedriver installed in the right path
CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=%s" % WINDOW_SIZE)
options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=options
                          )
url = 'https://hypernodes.bismuth.live/?page_id=163'
driver.get(url)

# Finds active Hypernode tables and stores them in respective variables
tabl4 = driver.find_elements_by_xpath('//*[@id="content"]/form/table[4]/tbody')
height = driver.find_elements_by_xpath('//*[@id="content"]/form/table[4]/tbody\
/tr[2]/td[7]/font')
hnreward = driver.find_elements_by_xpath('//*[@id="content"]/form/table[5]\
/tbody/tr[2]/td[2]')
hnROI = driver.find_elements_by_xpath('//*[@id="content"]/form/table[5]/tbody\
/tr[2]/td[4]')

# Adds table of active HNs to Active list
Active_list = []
for tag in tabl4:
    Active_list.append(tag.text)

# Adds blockheight to list
Blockheight = []
for tag in height:
    Blockheight.append(tag.text)

# Adds weekly hypernode rewards to list
W_hnreward = []
for tag in hnreward:
    W_hnreward.append(tag.text)

# Adds annual hypernode rewards to list, takes str out of list, turns it into a
# floating point, divides it by 100 then turns it back into a string.
A_hnreward = []
for tag in hnROI:
    A_hnreward.append(tag.text)

A_hnrewardstr = ' '.join(map(str, A_hnreward))
Hn_ROI = str((int(float(A_hnrewardstr) / 100)))

# Navigates to new page // Enter the URL of your reward address
url = 'https://hypernodes.bismuth.live\
/?page_id=152&ac=2e008722ee36cbab11c3ced3bafe11762a0ffc67058660324f156438'
driver.get(url)

# Finds account balance tables and stores them in relative variables
Bisbal = driver.find_elements_by_xpath('//*[@id="content"]/table[3]\
/tbody/tr[3]/td[2]')
USDbal = driver.find_elements_by_xpath('//*[@id="content"]/table[3]/tbody\
/tr[4]/td[2]')

# Adds BIS balance to list
B_bal = []
for tag in Bisbal:
    B_bal.append(tag.text)

# Adds USD balance to list
USD_bal = []
for tag in USDbal:
    USD_bal.append(tag.text)

# Navigates to new page
url = 'https://coinpaprika.com/coin/bis-bismuth/'
driver.get(url)

BISBTC = driver.find_elements_by_xpath('//*[@id="cp-app"]/div[2]/section[1]\
/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span')

BISinSats = []
for tag in BISBTC:
    BISinSats.append(tag.text)

# Calculates the price of Bismuth in USD & BTC and prints it


def BIS_price():
    x = ' '.join(map(str, USD_bal))
    y = x.split()
    z = y[1]
    bisprice = int(z) / float(' '.join(map(str, B_bal)))
    print(
        'The price of Bismuth is: ' + "\033[1m" + str(("%.3f" % bisprice))
        + ' USD' + '\033[0m' + ' // ' + "\033[1m"
        + '  '.join(map(str, BISinSats)) + '\033[0m'
    )


# Calculates the weekly payout in USD


def USD_payout():
    x = ' '.join(map(str, USD_bal))
    y = x.split()
    z = y[1]
    usdprice = int(z) / float(' '.join(map(str, B_bal)))
    wkly_hn = float(' '.join(map(str, W_hnreward)))
    print(
        'Avg. weekly payout in USD is: '
        + str(("%.2f" % (usdprice * wkly_hn))) + ' USD'
    )


# Closes chrome session
driver.quit()

# Your Hypernode IP address:
the_one = '11.11.111.11'

# Finds blockheight corresponding to IP address and prints message according
# to whether it matches the blockheight of HN #2 or not.


def search_height():
    A_list = (' '.join(map(str, Active_list)))
    IP = (A_list.find(the_one))
    b1 = IP + 35
    b2 = IP + 36
    b3 = IP + 37
    b4 = IP + 38
    b5 = IP + 39
    b6 = IP + 40
    b7 = IP + 41
    bh = A_list[b1] + A_list[b2] + A_list[b3] + A_list[b4] + A_list[b5]\
        + A_list[b6] + A_list[b7]

    for i in A_list:
        if bh == ' '.join(map(str, Blockheight)):
                print(
                    'Hypernode is currently in sync!'
                )
                print(" ")
        else:
                print(
                    'Hypernode is currently out of sync!'
                    )
                print(" ")
                print('HN blockheight is: ' + bh)
        break


# Iterates over lists and sends email (or prints) with update
for i in Active_list:
    if the_one not in i:
        print(" ")
        print('---------------------------------------------------')
        print(" ")
        print('\033[1m' + "Status Hypernode: Inactive!")
        print("\033[0m ")
        print(" ")
        BIS_price()
        print(" ")
        print(
            'BIS Reward Balance: '
            + (str("%.2f" % (float(' '.join(map(str, B_bal))))))
            + ' BIS'
        )
        print(
            'USD Reward Balance: ' + ' '.join(map(str, USD_bal))
        )
        print(" ")
        print(
            'Current blockheight is: ' + ' '.join(map(str, Blockheight))
        )
        print(
            'Avg. weekly payout in BIS is: ' + ' '.join(map(str, W_hnreward))
            + ' BIS'
        )
        USD_payout()
        print(
            'Annual ROI is: ' + Hn_ROI + '%'
        )
        print(" ")
        print('---------------------------------------------------')
        print(" ")
    else:
        print(" ")
        print('---------------------------------------------------')
        print(" ")
        print('\033[1m' + "Status Hypernode: Active" + "\033[0m ")
        search_height()
        print(
            'Current blockheight is: ' + ' '.join(map(str, Blockheight))
        )
        print(" ")
        BIS_price()
        print(" ")
        print(
            'BIS Reward Balance: '
            + (str("%.2f" % (float(' '.join(map(str, B_bal))))))
            + ' BIS'
        )
        print(
            'USD Reward Balance: ' + ' '.join(map(str, USD_bal))
        )
        print(" ")
        print(
            'Avg. weekly payout in BIS is: ' + ' '.join(map(str, W_hnreward))
            + ' BIS'
        )
        USD_payout()
        print(
            'Annual ROI is: ' + Hn_ROI + '%'
        )
        print(" ")
        print('---------------------------------------------------')
        print(" ")
    break
