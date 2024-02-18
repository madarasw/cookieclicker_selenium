# Automate the online game cookieclicker >> https://orteil.dashnet.org/experiments/cookie/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# constants
CHECK_DURATION = 10
MINUTES = 5

# init and config the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# go to page
url = 'https://orteil.dashnet.org/experiments/cookie/'
driver.get(url)

# get hold of useful elements
cookie = driver.find_element(By.ID, value="cookie")

break_time = time.time() + CHECK_DURATION
print(break_time)
cps = 0

loop_count = (MINUTES*60)/CHECK_DURATION # run game for 5 minutes
for i in range(loop_count):
    # while loop to click on cookie as much as possible
    while True:
        cookie.click()
        current_time = time.time()

        # check for the available upgrades every 10(CHECK_DURATION) seconds
        if current_time >= break_time:
            break_time += CHECK_DURATION

            # buy the unlocked best option
            store = driver.find_element(By.ID, value="store")
            all_items = store.find_elements(By.TAG_NAME, value="div")
            for item in all_items[::-1]:
                if item.get_attribute('class') != 'grayed':
                    item.click()
                    break
            break

# print the final cookies per second
cps = driver.find_element(By.ID, value="cps")
print(cps.text)

# close the tab
driver.close()
