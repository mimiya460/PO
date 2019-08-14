from appium import webdriver
import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
class DisplayPage():
    def __init__(self,driver):
        self.driver = init_driver()
    def closedd(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'打开')]").click()
