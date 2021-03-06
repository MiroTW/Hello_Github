import os
import time
import unittest
from selenium import webdriver

class singin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get('https://www.104.com.tw/jobs/main/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def Login(self):
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').click()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submitBtn').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[5]/a').is_displayed()

        if 'snoopy099' == password:
            print("password is same")
        else:
            print("password is different")

    #login test
    def test_01(self):
        self.Login()

if __name__ == '__main__':
    unittest.main()
