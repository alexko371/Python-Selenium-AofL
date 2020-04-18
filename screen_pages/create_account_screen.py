from screen_pages.base_screen import BaseScreen
import time


class CreateAccount(BaseScreen):

    def expand_shadow_element(self, element):
        shadow_root = self.app.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    # Subscription
    def open_abcmouse_web_page(self, qtest_web_page):
        self.app.driver.get(qtest_web_page)

    def expand_root_1(self):
        root1 = self.app.driver.find_element_by_tag_name("[style*='overflow'] subscription-form")
        shadow_root1 = self.expand_shadow_element(root1)
        return shadow_root1

    def submit_and_confirm_email(self, email):
        shadow_root1 = self.expand_root_1()
        email_field = shadow_root1.find_element_by_css_selector("#email")
        email_field.send_keys(email)
        confirm_email_field = shadow_root1.find_element_by_css_selector("#confirm-email")
        confirm_email_field.send_keys(email)

    def submit_and_confirm_password(self, password):
        shadow_root1 = self.expand_root_1()
        password_field = shadow_root1.find_element_by_css_selector("#password")
        password_field.send_keys(password)
        confirm_password_field = shadow_root1.find_element_by_css_selector("#confirm-password")
        confirm_password_field.send_keys(password)

    def click_submit_button(self):
        shadow_root1 = self.expand_root_1()
        time.sleep(9)
        submit_button = shadow_root1.find_element_by_css_selector("#submit-btn-container > button")
        submit_button.click()

    ##### Annual Subscription Page
    def select_no_thanks_anual_subscription(self):
        time.sleep(3)
        root01 = self.app.driver.find_element_by_tag_name("[style*='overflow'] landscape-upgrade-form")
        shadow_root01 = self.expand_shadow_element(root01)
        root02 = shadow_root01.find_element_by_css_selector("#no-thanks")
        shadow_root02 = self.expand_shadow_element(root02)
        no_thanks = shadow_root02.find_element_by_css_selector("#radio-wrapper")
        no_thanks.click()
        subscription_continue_button = shadow_root01.find_element_by_css_selector("#upgrade-form-container > button")
        subscription_continue_button.click()

    ##### Annual Subscription Pop up
    def close_anual_subscription_pop_up(self):
        time.sleep(3)
        root001 = self.app.driver.find_element_by_css_selector("#upgradeOffer")
        shadow_root001 = self.expand_shadow_element(root001)
        close_button_section = shadow_root001.find_element_by_id("bottom")
        no_thanks_pop_up = close_button_section.find_element_by_css_selector("#bottom > button:nth-child(1)")
        no_thanks_pop_up.click()

    ###### Assessment Subscription Page
    def select_no_thanks_assessment_subscription(self):
        time.sleep(3)
        root0001 = self.app.driver.find_element_by_css_selector("[reactivation='subscription']")
        shadow_root0001 = self.expand_shadow_element(root0001)
        root0002 = shadow_root0001.find_element_by_css_selector("#no-thanks")
        shadow_root0002 = self.expand_shadow_element(root0002)
        assessment_no_thanks = shadow_root0002.find_element_by_css_selector("#radio-wrapper")
        assessment_no_thanks.click()
        assessment_no_thanks = shadow_root0001.find_element_by_css_selector(
            "#assessment-monthly-form-container > button")
        assessment_no_thanks.click()

    ######## Click Submit Continue Registration button
    def click_submit_continue_registration_button(self):
        root1 = self.app.driver.find_element_by_css_selector(
            "body > aofl-app > confirmation-page > main-layout > section > div.button-panel > continue-button-reg")
        shadow_root1 = self.expand_shadow_element(root1)
        continue_button = shadow_root1.find_element_by_css_selector("[dom-scope='0AlIQfNR']")
        continue_button.click()

    ####### ASSERTION
    def thank_you_text(self):
        thank_you_string = self.app.driver.find_element_by_css_selector("h1.thankyou-tag").text
        return thank_you_string == "Thank you for subscribing to ABCmouse.com!"