
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Dropdown(unittest.TestCase):
    dropdown_class = (By.ID, 'coding-language-select')
    dropdown_css = (By.ID, "dropdownMenuButton")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/dropdown")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_select_using_class(self):
        my_dropdown = self.driver.find_element(*self.dropdown_class)
        dropdown_object = Select(my_dropdown)
        dropdown_object.select_by_value('Python')


