import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestPomotodo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def wait_for_xpath(self, xpath, *, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))

    def test_signup(self):
        username = 'selenium.pomotodo.com' + str(int(time.time()))

        driver = self.driver
        driver.get('https://www.pomotodo.com')

        button_signup = driver.find_element_by_xpath(
            '/html/body/div[1]/div/ul/li[6]/a')
        button_signup.click()

        input_username = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/form/div[1]/span/input[2]')
        input_email = driver.find_element_by_xpath('//*[@id="js-email"]')
        input_password = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/form/div[3]/input')
        input_username.send_keys(username)
        input_email.send_keys(username + '@zzz.com')
        input_password.send_keys('aaaaaaa')
        input_password.submit()

        button_cancel_tutorial = self.wait_for_xpath(
            '/html/body/div[9]/div/div/div[2]/button[2]')
        button_cancel_tutorial.click()

        button_profile = driver.find_element_by_xpath(
            '/html/body/header/ul/li[3]/a')
        assert button_profile.is_enabled()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
