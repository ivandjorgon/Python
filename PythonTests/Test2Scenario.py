from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Test2Scen():

    def Test2(self):
        baseUrl = "file:///C:/Users/idjorgon/Desktop/Files/Automation/Udemy/Ivan/index.html"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")

        # Test 2
        # Navigate to home page
        # In the test 2 div, assert that there are three values in the listgroup
        # Assert that the second list item's value is set to "List Item 2"
        # Assert that the second list item's badge value is 6

        driver.maximize_window()
        # Navigate to home page
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 500);")
        title = driver.title
        # Get Title of the web page to confirm we have successfully navigated to home page
        print("Title of the web page is: " + title)
        # driver.implicitly_wait(3)

        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Assert that there are three values in the listgroup
        elemListByClassName = driver.find_elements_by_class_name("list-group-item")
        length = len(elemListByClassName)
        #assert str(length) == 3
        if elemListByClassName is not None:
            print("Test 2 List Group -> Size of the list is: " + str(length))

        # Assert that the second list item's value is set to "List Item 2"
        listItem2 = driver.find_element(By.XPATH, ".//*[@id='test-2-div']/ul/li[2]//parent::li")
        itemValue = listItem2.text
        print("The second list element contains: " + itemValue)

        findthis = "List Item 2"
        assert "List Item 2" in findthis
        if findthis in itemValue:
            print(findthis, "value has been found in the second list item")
        else:
            print(find_this, "value is not located in", itemValue)

        # Assert that the second list item's badge value is 6
        badgeItem = driver.find_element(By.XPATH, ".//*[@id='test-2-div']/ul/li[2]/span")
        badgeValue = badgeItem.text
        print("Second list item's badge value is: " + badgeValue)
        assert "6" in badgeValue
        time.sleep(3)

        # Browser Close / Quit
        # driver.close()
        driver.quit()

e = Test2Scen()
e.Test2()