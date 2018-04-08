from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class UltimateQA(unittest.TestCase):

    def test(self):
        baseUrl = "https://courses.ultimateqa.com/users/sign_in"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        title = driver.title
        self.assertTrue(title)
        print("Title of the web page is: " + title)

        emailField = driver.find_element(By.ID, "user_email")
        self.assertIsNotNone(emailField)
        self.assertTrue(emailField)
        emailField.send_keys("admintest@test.com")

        passwordField = driver.find_element(By.ID, "user_password")
        self.assertIsNotNone(passwordField)
        passwordField.send_keys("adminpassword")

        signInButton = driver.find_element(By.ID, "btn-signin")
        signInButton.click()

        notificationHeader = driver.find_element(By.XPATH, "//div[@id='notifications']/div[@class='row']//p[@class='message-text']")
        notificationRedMsg = driver.find_element(By.XPATH, "//div[@id='notifications-error']//li[@class='notifications-error__list-item']")
        self.assertIsNotNone(notificationHeader)
        self.assertTrue(notificationRedMsg)
        print("Value of Red Message Notification: " + str(notificationRedMsg))

chrometest = UltimateQA()
chrometest.test()