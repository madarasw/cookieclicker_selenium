import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHECK_DURATION = 10
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://orteil.dashnet.org/experiments/cookie/'
driver.get(url)

cookie = driver.find_element(By.ID, value = "cookie")

store = driver.find_element(By.ID, value="store")
all_items = store.find_elements(By.TAG_NAME, value="div")

break_time = time.time() + CHECK_DURATION
print(break_time)
cps = 0
for i in range(60):
    while True:
        cookie.click()
        current_time = time.time()
        if current_time >= break_time:
            break_time += CHECK_DURATION
            store = driver.find_element(By.ID, value="store")
            all_items = store.find_elements(By.TAG_NAME, value="div")
            for item in all_items[::-1]:
                if item.get_attribute('class') != 'grayed':
                    item.click()
                    break
            break

cps = driver.find_element(By.ID, value="cps")
time.sleep(5)
print(cps.text)
driver.close()
