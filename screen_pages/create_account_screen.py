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

    def expand_root_2(self):
        root2 = self.app.driver.find_element_by_tag_name("[style*='overflow'] landscape-upgrade-form")
        shadow_root2 = self.expand_shadow_element(root2)
        return shadow_root2

    def expand_root_3(self):
        root3 = self.app.driver.find_element_by_tag_name("[reactivation='subscription']")
        shadow_root3 = self.expand_shadow_element(root3)
        return shadow_root3

    def expand_root_4(self):
        root4 = self.app.driver.find_element_by_tag_name("[style*='overflow'] assessment-annual-form")
        shadow_root4 = self.expand_shadow_element(root4)
        return shadow_root4


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

    ##### Annual Subscription Page $4.95/Mo. ($59.40 charged now and each year – Save 50%)
    def select_annual_subscription(self):
        time.sleep(2)
        shadow_root2 = self.expand_root_2()

        # root01 = self.app.driver.find_element_by_tag_name("[style*='overflow'] landscape-upgrade-form")
        # shadow_root002 = self.expand_shadow_element(shadow_root2)

        root02 = shadow_root2.find_element_by_css_selector("#paid-in-full")
        shadow_root002 = self.expand_shadow_element(root02)
        annual_subscription = shadow_root002.find_element_by_css_selector("#radio-wrapper")
        annual_subscription.click()

        subscription_continue_button = shadow_root2.find_element_by_css_selector("[class*='blue-button']")
        subscription_continue_button.click()

    def click_next_button_in_congrats_annual_subscription_pop_up(self):
        root0002 = self.app.driver.find_element_by_id("upgradeThankYou")
        shadow_root_0002 = self.expand_shadow_element(root0002)
        click_next_button = shadow_root_0002.find_element_by_css_selector("aofl-drawer > abcmouse-popup > section > button")
        click_next_button.click()

    ##### Annual Subscription Page (No thanks, I’d like to stay on my $9.95/month plan.)
    def select_no_thanks_annual_subscription(self):
        time.sleep(2)
        shadow_root2 = self.expand_root_2()
        # root01 = self.app.driver.find_element_by_tag_name("[style*='overflow'] landscape-upgrade-form")
        # shadow_root01 = self.expand_shadow_element(root01)
        root02 = shadow_root2.find_element_by_css_selector("#no-thanks")
        shadow_root02 = self.expand_shadow_element(root02)
        no_thanks = shadow_root02.find_element_by_css_selector("#radio-wrapper")
        no_thanks.click()
        subscription_continue_button = shadow_root2.find_element_by_css_selector("#upgrade-form-container > button")
        subscription_continue_button.click()

    ##### Annual Subscription Pop up
    def close_annual_subscription_pop_up(self):
        time.sleep(2)
        root001 = self.app.driver.find_element_by_css_selector("#upgradeOffer")
        shadow_root001 = self.expand_shadow_element(root001)
        close_button_section = shadow_root001.find_element_by_id("bottom")
        no_thanks_pop_up = close_button_section.find_element_by_css_selector("#bottom > button:nth-child(1)")
        no_thanks_pop_up.click()


    ###### Assessment Subscription Page
    def select_no_thanks_free_trial_assessment_subscription(self):
        time.sleep(3)
        shadow_root3 = self.expand_root_3()

        # root0001 = self.app.driver.find_element_by_css_selector("[reactivation='subscription']")
        # shadow_root0001 = self.expand_shadow_element(root0001)

        root03 = shadow_root3.find_element_by_css_selector("#no-thanks")
        shadow_root003 = self.expand_shadow_element(root03)
        assessment_no_thanks = shadow_root003.find_element_by_css_selector("#radio-wrapper")
        assessment_no_thanks.click()
        assessment_no_thanks = shadow_root3.find_element_by_css_selector(
            "#assessment-monthly-form-container > button")
        assessment_no_thanks.click()


    def select_free_trial_assessment_subscription(self):
        time.sleep(3)
        shadow_root3 = self.expand_root_3()
        root03 = shadow_root3.find_element_by_id("yes")
        shadow_root003 = self.expand_shadow_element(root03)
        yes_assessment = shadow_root003.find_element_by_css_selector("#radio-wrapper")
        yes_assessment.click()
        click_submit_button = shadow_root3.find_element_by_css_selector("[class*='blue-button']")
        click_submit_button.click()

    def click_next_button_in_free_trial_congrats_assessment_pop_up(self):
        root004 = self.app.driver.find_element_by_id("assessmentMonthlyThankYou")
        shadow_root_004 = self.expand_shadow_element(root004)
        click_next_button = shadow_root_004.find_element_by_css_selector(".blue-button")
        click_next_button.click()


    ####### YES! $39 95 for a yearly subscription to the Assessment Center*
    def select_annual_assessment_subscription(self):
        shadow_root4 = self.expand_root_4()
        root04 = shadow_root4.find_element_by_id("yes")
        shadow_root04 = self.expand_shadow_element(root04)
        yes_assessment = shadow_root04.find_element_by_id("radio-wrapper")
        yes_assessment.click()
        submit_button = shadow_root4.find_element_by_css_selector("[class='blue-button true']")
        submit_button.click()

    def select_no_thanks_assessment_subscription(self):
        shadow_root4 = self.expand_root_4()
        root04 = shadow_root4.find_element_by_id("no-thanks")
        shadow_root04 = self.expand_shadow_element(root04)
        yes_assessment = shadow_root04.find_element_by_id("radio-wrapper")
        yes_assessment.click()
        submit_button = shadow_root4.find_element_by_css_selector("[class='blue-button true']")
        submit_button.click()
        root004 = self.app.driver.find_element_by_id("assessmentOffer")
        shadow_root004 = self.expand_shadow_element(root004)
        assessment_no_thanks = shadow_root004.find_element_by_css_selector("#bottom > button:nth-child(1)")
        assessment_no_thanks.click()


    def click_next_button_in_annual_congrats_assessment_pop_up(self):
        root004 = self.app.driver.find_element_by_id("assessmentAnnualThankYou")
        shadow_root_004 = self.expand_shadow_element(root004)
        click_next_button = shadow_root_004.find_element_by_css_selector(".blue-button")
        click_next_button.click()


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