from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
import time
#from selenium.webdriver.support.select import Select
# Import test6Method
from PythonTests.Test6Method import test6Method

class Test6Scen():

    def Test6(self):
        baseUrl = "file:///C:/Users/idjorgon/Desktop/Files/Automation/Udemy/Ivan/index.html"
        driver = webdriver.Chrome("C:/Users/idjorgon/node_modules/chromedriver/lib/chromedriver/chromedriver.exe")

        # Test 6
        # Navigate to home page
        # Write a method that allows you to find the value of any cell on the grid
        # Use the method to find the value of the cell at coordinates 2, 2 (staring at 0 in the top left corner)
        # Assert that the value of the cell is "Ventosanzap"

        driver.maximize_window()
        hw = test6Method(driver)
        # Navigate to home page
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1400);")
        title = driver.title
        # Get Title of the web page to confirm we have successfully navigated to home page
        print("Title of the web page is: " + title)
        # driver.implicitly_wait(3)
        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Call the method to find the value of the cell at coordinates 3, 3
        # Which is the same as 2, 2 (starting at 1 instead in the top left corner)
        elementResult = hw.getElement("3", "3")
        # Confirm and assert that the value of the cell we got is Ventosanzap
        print("The value of the cell is: " + elementResult)

        # Additional tests just to test and confirm the method correctness
        elementResult = hw.getElement("2", "2")
        # This should print out and return Carswell
        print("The value of the cell is: " + elementResult)
        elementResult = hw.getElement("1", "3")
        # This should print out and return Cardguard
        print("The value of the cell is: " + elementResult)
        time.sleep(7)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = Test6Scen()
e.Test6()