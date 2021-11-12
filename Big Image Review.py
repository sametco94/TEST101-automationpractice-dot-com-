import time
import random
from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver.exe")

driver.maximize_window()
driver.get("http://automationpractice.com")
time.sleep(2)

elems = driver.find_elements_by_class_name("product_img_link")
products = []

for item in elems:
    a = item.get_attribute("href")
    products.append(a)

print(products)

for i in range(2):
    driver.get(random.choice(products))
    time.sleep(1)
    photos = driver.find_elements_by_class_name("img-responsive")
    check = len(photos) - 2
    driver.find_element_by_id("view_full_size").click()
    time.sleep(1)
    for i in range(check):
        driver.find_element_by_class_name("fancybox-next").click()
        time.sleep(1)
    driver.find_element_by_class_name("fancybox-close").click()
    time.sleep(1)
    driver.find_element_by_id("header_logo").click()
    time.sleep(1)

driver.close()