from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class BaseScreen:

    def __init__(self, app):
        self.app = app


    def wait(self):
        wait = WebDriverWait(self.app.driver, 10)
        return wait

    def wait_until_text_visible(self, csslocator, text_string):
        return self.wait().until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, csslocator), text_string))

    def wait_until_frame_available(self, id_locator):
        return self.wait().until(EC.frame_to_be_available_and_switch_to_it((By.ID, id_locator)))

    def wait_until_button_clickable(self, id_locator):
        return self.wait().until(EC.element_to_be_clickable((By.ID, id_locator)))

    # def find_element(self, cssLocator):
    #     return self.app.driver.find_element_by_css_selector(cssLocator)
    #
    # def click_to_element(self, cssLocator):
    #     self.find_element(cssLocator).click()
    #
    # def type_text(self, cssLocator, value):
    #     element = self.find_element(cssLocator)
    #     element.send_keys(value)