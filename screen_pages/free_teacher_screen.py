from screen_pages.base_screen import BaseScreen
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FreeTeacherScreen(BaseScreen):

    def open_teacher_registration_page(self, teacher_registration_page):
        self.app.driver.get(teacher_registration_page)  # Update URL QTEST!

    def open_teacher_login_page(self, teacher_registration_page):
        self.app.driver.get(teacher_registration_page)  # Update URL QTEST!

    def submit_email(self, email):
        #  Email Fields (DON'T FORGET TO UPDATE EMAIL FIELDS)
        self.app.driver.find_element_by_id("email").send_keys(email)
        self.app.driver.find_element_by_id("confirm_email").send_keys(email)

    def input_name(self, fname, lname):
        #  Teacher Name Fields
        self.app.driver.find_element_by_id("first_name").send_keys(fname)
        self.app.driver.find_element_by_id("last_name").send_keys(lname)

    def submit_confirm_password(self, password):
        self.app.driver.find_element_by_id("password").send_keys(password)
        self.app.driver.find_element_by_id("confirm_password").send_keys(password)

    def submit_district_info_fields(self, state_value, school_district_value):
        #  District Info Fields
        state = Select(self.app.driver.find_element_by_id("states"))
        state.select_by_value(state_value)
        district = Select(self.app.driver.find_element_by_id("districts"))
        district.select_by_value(school_district_value)
        school = Select(self.app.driver.find_element_by_id("schools"))
        school.select_by_value("other")


    def submit_school_info_fields(self, school_name, address, city, zip, district, phone, superintendent,
                                  website, other_info):
        ##### School Info Fields
        self.app.driver.find_element_by_id("school_name").send_keys(school_name)
        self.app.driver.find_element_by_id("school_address").send_keys(address)
        self.app.driver.find_element_by_id("school_city").send_keys(city)
        self.app.driver.find_element_by_id("school_zip").send_keys(zip)
        self.app.driver.find_element_by_id("school_district").clear()
        self.app.driver.find_element_by_id("school_district").send_keys(district)
        self.app.driver.find_element_by_id("school_phone").send_keys(phone)
        self.app.driver.find_element_by_id("district_super").clear()
        self.app.driver.find_element_by_id("district_super").send_keys(superintendent)
        self.app.driver.find_element_by_id("website").send_keys(website)
        school_type_field = Select(self.app.driver.find_element_by_id("school_type"))
        school_type_field.select_by_value("public school")
        primary_usage = Select(self.app.driver.find_element_by_id("primary_usage"))
        primary_usage.select_by_value("other")
        self.app.driver.find_element_by_id("other_textarea").send_keys(other_info)
        self.app.driver.find_element_by_id("checkbox_off_img").click()

    def proceed_to_welcome_page(self):
        # Submit Next Button
        button = self.wait_until_button_clickable("button_next_img")
        return button.click()


    def proceed_to_survey_page(self):
        # Continue Button
        self.app.driver.find_element_by_id("button_link_continue").click()

    def proceed_to_step_1_create_teacher_account_page(self):
        # Survey Button
        self.app.driver.find_element_by_id("survey-next").click()

    def step_1_create_teacher_account(self, teachers_name):
        # Step - 1 Create Teacher Account
        self.app.driver.find_element_by_id("teachers-name").clear()
        self.app.driver.find_element_by_id("teachers-name").send_keys(teachers_name)
        # self.app.driver.find_element_by_css_selector("[src='/av/hamster.jpg']").click()

    def proceed_to_step_2_add_students(self):
        # Create Teacher Next Button
        self.app.driver.find_element_by_id("create-account-next").click()

    def proceed_to_abcmouse_page(self):
        # Step 3: Get Started on ABCmouse.com Button
        button = self.wait_until_button_clickable("getting-started-next")
        return button.click()


    ####### ASSERTIONS
    def welcome_to_abcmouse_text(self, string):
        welcome_string = self.wait().until(EC.text_to_be_present_in_element((By.ID, "sub_confirm_welcome"), string))
        return welcome_string

    def survey_title(self, survey_title):
        text_string = self.wait_until_text_visible(csslocator="h1.title.alignleft", text_string=survey_title)
        return text_string

    def step_1_title(self, title):
        text_string = self.wait_until_text_visible(csslocator="h1.title.alignleft", text_string=title)
        return text_string

    def step_2_title(self, title):
        text_string = self.wait_until_text_visible(csslocator="h1.title.alignleft", text_string=title)
        return text_string

    def step_3_title(self, title):
        text_string = self.wait_until_text_visible(csslocator="h1.title.alignleft", text_string=title)
        return text_string

    def teacher_image_icon(self):
        image_icon = self.app.driver.find_element_by_css_selector("img.GsHeader__user-img")
        return image_icon

    def teacher_welcome_title(self, welcome_string):
        iframe2 = self.app.driver.find_element_by_id("mainFrame")
        self.app.driver.switch_to.frame(iframe2)

        text_string = self.wait_until_text_visible(csslocator="span[class*='HomepageCtrl__intro']", text_string=welcome_string)
        return text_string
        self.app.driver.switch_to.default_content()
