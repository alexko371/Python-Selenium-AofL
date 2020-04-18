from screen_pages.base_screen import BaseScreen

class Login(BaseScreen):

    def to_abcmouse(self, email, password):
        self.app.driver.find_element_by_id('login_email').send_keys(email)
        self.app.driver.find_element_by_id('login_password').send_keys(password)
        self.app.driver.find_element_by_css_selector("[type='submit']").click()


    def to_free_teacher_account(self, email, password):
        iframe = self.app.driver.find_element_by_id("content-iframe")
        self.app.driver.switch_to.frame(iframe)
        self.app.driver.find_element_by_id("login-button").click()
        self.app.driver.find_element_by_id("login_email").send_keys(email)
        self.app.driver.find_element_by_id("login_password").send_keys(password)
        submit_button = self.app.driver.find_element_by_css_selector(
            ".LoginPopupController_submit_button.aofl_century_bold")
        self.app.driver.execute_script("arguments[0].click();", submit_button)
        self.app.driver.switch_to.default_content()