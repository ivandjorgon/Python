from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
#from selenium.webdriver.support.select import Select
# Import test6Method
from PythonTests.Test6Method import test6Method

class Exercise18():

    def exec18(self):
        baseUrl = "https://www.airbnb.com/"
        driver = webdriver.Chrome("C:/Users/idjorgon/node_modules/chromedriver/lib/chromedriver/chromedriver.exe")

        driver.maximize_window()
        # Navigate to home page
        driver.get(baseUrl)
        # driver.execute_script("window.scrollBy(0, 1400);")
        title = driver.title
        # Get Title of the web page to confirm we have successfully navigated to home page
        print("Title of the web page is: " + title)
        driver.implicitly_wait(20)
        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        searchField = driver.find_element(By.NAME, "location")
        if searchField is not None:
            print("Search field is present")
        searchField.send_keys("Porto")

        #searchButton = driver.find_element(By.CLASS_NAME, "_vuq6rr")
            #if searchButton is not None:
                #print("Search button is present - located by its unique Class Name")
        #searchButton.click()

        time.sleep(8)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = Exercise18()
e.exec18()