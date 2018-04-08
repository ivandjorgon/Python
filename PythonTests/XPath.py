from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class XPath(unittest.TestCase):

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        #driver.execute_script("window.scrollBy(0, 700);")
        title = driver.title
        self.assertTrue(title)
        print("Title of the web page is: " + title)
        coursePrice = driver.find_element(By.XPATH, ".//table[@id='product']//td[.='30']")
        # coursePrice = driver.find_element(By.XPATH, ".//table[@id='product']//td[text()='Python Programming Language']//following-sibling::td")
        self.assertEqual('30', coursePrice.text)
        self.assertNotEqual('31', coursePrice.text)
        self.assertIsNotNone(coursePrice.text)
        print("The price for the course is: " + coursePrice.text)

        checkbox0 = driver.find_element(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label[1]")
        label0 = checkbox0.text
        print("Checkbox: " + label0)
        checkbox1 = driver.find_element(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label[2]")
        label1 = checkbox1.text
        print("Checkbox: " + label1)

ff = XPath()
ff.test()