from selenium.webdriver.common.by import By

from Page_Object.Common import Common


class Requisition(Common):

    # role_selection = (By.XPATH, "//input[@id='SelectRole1_btnSelectRole']")
    # setup_menu_loc = (By.LINK_TEXT, "Setup")
    # users_menu_loc = (By.XPATH, "//tbody/tr[1]/td[3]/ul[1]/li[6]/ul[1]/li[3]/a[1]")
    # client_menu_loc = (By.XPATH, "//a[@id='UserNavigation11_dlUserNavigation_hyLnkNavigation_0']")
    new_requisition = (By.XPATH, "//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]")
    search_mr = (By.ID, "ContentPlaceHolder1_LabsOrderControl_txtMRNumber")
    search_button = (By.ID, "ContentPlaceHolder1_LabsOrderControl_btnSearch")
    mr_result_click = (By.ID, "ContentPlaceHolder1_LabsOrderControl_gvPatientList_lnkSelectPat_0")
    create_new_requisition = (By.ID, "ContentPlaceHolder1_LabsOrderControl_lnkNewRequisition")
    collection_date = (By.ID, "ctl00_ContentPlaceHolder1_LabsOrderControl_RadDateTimePicker1_dateInput")
    EHR = (By.ID, "ContentPlaceHolder1_LabsOrderControl_TextBoxEHR")
    panels_search = (By.ID, "SearchTextAvailPanel")
    panel_selection = (By.ID, "ContentPlaceHolder1_LabsOrderControl_gvAvailablePanel_chkPanel_11")
    diagnosis_code = (By.ID, "ContentPlaceHolder1_LabsOrderControl_SearchCode")
    diagnosis_search = (By.CSS_SELECTOR, "#ContentPlaceHolder1_LabsOrderControl_lnkSearchDx > i")
    add_diagnosis = (By.XPATH, "//i[@class='fa fa-plus-circle']")
    selected_diagnosis = (By.XPATH, "//*[@id='4']")
    client_select_requistition = (By.ID, "ContentPlaceHolder1_LabsOrderControl_ddlClient")
    referring_provider_requistition = (By.ID, "ContentPlaceHolder1_LabsOrderControl_ddlProvider")
    fasting_requistition = (By.ID, "ContentPlaceHolder1_LabsOrderControl_ddlFasting")
    prescribed_medication = (By.ID, "SearchTextMed")
    select_prescribed_medication = (By.ID, "ContentPlaceHolder1_LabsOrderControl_gvPriscribedMed_chkPrescribed_5")

    def __init__(self, driver):
        self.driver = driver

    # def Role_Click(self):
    #     #return self.onclick(self.role_selection)
    #     #return self.driver.execute_script("document.getElementByID('SelectRole1_btnSelectRole')[0].click()")
    #     element = self.driver.find_element(*self.role_selection)
    #     return self.driver.execute_script("arguments[0].click();", element)

    # def mouse_hover(self):
    #     action = ActionChains(self.driver)
    #     setup = self.driver.find_element(*self.setup_menu)
    #     user = self.driver.find_element(*self.users_menu)
    #   #  client = self.driver.find_element(*self.client)
    #     return action.move_to_element(setup).move_to_element(user)

    def get_new_requisition(self):
        return self.execute_script(self.new_requisition)

    def search_MR_number(self):
        return self.sendkey(self.search_mr, "180")

    def get_search_button(self):
        return self.onclick(self.search_button)

    def get_MR_result_click(self):
        return self.onclick(self.mr_result_click)

    def get_create_new_requisition(self):
        return self.onclick(self.create_new_requisition)

    def get_collection_date(self):
        return self.sendkey(self.collection_date, "3/26/2021 7:35 AM")

    def get_EHR(self):
        return self.sendkey(self.EHR, "abcd")

    def get_panel_search(self):
        return self.sendkey(self.panels_search, "Test")

    def get_panel_selection(self):
        return self.execute_script(self.panel_selection)

    def get_diagnosis_code(self):
        return self.sendkey(self.diagnosis_code, "A01.0")

    def get_diagnosis_search(self):
        return self.execute_script(self.diagnosis_search)

    def get_add_diagnosis(self):
        return self.execute_script(self.add_diagnosis)

    def get_selected_diagnosis(self):
        return self.get_element_text(self.selected_diagnosis)

    def get_client_select_requistition(self):
        return self.dropdown_by_text(self.client_select_requistition, "Demo")

    def get_reference_provider(self):
        return self.dropdown_by_text(self.referring_provider_requistition, "Applicable, Not")

    def get_fasting_requistition(self):
        return self.dropdown_by_text(self.fasting_requistition, "No")

    def get_prescribed_medication(self):
        return self.sendkey(self.prescribed_medication, "ambien")

    def get_select_prescribed_medication(self):
        return self.execute_script(self.select_prescribed_medication)