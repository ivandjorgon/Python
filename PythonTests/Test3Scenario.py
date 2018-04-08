from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
#from selenium.webdriver.support.select import Select

class Test3Scen():

    def Test3(self):
        baseUrl = "file:///C:/Users/idjorgon/Desktop/Files/Automation/Udemy/Ivan/index.html"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")

        # Test 3
        # Navigate to home page
        # In the test 3 div, assert that "Option 1" is the default selected value
        # Select "Option 3" from the select list

        driver.maximize_window()
        # Navigate to home page
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 700);")
        title = driver.title
        # Get Title of the web page to confirm we have successfully navigated to home page
        print("Title of the web page is: " + title)
        # driver.implicitly_wait(3)

        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # In the test 3 div, assert that "Option 1" is the default selected value
        element = driver.find_element_by_id("dropdownMenuButton")
        defaultSelected = element.text
        print("The default selected value in test 3 div is: " + defaultSelected)

        # Select "Option 3" from the select list and confirm it's been selected
        element.click()
        elementOpt3 = driver.find_element(By.XPATH, ".//*[@id='test-3-div']/div/div/a[3]")
        elementOpt3.click()
        option3 = element.text
        print("We successfully selected: " + option3)

        time.sleep(9)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = Test3Scen()
e.Test3()