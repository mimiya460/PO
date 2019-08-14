from appium import webdriver
import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
class TestDisplay:
    def setup(self):
        self.driver = init_driver()
    def test_mobile_display(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'关闭')]").click()

    def teardown(self):
        self.driver.quit()








