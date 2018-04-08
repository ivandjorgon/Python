from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
import time
#from selenium.webdriver.support.select import Select

class Test5Scen():

    def Test5(self):
        baseUrl = "file:///C:/Users/idjorgon/Desktop/Files/Automation/Udemy/Ivan/index.html"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")

        # Test 5
        # Navigate to home page
        # In the test 5 div, wait for a button to be displayed (note: the delay is random) and then click it
        # Once you've clicked the button, assert that a success message is displayed
        # Assert that the button is now disabled

        driver.maximize_window()
        # Navigate to home page
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")
        title = driver.title
        # Get Title of the web page to confirm we have successfully navigated to home page
        print("Title of the web page is: " + title)
        # driver.implicitly_wait(3)
        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # In the test 5 div, wait for the button to be displayed (note: it seems the delay does not exceed 10 seconds) and then click it
        # Math.random() returns a value in the range [0, 1). 0 is included but 1 is excluded (the range is: 0 to 0.999999...)
        # time sleep it for 11 secs
        time.sleep(11)
        test5Button = driver.find_element(By.XPATH, ".//*[@id='test5-button']")
        # Assert that the button is now enabled
        print("The button is now enabled and set to: " + str(test5Button.is_enabled()))
        test5Button.click()
        alertElement = driver.find_element(By.XPATH, ".//*[@id='test5-alert']")
        message = alertElement.text
        print("Success message is correctly displayed as follows: " + message)
        # Assert that the button is now disabled
        print("The button is now disabled and is therefore set to: " + str(test5Button.is_enabled()))
        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = Test5Scen()
e.Test5()