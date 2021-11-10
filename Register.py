import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = "test5@testmail.com"
fname = "ABC"
lname= "DEF"
password = "123456789test"
company = "ABC CO"
address = "First Street N 17, 34123 Kadıköy/İstanbul"
city = "İstanbul"
ZIP = "34123"
mobile = "+9012344567890"
addressname = "Company Address"
day = "1"
month = "January"
year = "1990"
state = "Wisconsin"

driver = webdriver.Chrome("C:\\Users\esame\OneDrive\Masaüstü\Samet Çolak\Testing\chromedriver.exe")
driver.maximize_window()
driver.get("http://automationpractice.com")

driver.find_element_by_xpath("/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()
time.sleep(1)

element = driver.find_element_by_id("email_create").send_keys(email)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[3]/button/span").click()
time.sleep(3)

driver.find_element_by_css_selector("input#id_gender1").click()

element = driver.find_element_by_id("customer_firstname").send_keys(fname)
time.sleep(1)

element = driver.find_element_by_id("customer_lastname").send_keys(lname)
time.sleep(1)

element = driver.find_element_by_id("passwd").send_keys(password)
time.sleep(1)

driver.find_element_by_id("days").send_keys(day)
driver.find_element_by_id("months").send_keys(month)
driver.find_element_by_id("years").send_keys(year)
time.sleep(1)

driver.find_element_by_id("newsletter").click()
driver.find_element_by_id("optin").click()
time.sleep(1)

"""
element = driver.find_element_by_id("firstname").send_keys(fname)
time.sleep(1)

element = driver.find_element_by_id("lastname").send_keys(lname)
time.sleep(1)
"""

element = driver.find_element_by_id("company").send_keys(company)
time.sleep(1)

element = driver.find_element_by_id("address1").send_keys(address)
time.sleep(1)

element = driver.find_element_by_id("city").send_keys(city)
time.sleep(1)

driver.find_element_by_id("id_country").send_keys("United States")
driver.find_element_by_id("id_state").send_keys(state)
time.sleep(1)

element = driver.find_element_by_id("postcode").send_keys(ZIP)
time.sleep(1)

element = driver.find_element_by_id("phone_mobile").send_keys(mobile)
time.sleep(1)

element = driver.find_element_by_id("alias").clear()
element = driver.find_element_by_id("alias").send_keys(addressname)
time.sleep(1)

element = driver.find_element_by_id("submitAccount").click()
time.sleep(5)

driver.close()