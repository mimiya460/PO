from appium import webdriver
import os,sys

from selenium.webdriver.common.by import By
#到模块快捷键alt+enter

sys.path.append(os.getcwd())
from base.base_driver import init_driver
class DisplayPage():
    def __init__(self,driver):
        self.driver = init_driver()
    def anquan_click(self):
        #self.driver.find_element_by_xpath("").click()
        self.driver.find_element(By.XPATH,"//*[contains(@text,'安全')]")
    def pingmusd_click(self):
        self.driver.find_element(By.XPATH, "//*[contains(@text,'屏幕锁定')]")
        #self.driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
    def huadong_click(self):
        self.driver.find_element(By.XPATH, "//*[contains(@text,'滑动')]")
        #self.driver.find_element_by_xpath("//*[contains(@text,'滑动')]").click()
