from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
import time

class ChromeTests():

    def Tests(self):
        baseUrl = "file:///C:/Users/idjorgon/Desktop/Files/Automation/Udemy/Ivan/index.html"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")

        # Test 1
        # Navigate to home page
        # Assert that both the email and password inputs are present as well as the login button
        # Enter in an email address and password combination into the respective fields

        driver.maximize_window()
        # Navigate to home page
        driver.get(baseUrl)
        title = driver.title
        # Get Title of the web page to confirm we have successfully navigated to home page
        print("Title of the web page is: " + title)
        driver.implicitly_wait(3)

        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        emailField = driver.find_element(By.ID, "inputEmail")
        if emailField is not None:
            print("Email input is present - located by its unique ID")
        emailField.send_keys("ivan@emailtest.com")

        passField = driver.find_element(By.ID, "inputPassword")
        if passField is not None:
            print("Password input is present - located by its unique ID")
        passField.send_keys("password")

        signinLogin = driver.find_element(By.CLASS_NAME, "btn-block")
        if signinLogin is not None:
            print("Sign in login button is present - located by its unique class name")
        signinCaption = signinLogin.text
        # Get Text of the Sign in button to confirm we have found and located the correct login button
        print("Text on Sign in button: " + signinCaption)

        time.sleep(3)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = ChromeTests()
e.Tests()