import time
from Page_Object.New_Requistion import New_Patient
from Utilities.BaseClass import BaseClass


class TestCase2(BaseClass):

    def test_create_patient(self):
        self.login()
        self.driver.get("https://mla-test.azurewebsites.net/Pages/Appointment/PatientRequisitionFormForLab")
        create_patient = New_Patient(self.driver)
        create_patient.get_new_patient()
        create_patient.get_first_name()
        create_patient.get_last_name()
        create_patient.get_dob()
        # drop = create_patient.get_sex()
        # drop.select_by_visible_text("Male")
        create_patient.get_sex()
        # select = Select(self.driver.find_element_by_id(self.sex_patient))
        # select.select_by_visible_text("Male")
        create_patient.get_race_patient()
        # select = Select(self.driver.find_element_by_id(self.race_patient))
        # select.select_by_index(2)
        create_patient.get_cell()
        create_patient.get_address()
        create_patient.get_city()
        create_patient.get_state_patient()
        # select = Select(self.driver.find_element_by_id(self.state_patient))
        # create_patient.get_state_patient()
        # states_selection = self.driver.find_elements_by_id(self.state_patient_loop)
        # print(len(states_selection))
        # for state in states_selection:
        #     if state.text == "NY":
        #         state.onclick()
        #         break
        #
        # time.sleep(3)
        # select.select_by_visible_text("NY")
        create_patient.get_zip_code()
        create_patient.get_same_as_patient()
        create_patient.get_same_as_patient_primary_insurance()
        create_patient.get_insurance_name_primary_insurance()
        # select = Select(self.driver.find_element_by_id(self.insurance_name_primary_insurance))
        # select.select_by_visible_text("AETNA MEDICARE - 60054")
        create_patient.get_policy_num()
        create_patient.get_relationship_primary_insurance()
        # select = Select(self.driver.find_element_by_id(self.relationship_primary_insurance))
        # select.select_by_visible_text("Parent")
        create_patient.get_client_name_select()
        create_patient.get_close_patient()

        # create_patient.get_create_patient()

        time.sleep(5)
