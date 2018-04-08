from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
#from selenium.webdriver.support.select import Select

class Test4Scen():

    def Test4(self):
        baseUrl = "file:///C:/Users/idjorgon/Desktop/Files/Automation/Udemy/Ivan/index.html"
        driver = webdriver.Chrome("C:/Users/idjorgon/node_modules/chromedriver/lib/chromedriver/chromedriver.exe")

        # Test 4
        # Navigate to home page
        # In the test 4 div, assert that the first button is enabled and that the second button is disabled

        driver.maximize_window()
        # Navigate to home page
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 800);")
        title = driver.title
        # Get Title of the web page to confirm we have successfully navigated to home page
        print("Title of the web page is: " + title)
        # driver.implicitly_wait(3)

        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Assert and print out that the first button is enabled and that the second button is disabled
        firstButton = driver.find_element(By.XPATH, ".//*[@id='test-4-div']/button[1]")
        e1State = firstButton.is_enabled()
        print("In the test 4 div, is the First Button Enabled? -> " + str(e1State))

        secondButton = driver.find_element(By.XPATH, ".//*[@id='test-4-div']/button[2]")
        e2State = secondButton.is_enabled()
        print("In the test 4 div, is the Second Button Enabled? -> " + str(e2State))

        time.sleep(3)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = Test4Scen()
e.Test4()