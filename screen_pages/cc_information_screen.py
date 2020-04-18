from screen_pages.base_screen import BaseScreen

class CreditInformation(BaseScreen):

    def expand_shadow_element(self, element):
        shadow_root = self.app.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def expand_root_1(self):
        root1 = self.app.driver.find_element_by_tag_name("[style*='overflow'] subscription-form")
        shadow_root1 = self.expand_shadow_element(root1)
        return shadow_root1


    def submit_cc_qtest(self, cardholder, code_cvv, zip_code):
        shadow_root1 = self.expand_root_1()
        cardholder_name_field = shadow_root1.find_element_by_css_selector("#card-name")
        cardholder_name_field.send_keys(cardholder)

        card_number_field = shadow_root1.find_element_by_css_selector("#cc-num")
        card_number_field.send_keys("4000100011112224")  # qtest CC

        exp_month = shadow_root1.find_element_by_id("month-dropdown")
        exp_month.click()
        select_month_field = shadow_root1.find_element_by_css_selector("#month-dropdown > option:nth-child(7)")
        select_month_field.click()

        exp_year = shadow_root1.find_element_by_id("month-dropdown")
        exp_year.click()
        select_year_field = shadow_root1.find_element_by_css_selector("#year-dropdown > option:nth-child(4)")
        select_year_field.click()

        cvv_field = shadow_root1.find_element_by_css_selector("#cvv")
        cvv_field.send_keys(code_cvv)

        zip_code_field = shadow_root1.find_element_by_css_selector("#zipcode")
        zip_code_field.send_keys(zip_code)




    def check_to_agree(self):
        shadow_root1 = self.expand_root_1()
        root2 = shadow_root1.find_element_by_css_selector("[name='legalText']")
        shadow_root2 = self.expand_shadow_element(root2)

        check_to_agree_checkbox = shadow_root2.find_element_by_id("checkbox-container")
        self.app.driver.execute_script("arguments[0].click();", check_to_agree_checkbox)




    def submit_cc_live(self, cardholder):
        shadow_root1 = self.expand_root_1()
        cardholder_name_field = shadow_root1.find_element_by_css_selector("#card-name")
        cardholder_name_field.send_keys(cardholder)

        card_number_field = shadow_root1.find_element_by_css_selector("#cc-num")
        card_number_field.send_keys("379215847321004")  # qtest CC

        exp_month = shadow_root1.find_element_by_id("month-dropdown")
        exp_month.click()
        select_month_field = shadow_root1.find_element_by_css_selector("#month-dropdown > option:nth-child(7)")
        select_month_field.click()

        exp_year = shadow_root1.find_element_by_id("month-dropdown")
        exp_year.click()
        select_year_field = shadow_root1.find_element_by_css_selector("#year-dropdown > option:nth-child(4)")
        select_year_field.click()

        cvv_field = shadow_root1.find_element_by_css_selector("#cvv")
        cvv_field.send_keys("1432")

        zip_code_field = shadow_root1.find_element_by_css_selector("#zipcode")
        zip_code_field.send_keys("91203")