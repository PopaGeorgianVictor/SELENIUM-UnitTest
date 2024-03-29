
import unittest
import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



class Search(unittest.TestCase):

    SEARCH_BAR = (By.ID,"myInput")
    ELEM = (By.LINK_TEXT, "LISTS")


    def setUp(self) -> None:
        self.driver =  webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/search_bar")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('lists')
        elem = self.driver.find_element(*self.ELEM)
        actual_search = elem.text
        expected_search = "LISTS"
        assert actual_search == expected_search, f'Error: expected: {expected_search}, actual: {actual_search}'

    def test_click(self):
        self.driver.find_element(*self.ELEM).click()
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(By.CSS_SELECTOR, "a[title='Python Tutorial']")
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))