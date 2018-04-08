from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ElementState():

    def isEnabled(self):
        baseUrl = "http://www.google.com/"
        driver = webdriver.Chrome("C:/Users/idjorgon/node_modules/chromedriver/lib/chromedriver/chromedriver.exe")

        driver.maximize_window()
        driver.get(baseUrl)
        title = driver.title
        print("Title of the web page is: " + title)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_id("gs_htif0")
        e1State = e1.is_enabled()
        print("E1 is Enabled? -> " + str(e1State))

        e2 = driver.find_element_by_id("gs_taif0")
        e2State = e2.is_enabled()
        print("E2 is Enabled? -> " + str(e2State))

        e3 = driver.find_element_by_id("lst-ib")
        e3State = e3.is_enabled()
        print("E3 is Enabled? -> " + str(e3State))

        e3.send_keys("letskodeit")

        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = ElementState()
e.isEnabled()