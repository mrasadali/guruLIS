from selenium.webdriver.common.by import By

from Page_Object.Common import Common


class RecieveSample(Common):
    specimen_id = (By.ID, "ContentPlaceHolder1_txtSpecimenId")
    patient_name = (By.ID, "ContentPlaceHolder1_txtReceiveLabPatName")
    search_button = (By.ID, "ContentPlaceHolder1_btnReceiveLabSearch")
    print_samples = (By.XPATH, "//*[@id='ContentPlaceHolder1_gvReceiveResult_lnkprintlabel_0']/i")
    specimen_recieved = (By.XPATH,"//*[@id='placeholder']/table[2]/tbody/tr/td/table/tbody/tr[4]/td[6]")

    def __init__(self, driver):
        self.driver = driver

    def get_search_specimen(self):
        return self.sendkey(self.specimen_id, "24285")

    def get_patient_name(self):
        return self.sendkey(self.patient_name, "North")

    def get_search_button(self):
        return self.execute_script(self.search_button)

    def get_print_sample(self):
        return self.execute_script(self.print_samples)

    def get_specimen_recieved(self):
        return self.get_element_text(self.specimen_id)