from selenium import webdriver


class FindByLinkText():

    def test123(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome("C:/Users/idjorgon/PycharmProjects/libs/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)

        #title = driver.title
        #print("Title of the web page is: " + title)
        assert "Kode" in driver.title

        driver.implicitly_wait(5)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")

ff = FindByLinkText()
ff.test123()