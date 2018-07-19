import unittest
from selenium import webdriver
from registration_step import *
from selenium.webdriver.support.wait import WebDriverWait


class RegTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Drivers/chromedriver.exe")
        self.base_url = "http://test.stage/"
        self.driver.get(self.base_url)
        self.wait = WebDriverWait(self.driver, 10)

    def test_registration_valid(self):
        registration(self.driver)
        #self.assertTrue(is_user_created(self.driver))

    def test_registration_invalid_mail(self):
        registration(self.driver, email="qwerty")
        self.assertTrue(help_block(self.driver))

    def test_registration_invalid_first_name(self):
        registration(self.driver, first_name=" ")
        self.assertTrue(help_block(self.driver))

    def test_registration_invalid_last_name(self):
        registration(self.driver, last_name=" ")
        self.assertTrue(help_block(self.driver))

    def tearDown(self):
        self.driver.close()
