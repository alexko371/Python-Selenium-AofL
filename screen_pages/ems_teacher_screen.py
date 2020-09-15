from os import name

from selenium.webdriver import ActionChains
from screen_pages.base_screen import BaseScreen
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class EmsTeacherScreen(BaseScreen):

    def open_ems_teacher_registration_page(self):
        self.app.driver.get("https://bn.qtest.abcmouse.com/admin")

    def open_live_ems_teacher_registration_page(self):
        self.app.driver.get("https://www.abcmouse.com/admin")

    def login_to_ems(self):
        self.open_ems_iframe()
        self.app.driver.find_element_by_id("username").send_keys("aaron.worley@test.com")
        self.app.driver.find_element_by_id("password").send_keys("password")
        self.app.driver.find_element_by_css_selector("[class*='emsButton']").click()
        self.app.driver.switch_to.default_content()

    def navigate_to_organizations(self):
        self.open_ems_iframe()
        self.app.driver.find_element_by_css_selector("[ng-click*='goToOrganization()']").click()
        self.app.driver.switch_to.default_content()

    def create_organization(self, org_name):
        self.open_ems_iframe()
        self.wait_until_css_clickable(".u-text-underline").click()
        self.wait_until_id_clickable("instName").send_keys(org_name)
        self.wait_until_css_clickable("[class='emsButton']").click()
        self.app.driver.switch_to.default_content()


    def select_my_organization(self):
        self.open_ems_iframe()
        action_chain = ActionChains(self.app.driver)
        action_chain.double_click(self.app.driver.find_element_by_xpath("(//a[contains(@class,'emsHeader_areaLink')]) [3]")).perform()       #####    (//div[contains(@class,'emsList__row')]) [4]
        action_chain = ActionChains(self.app.driver)
        action_chain.double_click(
            self.app.driver.find_element_by_xpath("(//div[contains(@class,'emsList__row')]) [4]")).perform()
        self.app.driver.switch_to.default_content()

    def click_institution_button(self):
        self.open_ems_iframe()
        action_chain = ActionChains(self.app.driver)
        action_chain.double_click(
            self.app.driver.find_element_by_xpath("(//li[contains(@class,'menu_item')]) [2]")).perform()     #####  (//li[contains(@class,'menu_item')]) [2]
        self.app.driver.switch_to.default_content()





    def create_institution(self, inst_name):
        self.open_ems_iframe()
        self.app.driver.find_element_by_css_selector("[class*='emsInstitution__create']").click()
        self.app.driver.find_element_by_id("instName").send_keys(inst_name)
        self.app.driver.find_element_by_css_selector("[class='emsButton']").click()
        self.app.driver.switch_to.default_content()

    def select_my_institution(self):
        time.sleep(1)
        self.open_ems_iframe()
        action_chain = ActionChains(self.app.driver)
        action_chain.double_click(self.app.driver.find_element_by_xpath("(//div[contains(@class,'emsList__row')]) [5]")).perform()
        self.app.driver.switch_to.default_content()

    def select_schools(self):
        self.open_ems_iframe()
        self.wait_until_xpath_clickable("(//h4[contains(@class,'uploadFilesSummary__icon')]) [1]").click()
        # self.app.driver.find_element_by_xpath("(//h4[contains(@class,'uploadFilesSummary__icon')]) [1]").click()
        self.app.driver.switch_to.default_content()

    def create_school(self, school_name, ext_id):
        time.sleep(3)
        self.open_ems_iframe()
        create_school_button = self.wait_until_css_clickable("[class*='emsDownloadLink__plus']")    ##### [class*='emsDownloadLink']
        create_school_button.click()
        self.wait_until_id_clickable("instName").send_keys(school_name)

        self.wait_until_id_clickable("externalId").send_keys(ext_id)
        self.app.driver.find_element_by_css_selector("[class='emsButton']").click()
        # open_created_school = self.wait_until_xpath_clickable("(//div[contains(@class,'emsListItem__table')]) [1]")
        # open_created_school.click()
        self.app.driver.switch_to.default_content()

    def open_created_school(self):
        self.open_ems_iframe()
        self.wait_until_xpath_clickable("(//div[contains(@class,'emsListItem__table')]) [1]").click()
        self.app.driver.switch_to.default_content()

    def return_to_my_institution_details_page(self):
        time.sleep(3)
        self.open_ems_iframe()
        action_chain = ActionChains(self.app.driver)
        action_chain.double_click(
            self.app.driver.find_element_by_css_selector("[aria-label*='Test']")).perform()  ###   (//a[contains(@class,'emsBreadcrumb__item')]) [2]

        # return_to_institution = self.wait_until_xpath_clickable("(//a[contains(@class,'emsBreadcrumb__item')]) [2]")
        # self.app.driver.find_element_by_xpath("(//a[contains(@class,'emsBreadcrumb__item')]) [2]").click()
        self.app.driver.switch_to.default_content()
        # return return_to_institution.click()

    def select_sections(self):
        self.open_ems_iframe()
        self.wait_until_xpath_clickable("(//h4[contains(@class,'uploadFilesSummary__icon')]) [4]").click()
        self.app.driver.switch_to.default_content()

    def create_section(self, section_name, ext_id):
        time.sleep(3)
        self.open_ems_iframe()
        click_create_section_link = self.wait_until_css_clickable("[class*='plus-icon']")
        click_create_section_link.click()
        add_section_name = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [1]")
        add_section_name.send_keys(section_name)
        add_ext_id = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [2]")
        add_ext_id.send_keys(ext_id)
        ### Select School
        self.app.driver.find_element_by_id("emsForm__select--license-products").click()
        self.wait_until_css_clickable("[label='Test School 1']").click()
        # select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--license-products"))
        # select_grade.select_by_value("Test School 1")

        click_save_button = self.wait_until_css_clickable("[class*='emsLicenseButton__save']")
        click_save_button.click()
        self.app.driver.switch_to.default_content()

    def select_teachers(self):
        self.open_ems_iframe()
        self.wait_until_xpath_clickable("(//h4[contains(@class,'uploadFilesSummary__icon')]) [2]").click()
        self.app.driver.switch_to.default_content()

    def create_teachers(self, first_name, last_name, ext_id, ems_email):
        time.sleep(3)
        self.open_ems_iframe()
        click_create_teacher_link = self.wait_until_css_clickable("[class*='plus-icon']")
        click_create_teacher_link.click()
        add_first_name = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [1]")
        add_first_name.send_keys(first_name)
        add_last_name = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [2]")
        add_last_name.send_keys(last_name)
        add_ext_id = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [3]")
        add_ext_id.send_keys(ext_id)
        ### Select School
        self.wait_until_id_clickable("emsForm__select--teacher-school").click()
        self.wait_until_css_clickable("[label='Test School 1']").click()
        input_email = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [4]")
        input_email.send_keys(ems_email)
        ### Select Section
        self.wait_until_id_clickable("emsForm__select--teacher-section")
        self.wait_until_css_clickable("[label='Test - Section']").click()
        click_save_button = self.wait_until_css_clickable("[class*='emsTeacherButton__save']")
        click_save_button.click()
        self.app.driver.switch_to.default_content()

    def select_students(self):
        self.open_ems_iframe()
        self.wait_until_xpath_clickable("(//h4[contains(@class,'uploadFilesSummary__icon')]) [3]").click()
        self.app.driver.switch_to.default_content()

    """LICENSE PAGE"""
    def create_license(self, lic_name, start_date, end_date, pw):
        self.open_ems_iframe()
        click_site_shell_license_link = self.wait_until_xpath_clickable("(//div[contains(@class,'emsSideNavigation__icon')]) [5]")
        click_site_shell_license_link.click()
        create_license_link = self.wait_until_css_clickable("img[class*='emsDownloadLink']")
        create_license_link.click()
        select_license_name = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [1]")
        select_license_name.send_keys(lic_name)
        select_start_date = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [4]")
        select_start_date.send_keys(start_date)
        select_end_date = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [5]")
        select_end_date.send_keys(end_date)
        create_password = self.wait_until_css_clickable("[name=defaultTeacherPassword]")
        create_password.clear()
        create_password = self.wait_until_css_clickable("[name=defaultTeacherPassword]")
        create_password.send_keys(pw)
        click_save_button = self.wait_until_css_clickable("ems-smart-button [class*='emsButton']")
        click_save_button.click()
        self.app.driver.switch_to.default_content()

    def activate_license(self):
        self.open_ems_iframe()
        click_site_shell_license_link = self.wait_until_xpath_clickable(
            "(//div[contains(@class,'emsSideNavigation__icon')]) [5]")
        click_site_shell_license_link.click()
        select_created_license = self.wait_until_xpath_clickable("(//div[contains(@class,'emsListItem__table')]) [1]")
        select_created_license.click()
        select_assign_license = self.wait_until_css_clickable("span[class*='emsLicenseRosterContainer']")
        select_assign_license.click()
        institution_license_checkbox = self.wait_until_css_clickable("input[ng-model='item.checkbox']")
        institution_license_checkbox.click()
        save_button = self.wait_until_css_clickable("button[class*='emsLicenseButton__save']")
        save_button.click()
        activate_license_button = self.wait_until_css_clickable("button[class*='emsLicenseDetails__button']")
        activate_license_button.click()
        confirm_activate_license_button = self.wait_until_xpath_clickable("(//button[contains(@class,'emsButton--confirmation')]) [2]")
        confirm_activate_license_button.click()

        self.app.driver.switch_to.default_content()




    """ASSERTIONS"""

    def organizations_name(self, org_name):
        self.open_ems_iframe()
        self.wait_until_text_visible_by_xpath("//*[@id='main']/div[2]/main/div/ems-search-container/div/ems-list-container/div/ems-list/div/ems-list-item/div[1]/div[1]", org_name)
        self.app.driver.switch_to.default_content()

    def create_organizations_title(self, org_title):
        self.open_ems_iframe()
        create_organizations_string = self.wait_until_text_visible_by_css(".u-text-underline", org_title)
        self.app.driver.switch_to.default_content()
        return create_organizations_string

    def institution_title(self, inst_name):
        self.open_ems_iframe()
        institution_string = self.wait_until_text_visible_by_css("[class*='emsInstitutionDetail__title']", inst_name)
        self.app.driver.switch_to.default_content()
        return institution_string

    ####### SCHOOL PAGE ASSERTION
    def school_title(self, school):
        self.open_ems_iframe()
        # self.wait_until_text_value_visible_by_xpath("(//div[contains(@class,'emsForm__box')]) [3]")
        # self.wait_until_text_visible_by_xpath("(//div[contains(@class,'emsListItem__table')]) [3]", school)    ##### (//a[contains(@class,'emsBreadcrumb__item')]) [3]
        school_name_string = self.wait().until(
            EC.visibility_of_any_elements_located((By.XPATH, "(//div[contains(@class,'emsForm__box')]) [3]"), school))
        self.app.driver.switch_to.default_content()
        return school_name_string

### text_to_be_present_in_element