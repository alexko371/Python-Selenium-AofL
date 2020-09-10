from selenium.webdriver import ActionChains
from screen_pages.base_screen import BaseScreen
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class EmsTeacherScreen(BaseScreen):

    def open_ems_teacher_registration_page(self, ems_teacher_registration_page):
        self.app.driver.get(ems_teacher_registration_page)

    # def open_ems_iframe(self):
    #     ems_iframe = self.app.driver.find_element_by_css_selector("[class='frame']")
    #     open_ems_iframe = self.app.driver.switch_to.frame(ems_iframe)
    #     return open_ems_iframe


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

    ####### ASSERTION
    def create_organizations_title(self, org_title):
        self.open_ems_iframe()
        create_organizations_string = self.wait_until_text_visible_by_css(".u-text-underline", org_title)
        # create_organizations_string = self.wait().until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".u-text-underline"), string))
        self.app.driver.switch_to.default_content()
        return create_organizations_string


    def create_organization(self, org_name):
        self.open_ems_iframe()
        self.wait_until_css_clickable(".u-text-underline").click()
        # self.app.driver.find_element_by_css_selector(".u-text-underline").click()
        self.wait_until_id_clickable("instName").send_keys(org_name)
        # self.app.driver.find_element_by_id("instName").send_keys(org_name)
        self.wait_until_css_clickable("[class='emsButton']").click()
        # self.app.driver.find_element_by_css_selector("[class='emsButton']").click()
        self.app.driver.switch_to.default_content()

    ####### ASSERTION
    def organizations_name(self, org_name):
        self.open_ems_iframe()
        self.wait_until_text_visible_by_xpath("//*[@id='main']/div[2]/main/div/ems-search-container/div/ems-list-container/div/ems-list/div/ems-list-item/div[1]/div[1]", org_name)
        #self.wait().until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='main']/div[2]/main/div/ems-search-container/div/ems-list-container/div/ems-list/div/ems-list-item/div[1]/div[1]"), string))
        self.app.driver.switch_to.default_content()
        # return organizations_name  #organizations_name =

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


    ####### ASSERTION
    def institution_title(self, inst_name):
        self.open_ems_iframe()
        institution_string = self.wait_until_text_visible_by_css("[class*='emsInstitutionDetail__title']", inst_name)
        self.app.driver.switch_to.default_content()
        return institution_string


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

    ####### SCHOOL PAGE ASSERTION
    def school_title(self, school):
        # time.sleep(3)
        self.open_ems_iframe()
        self.wait_until_text_visible_by_css("h3[class]", school)    #####   (//a[contains(@class,'emsBreadcrumb__item')]) [3]
        # school_string = self.wait().until(
        #     EC.text_to_be_present_in_element((By.XPATH, "(//a[contains(@class,'emsBreadcrumb__item')]) [3]"), school))
        self.app.driver.switch_to.default_content()
        # return school_string

    def create_school(self, school_name, ext_id):
        # time.sleep(3)
        self.open_ems_iframe()
        self.wait_until_css_clickable("[class*='emsDownloadLink']").click()

        # self.app.driver.find_element_by_css_selector("[class*='emsDownloadLink']").click()
        self.wait_until_id_clickable("instName").send_keys(school_name)
        # self.app.driver.find_element_by_id("instName").send_keys(school_name)

        self.wait_until_id_clickable("externalId").send_keys(ext_id)
        # self.app.driver.find_element_by_id("externalId").send_keys(ext_id)
        self.app.driver.find_element_by_css_selector("[class='emsButton']").click()
        self.app.driver.switch_to.default_content()
        # return select_click_school_button.click(), add_school_name

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
    # def

    # def click_create_students(self):
    #     self.open_ems_iframe()
    #     self.wait_until_css_clickable("[class*='plus-icon']").click()
