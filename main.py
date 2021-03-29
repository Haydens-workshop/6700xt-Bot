import PySimpleGUI as sg
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.chrome.options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import re
import time
import os
import shutil


PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-user-media-security=true")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(PATH, options=options)
action = ActionChains(driver)

event, values = sg.Window('AMD BUYER BOT(Type all information for your bestbuy acct!)',
                  [[sg.T('Enter Your First Name'), sg.In(key='-ID-')],
                  [sg.T('Enter your Last name'), sg.In(key='-ID-1')],
                  [sg.T('Enter your Best Buy Email'), sg.In(key='-ID-2')],
                   [sg.T('Enter your Best Buy Password'), sg.In(key='-ID-3')],
                  [sg.T('Enter your Credit Card CVV'), sg.In(key='-ID-4')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

first_Name = values['-ID-']
last_Name=values['-ID-1']
email=values['-ID-2']
password=values['-ID-3']
cvv=values['-ID-4']



driver.get("https://www.bestbuy.com/site/xfx-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-gray-black/6457624.p?skuId=6457624")


driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
time.sleep(3)
element = driver.find_element_by_class_name('add-to-cart-button')
a=1
while a==1:
    element = driver.find_element_by_class_name('add-to-cart-button')
    data = element.is_enabled()
    if data == True:
        element.click()
        time.sleep(3)
        driver.get("https://www.bestbuy.com/cart")
        time.sleep(2)
        driver.find_element_by_xpath("//*[contains(text(), 'Checkout')]").click()
        time.sleep(3)
        email = driver.find_element_by_id("fld-e")
        password= driver.find_element_by_id("fld-p1")

        email.send_keys(email)
        password.send_keys(password)
        driver.find_element_by_class_name("btn-secondary").click()
        time.sleep(5)
        driver.find_element_by_class_name("ispu-card__switch").click()
        time.sleep(6)
        driver.find_element_by_xpath("//*[contains(text(), 'Continue to Payment Information')]").click()
        time.sleep(6)
        #final payment page
        cvv= driver.find_element_by_id("credit-card-cvv")
        cvv.send_keys(cvv)
        time.sleep(3)
        driver.find_element_by_class_name('btn-primary').click()
        a=2
    else:
        time.sleep(420)
        driver.get("https://www.bestbuy.com/site/xfx-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-gray-black/6457624.p?skuId=6457624")
        try:
            time.sleep(5)
            driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
            time.sleep(3)
            element = driver.find_element_by_class_name('add-to-cart-button')
        except:
            pass