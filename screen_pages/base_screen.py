from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class BaseScreen:

    def __init__(self, app):
        self.app = app


    def wait(self):
        wait = WebDriverWait(self.app.driver, 10)
        return wait

    def wait_until_text_visible_by_css(self, css_locator, text_string):
        return self.wait().until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_locator), text_string))

    def wait_until_text_visible_by_xpath(self, xpath_locator, text_string):
        return self.wait().until(EC.text_to_be_present_in_element((By.XPATH, xpath_locator), text_string))

    def wait_until_frame_available_by_id(self, id_locator):
        return self.wait().until(EC.frame_to_be_available_and_switch_to_it((By.ID, id_locator)))

    def wait_until_frame_available_by_css(self, css_locator):
        return self.wait().until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, css_locator)))

    def wait_until_id_clickable(self, id_locator):
        return self.wait().until(EC.element_to_be_clickable((By.ID, id_locator)))

    def wait_until_css_clickable(self, css_locator):
        return self.wait().until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_locator)))

    def wait_until_xpath_clickable(self, xpath_locator):
        return self.wait().until(EC.element_to_be_clickable((By.XPATH, xpath_locator)))


    def open_ems_iframe(self):
        ems_iframe = self.wait_until_css_clickable("[class='frame']")
        open_ems_iframe = self.app.driver.switch_to.frame(ems_iframe)
        return open_ems_iframe

    # def find_element(self, cssLocator):
    #     return self.app.driver.find_element_by_css_selector(cssLocator)
    #
    # def click_to_element(self, cssLocator):
    #     self.find_element(cssLocator).click()
    #
    # def type_text(self, cssLocator, value):
    #     element = self.find_element(cssLocator)
    #     element.send_keys(value)