# from appium import webdriver
# class TestSetting:
#     def setup(self):
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '4.4'
#         desired_caps['deviceName'] = '127.0.0.1:62001'
#         desired_caps['appPackage'] = 'com.android.settings'
#         desired_caps['appActivity'] = '.Settings'
#         #解决输入中文
#         desired_caps['unicodekeyboard'] = True
#         desired_caps['resetKeyboard'] = True
#         #声明Driver对象
#         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#
#     def test_mobile_network_2g(self):
#         self.driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'滑动')]").click()
#
#     def test_mobile_display(self):
#         self.driver.find_element_by_xpath("//*[contains(@text,'打开')]").click()
#
#
#     def teardown(self):
#         self.driver.quit()








