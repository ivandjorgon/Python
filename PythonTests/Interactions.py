from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Login to Vancouver QA environment
class PureFactsLogin():

    def loginTest(self):
        baseUrl = "http://vancouver.qa/"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")

        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(baseUrl)
        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)
        # Wait a little bit
        driver.implicitly_wait(5)

        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Find Username field by ID, and populate it with Correct Username
        usernameField = driver.find_element(By.ID, "textfield-1025-inputEl")
        usernameField.send_keys("pfadmin")
        # Find Password field by ID, and populate it with Correct Password
        passwordField = driver.find_element(By.ID, "textfield-1026-inputEl")
        passwordField.send_keys("password")
        # Login to application
        loginLink = driver.find_element(By.ID, "button-1030-btnWrap")
        loginLink.click()

        time.sleep(3)
        # Click on Add New Contact button
        # addContact = driver.find_element(By.ID, "button-1016-btnInnerEl")
        # addContact.click()

        # Find Add New Contact element by ID, in order to confirm successful login
        addContactById = driver.find_element_by_id("button-1016-btnInnerEl")
        if addContactById is not None:
            print("We found the Add New Contact button element")

        # Find Welcome PureFacts Admin Message in order to confirm successful login
        elementById = driver.find_element_by_id("label-2352")
        if elementById is not None:
            print("We found the Welcome Admin Message")

        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)
        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        time.sleep(8)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

chromeTest = PureFactsLogin()
chromeTest.loginTest()