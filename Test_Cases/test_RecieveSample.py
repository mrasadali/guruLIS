import time

from Page_Object.Recieve_Sample import RecieveSample
from Utilities.BaseClass import BaseClass


class TestCase1(BaseClass):
    def test_case3(self):
        self.login()
        self.driver.get("https://mla-test.azurewebsites.net/Pages/Appointment/CollectedLabSampleReceiving.aspx")
        recieve_sample = RecieveSample(self.driver)
        # recieve_sample.get_search_specimen()
        # # time.sleep(3)
        #
        # recieve_sample.get_patient_name()
        # recieve_sample.get_search_button()
        # recieve_sample.get_print_sample()
        check = recieve_sample.get_specimen_recieved()
        print(check)
        time.sleep(5)