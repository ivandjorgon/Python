from selenium.webdriver.common.by import By

# This class contains the getElement method
class test6Method():

    def __init__(self, driver):
        self.driver = driver

    # Method that allows us to find the value of any cell on the test 6 div grid
    def getElement(self, row, column):
        element = None
        # Build an XPath depending on the values
        locator = "//*[@id='test-6-div']/div/table/tbody/tr[" + row + "]/td[" + column + "]"
        element = self.driver.find_element(By.XPATH, locator)
        return element.text

