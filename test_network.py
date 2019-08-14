from appium import webdriver
import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
class TestNetwork:
    def setup(self):
        self.driver = init_driver()
    def test_mobile_network_2g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'滑动')]").click()


    def teardown(self):
        self.driver.quit()








