from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Common:

    def onclick(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).click()

    def sendkey(self, locator, value):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_title(self, title):
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        return self.driver.title

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_elements_text(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(locator))
        return element.text

    def execute_script(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].click();", element)

    def execute_script(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].click();", element)

    def dropdown_by_text(self, locator, text):
        select = Select(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)))
        return select.select_by_visible_text(text)

    def dropdown_by_index(self, locator, index):
        select = Select(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)))
        return select.select_by_index(index)

    def dropdown_by_value(self, locator, value):
        select = Select(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)))
        return select.select_by_visible_text(value)
