import time

from Page_Object.Sample_Transits import SampleTransit
from Utilities.BaseClass import BaseClass


class TestCase4(BaseClass):
    def test_testCase4(self):
        self.login()
        print("Logged In")
        self.driver.get("https://mla-test.azurewebsites.net/Pages/Reports/Labs/LabsSamplesInTransit.aspx")
        sample_transit = SampleTransit(self.driver)
        # sam= self.driver.find_elements_by_xpath("//td[contains(text(),'BRIDGES, MONA')]")
        # print(sam)
        samples_data = self.driver.find_elements_by_xpath("//table[@class='grid100 table']/tbody/tr[*]/td[2]")
        print(len(samples_data))
        # for items in samples_data:
        #     if items == "BRIDGES, MONA":
        #         print(items.text)
        sample_transit.get_generate_report()
        time.sleep(5)