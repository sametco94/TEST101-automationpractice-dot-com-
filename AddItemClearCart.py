import time
import random
from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver.exe")

driver.maximize_window()
driver.get("http://automationpractice.com")
time.sleep(2)

elems = driver.find_elements_by_class_name("ajax_add_to_cart_button")
links = []

for link in elems:
    a = link.get_attribute("href")
    links.append(a)

for i in range(4):
    driver.get(random.choice(links))
    time.sleep(1)
    driver.find_element_by_id("header_logo").click()
    time.sleep(1)

driver.get("http://automationpractice.com/index.php?controller=order")
time.sleep(2)

clear_elem = driver.find_elements_by_class_name("clear_cart")
check = len(clear_elem)
items = driver.find_elements_by_class_name("icon-trash")
remover = len(items)

if check <= 0:
    print("Clear Cart option does not exist!")
    for i in range(remover):
        driver.find_element_by_class_name("icon-trash").click()
        time.sleep(2)
else:
    driver.get(clear_cart)

print("Shopping cart is successfully cleared")
driver.find_element_by_id("header_logo").click()
time.sleep(1)

driver.close()