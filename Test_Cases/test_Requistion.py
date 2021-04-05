import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Page_Object.Requisition import Requisition
from Utilities.BaseClass import BaseClass


class TestCase1(BaseClass):
    setup_menu = (By.LINK_TEXT, "Setup")
    users_menu = (By.XPATH, "//tbody/tr[1]/td[3]/ul[1]/li[6]/ul[1]/li[3]/a[1]")
    client_menu = (By.XPATH, "//a[@id='UserNavigation11_dlUserNavigation_hyLnkNavigation_0']")

    def test_case1(self):

        self.login()
        requisition = Requisition(self.driver)
        requisition.get_new_requisition()
        self.driver.switch_to.window(self.driver.window_handles[1])
        requisition.search_MR_number()
        requisition.get_search_button()
        requisition.get_MR_result_click()
        requisition.get_create_new_requisition()
        requisition.get_client_select_requistition()
        # client = Select(self.driver.find_element_by_id(self.client_select_requistition))
        # client.select_by_visible_text("Demo")
        requisition.get_reference_provider()
        # ref_provider = Select(self.driver.find_element_by_id(self.referring_provider_requistition))
        # ref_provider.select_by_visible_text("Applicable, Not")
        # requisition.get_collection_date()
        requisition.get_collection_date()
        requisition.get_fasting_requistition()
        # client = Select(self.driver.find_element_by_id(self.fasting_requistition))
        # client.select_by_visible_text("No")
        requisition.get_panel_search()
        requisition.get_panel_selection()
        requisition.get_diagnosis_code()
        requisition.get_diagnosis_search()
        requisition.get_add_diagnosis()
        selected_diag = requisition.get_selected_diagnosis()
        assert self.selected_diagnosis_text in selected_diag
        requisition.get_prescribed_medication()
        requisition.get_select_prescribed_medication()
        time.sleep(5)

        # dashboard.Role_Click()
        # dashboard.mouse_hover()
        # action = ActionChains(self.driver)
        # # setup = self.driver.find_element(*self.setup_menu)
        # # user = self.driver.find_element(*self.users_menu)
        # # client = self.driver.find_element(*self.client_menu)
        # action.move_to_element(setup).move_to_element(user).move_to_element(client).click().perform()
        # dashboard.client_click()
