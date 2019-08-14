import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from display_page分离测试脚本 import DisplayPage
class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.display = DisplayPage(self.driver)
    def test_mobile_display(self):
        self.display.closedd()
        # self.driver.find_element_by_xpath("//*[contains(@text,'打开')]").click()
    def teardown(self):
        self.driver.quit()
#







