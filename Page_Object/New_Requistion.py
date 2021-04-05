from selenium.webdriver.common.by import By

from Page_Object.Common import Common


class New_Patient(Common):

    new_patient = (By.ID, "ContentPlaceHolder1_LabsOrderControl_lnkPatCreate")
    first_name = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtFirstName")
    last_name = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtLastName")
    dob = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtDOB")
    cell = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtCell")
    address = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtAddress1")
    city = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtCity")
    # state_patient = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_ddlState")
    zip_code = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtZIP")
    same_as_patient = (By.XPATH, "//*[@id='ContentPlaceHolder1_ManagePatientCreateV31_pnlClient']/div[2]/div[1]/h5/a")
    same_as_patient_primary_insurance = (By.XPATH, "//*[@id='Primary']/div[1]/div[2]/div[1]/h5/a")
    policy_num = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_txtPolicyNumber")
    client_name_select = (By.XPATH, "//label[@for='ContentPlaceHolder1_ManagePatientCreateV31_dlClientList_chkBoxClient_11']")
    create_patient = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_btnSave")
    close_patient = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_lnkbtnClose")
    sex = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_ddlGender")
    race_patient = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_ddlRace")
    state_patient = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_ddlState")
    insurance_name_primary_insurance = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_ddlInsurance")
    relationship_primary_insurance = (By.ID, "ContentPlaceHolder1_ManagePatientCreateV31_ddlRelationshipToInsured")

    def __init__(self, driver):
        self.driver = driver

    def get_new_patient(self):
        return self.onclick(self.new_patient)

    def get_first_name(self):
        return self.sendkey(self.first_name, "Salman")

    def get_last_name(self):
        return self.sendkey(self.last_name, "Ali")

    def get_dob(self):
        self.execute_script(self.dob)
        return self.sendkey(self.dob, "30/05/1994")

    def get_cell(self):
        self.onclick(self.cell)
        return self.sendkey(self.cell, "03322293892")

    def get_address(self):
        return self.sendkey(self.address, "ABCDEFGHIJKL")

    def get_city(self):
        return self.sendkey(self.city, "New York")

    def get_zip_code(self):
        self.onclick(self.zip_code)
        return self.sendkey(self.zip_code, "75000")

    def get_same_as_patient(self):
        return self.onclick(self.same_as_patient)

    def get_same_as_patient_primary_insurance(self):
        return self.execute_script(self.same_as_patient_primary_insurance)

    def get_policy_num(self):
        return self.sendkey(self.policy_num, "policy")

    def get_client_name_select(self):
        return self.execute_script(self.client_name_select)

    def get_create_patient(self):
        return self.execute_script(self.create_patient)

    def get_close_patient(self):
        return self.onclick(self.close_patient)

    # def get_state_patient(self):
    #     return self.onclick(self.state_patient)
    def get_sex(self):
        return self.dropdown_by_text(self.sex, "Male")

    def get_race_patient(self):
        return self.dropdown_by_index(self.race_patient, 2)

    def get_state_patient(self):
        return self.dropdown_by_text(self.state_patient, "NY")

    def get_insurance_name_primary_insurance(self):
        return self.dropdown_by_text(self.insurance_name_primary_insurance, "AETNA MEDICARE - 60054")

    def get_relationship_primary_insurance(self):
        return self.dropdown_by_text(self.relationship_primary_insurance, "Parent")