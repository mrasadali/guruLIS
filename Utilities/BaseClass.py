import pytest
from selenium.webdriver.common.by import By
from Page_Object.Common import Common


@pytest.mark.usefixtures("setup")
class BaseClass(Common):
    username = "hmeghani"
    password = "Axg@1101"
    role_selection = (By.XPATH, "//input[@id='SelectRole1_btnSelectRole']")
    # state_patient_loop = "//select[@class='ddlState']/option"
    selected_diagnosis_text = "A01.0"

    def login(self):
        self.driver.find_element(By.ID, "Login1_txtUserName").send_keys(self.username)
        self.driver.find_element(By.ID, "Login1_txtPassword").send_keys(self.password)
        self.driver.execute_script("document.getElementById('Login1_btnLogin').removeAttribute('disabled')")
        self.driver.find_element(By.ID, "Login1_btnLogin").click()
        element = self.driver.find_element(*self.role_selection)
        return self.driver.execute_script("arguments[0].click();", element)

    def check_availibility_of_element(self, variable):
        if len(variable) == 0:
            print("Test case failed")
        else:
            print("Test Case Passed")

    # Two ways to assert the text
    def asserting_the_text(self, text, variable):
        if text in variable:
            print("Successfully Asserted")
        else:
            print("String is not present")

    def check_the_assertion(self, text, variable):
        assert text in variable

    # def get_current_url(self):
    #    self.driver.current_url
