from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Sliders():

    def test1(self):
        baseUrl = "https://jqueryui.com/slider/"
        #driver = webdriver.Firefox()
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 300, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")

    def check(self, percent):
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")
        driver.get("http://jqueryui.com/demos/slider/");
        driver.switch_to_frame(0)
        driver.switch_to_active_element()

        slidebar = driver.find_element_by_id("slider")
        height = slidebar.size['height']
        width = slidebar.size['width']

        move = ActionChains(driver);
        slider = driver.find_element_by_xpath("//div[@id='slider']/a")

        if width > height:
            move.click_and_hold(slider).move_by_offset(percent * width / 100, 0).release().perform()
        else:
            move.click_and_hold(slider).move_by_offset(percent * height / 100, 0).release().perform()

        driver.switch_to_default_content()

ff = Sliders()
ff.test1()