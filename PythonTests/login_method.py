from selenium.webdriver.common.by import By

# This class contains the getElement method
class login_method():

    def __init__(self, driver):
        self.driver = driver

    # Method that allows us to find the value of any cell on the test 6 div grid
    def login_method(self, row, column):
        # Find Username field by ID, and populate it with Correct Username
        usernameField = driver.find_element(By.ID, "textfield-1025-inputEl")
        usernameField.send_keys("admin")
        # Find Password field by ID, and populate it with Correct Password
        passwordField = driver.find_element(By.ID, "textfield-1026-inputEl")
        passwordField.send_keys("password")
        # Login to application
        loginLink = driver.find_element(By.ID, "button-1030-btnWrap")
        loginLink.click()
        time.sleep(3)

