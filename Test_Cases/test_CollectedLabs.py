import time

from Page_Object.Collected_Labs import CollectedLabs
from Utilities.BaseClass import BaseClass


class TestCase1(BaseClass):
    def test_case3(self):
        self.login()
        self.driver.get("https://mla-test.azurewebsites.net/Pages/Appointment/CollectedLabSampleReceiving.aspx")
        collect_lab = CollectedLabs(self.driver)
        # collect_lab.get_search_specimen()
        # time.sleep(3)
        collect_lab.get_print_sample()
        collect_lab.get_patient_name()
        collect_lab.get_search_button()
        time.sleep(5)