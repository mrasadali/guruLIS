from selenium.webdriver.common.by import By

from Page_Object.Common import Common


class CollectedLabs(Common):
    specimen_id = (By.ID, "ContentPlaceHolder1_txtSpecimenId")
    patient_name = (By.XPATH, "//*[@id='ContentPlaceHolder1_txtReceiveLabPatName']")
    search_button = (By.ID, "ContentPlaceHolder1_btnReceiveLabSearch")
    print_samples = (By.XPATH, "//*[@id='ContentPlaceHolder1_gvReceiveDate_lnkprintlabel_0']/i")

    def __init__(self, driver):
        self.driver = driver

    def get_search_specimen(self):
        return self.sendkey(self.specimen_id, "24284")

    def get_patient_name(self):
        return self.sendkey(self.patient_name, "North")

    def get_search_button(self):
        return self.execute_script(self.search_button)

    def get_print_sample(self):
        return self.execute_script(self.print_samples)