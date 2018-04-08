from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class manyelements():

    def elem_test(self):
        baseUrl = "https://www.ultimateqa.com/simple-html-elements-for-automation/"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        title = driver.title
        assert "HTML" in driver.title
        print("Title of the main web page is: " + title)

        clickMe = driver.find_element(By.ID, "button1")
        clickMe.click()

        title2 = driver.title
        print("Second title is: " + title2)
        assert "QA" in driver.title
        driver.back()

        clickMe2 = driver.find_element(By.ID, "button2")
        clickMe2.click()

        title3 = driver.title
        assert "QA" in driver.title
        print("Third title is: " + title3)
        driver.back()

        assert title2 == title3
        assert title != title2

ccc = manyelements()
ccc.elem_test()