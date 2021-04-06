from selenium.webdriver.common.by import By

from Page_Object.Common import Common


class SampleTransit(Common):
    generate_report = (By.XPATH, "//*[@id='placeholder']/table[1]/tbody/tr/td[2]/a")

    def __init__(self, driver):
        self.driver = driver

    def get_generate_report(self):
        return self.execute_script(self.generate_report)