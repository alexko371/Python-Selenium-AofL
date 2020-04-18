from screen_pages.base_screen import BaseScreen
import time

class Onboarding(BaseScreen):

    def expand_shadow_element(self, element):
        shadow_root = self.app.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def open_login_page(self, login_page):
        self.app.driver.get(login_page)

    def welcome_page_click_get_started_button(self):
        ###### Welcome to ABCmouse page
        time.sleep(1)
        iframe = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe)
        get_started = self.app.driver.find_element_by_id("survey-link")
        self.app.driver.execute_script("arguments[0].click();", get_started)
        self.app.driver.switch_to.default_content()

    def survey_click_continue_buttons(self):
        ######## STEP 1.1 Survey Continue Button
        time.sleep(1)
        iframe_step_1_1 = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_step_1_1)
        continue_button = self.app.driver.find_element_by_id("survey-2-link")
        self.app.driver.execute_script("arguments[0].click();", continue_button)
        self.app.driver.switch_to.default_content()

        ######## STEP 1.2 Survey Continue Button
        # time.sleep(1)
        time.sleep(1)
        iframe_step_1_2 = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_step_1_2)
        continue_button = self.app.driver.find_element_by_id("setup-parent-link")
        self.app.driver.execute_script("arguments[0].click();", continue_button)
        self.app.driver.switch_to.default_content()

    def input_parent_name(self, parent_first_name, parent_family_name):
        ######## STEP 2 Setup Parent Continue
        time.sleep(3)
        iframe_step_2_1 = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_step_2_1)
        first_name_field = self.app.driver.find_element_by_name("firstName")
        first_name_field.send_keys(parent_first_name)
        family_name_field = self.app.driver.find_element_by_name("familyName")
        family_name_field.send_keys(parent_family_name)
        setup_parent_continue = self.app.driver.find_element_by_id("setup-parent-continue")
        self.app.driver.execute_script("arguments[0].click();", setup_parent_continue)
        self.app.driver.switch_to.default_content()

    def create_child_profile(self, child_name, gender, academic_level):
        ###### STEP 3 Create Child Profile
        time.sleep(3)
        iframe_step_3 = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_step_3)
        child_first_name_field = self.app.driver.find_element_by_name("firstName")
        child_first_name_field.send_keys(child_name)  # TO BE UPDATED   G_1(da3)
        gender_checkbox = self.app.driver.find_element_by_id(gender)
        self.app.driver.execute_script("arguments[0].click();", gender_checkbox)
        birthday_month = self.app.driver.find_element_by_xpath("(//div[contains(@class,'dropdown')]) [2]")
        self.app.driver.execute_script("arguments[0].click();", birthday_month)
        actual_month_field = self.app.driver.find_element_by_xpath("(//div[contains(@class,'ng-options')]) [1]")
        for option_1 in actual_month_field.find_elements_by_css_selector(
                ".single"):  #####   (//label[contains(@class,'single')]) [4]
            if option_1.text == "January":
                self.app.driver.execute_script("arguments[0].click();", option_1)
                # option_1.click()  # select() in earlier versions of webdriver
                break
        birthday_year = self.app.driver.find_element_by_xpath(
            '//*[@id="onboarding"]/div/div/div[1]/form/div[1]/div[3]/aofl-dropdown[2]/div/div/div[1]')
        self.app.driver.execute_script("arguments[0].click();", birthday_year)
        actual_year_field = self.app.driver.find_element_by_xpath(
            "(//div[contains(@class,'ng-options')]) [2]")
        # time.sleep(3)
        for option_2 in actual_year_field.find_elements_by_xpath(
                "(//label[contains(@class,'single')]) [16]"):
            if option_2.text == "2017":
                self.app.driver.execute_script("arguments[0].click();", option_2)
                break
        select_academic_level = self.app.driver.find_element_by_id(academic_level)
        self.app.driver.execute_script("arguments[0].click();", select_academic_level)
        step_3_continue_button = self.app.driver.find_element_by_css_selector(".continue-btn")
        self.app.driver.execute_script("arguments[0].click();", step_3_continue_button)
        self.app.driver.switch_to.default_content()

    def choose_avatar(self, avatar):
        #### STEP 3.1 CHOOSE AVATAR
        time.sleep(3)
        iframe_step_3_1 = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_step_3_1)
        choose_avatar_icon = self.app.driver.find_element_by_id(avatar)
        self.app.driver.execute_script("arguments[0].click();", choose_avatar_icon)
        step_3_1_continue_button = self.app.driver.find_element_by_css_selector("[class *='continue-btn']")
        self.app.driver.execute_script("arguments[0].click();", step_3_1_continue_button)
        self.app.driver.switch_to.default_content()

    def choose_hamster_and_fish(self, hamster, fish, hamster_name):
        #### STEP 3.2 CHOOSE Hamster/Fish
        time.sleep(3)
        iframe_step_3_2 = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_step_3_2)
        select_hamster = self.app.driver.find_element_by_id(hamster)
        self.app.driver.execute_script("arguments[0].click();", select_hamster)
        select_fish = self.app.driver.find_element_by_id(fish)
        self.app.driver.execute_script("arguments[0].click();", select_fish)
        input_hamster_name = self.app.driver.find_element_by_name("hamsterName")
        input_hamster_name.send_keys(hamster_name)
        step_3_2_continue_button = self.app.driver.find_element_by_css_selector("[class *='continue-btn']")
        self.app.driver.execute_script("arguments[0].click();", step_3_2_continue_button)
        self.app.driver.switch_to.default_content()

    def skip_video(self):
        ###### STEP 4.1 SKIP VIDEO
        time.sleep(3)
        iframe_step_3_3 = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_step_3_3)
        step_4_skip_button = self.app.driver.find_element_by_css_selector("a.onboarding-video-skip")
        self.app.driver.execute_script("arguments[0].click();", step_4_skip_button)
        skip_for_now_popup_button = self.app.driver.find_element_by_xpath("(//button[contains(@class,'aofl-btn')]) [2]")
        self.app.driver.execute_script("arguments[0].click();", skip_for_now_popup_button)

    def go_to_shp(self):
        ###### STEP 4.2 CONTINUE BUTTON CLICK
        step_4_continue_button = self.app.driver.find_element_by_id("student-homepage-link")
        self.app.driver.execute_script("arguments[0].click();", step_4_continue_button)
        self.app.driver.switch_to.default_content()

    ####### ASSERTION
    def mouse_pop_up(self):
        time.sleep(3)
        iframe_mouse = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe_mouse)
        mouse = self.app.driver.find_element_by_css_selector("body > route-view")
        return mouse
