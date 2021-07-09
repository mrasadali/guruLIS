import time

from Page_Object.Sample_Transits import SampleTransit
from Utilities.BaseClass import BaseClass


class TestCase4(BaseClass):
    def test_testCase4(self):
        self.login()
        self.driver.get("https://mla-test.azurewebsites.net/Pages/Reports/Labs/LabsSamplesInTransit.aspx")
        sample_transit = SampleTransit(self.driver)
        samples_data = self.driver.find_elements_by_xpath("//table[@class='grid100 table']/tbody/tr[*]/td[4]")
        print(len(samples_data))
        for items in samples_data:
            requisition_id = items.find_element_by_xpath("//*[@id='ContentPlaceHolder1_gvOrderedLabs']/tbody/tr[183]/td[4]").text
            if requisition_id == "17187":
                print(requisition_id)
                break

            else:
                print("The data is not found")
                break

        sample_transit.get_generate_report()
        time.sleep(5)