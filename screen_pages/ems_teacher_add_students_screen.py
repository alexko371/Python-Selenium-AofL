from screen_pages.base_screen import BaseScreen
from selenium.webdriver.support.select import Select
import time

class EmsStudents(BaseScreen):

    def create_ems_girl_toddler(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_toddler_time()
        self.select_section()
        self.select_student_girl()
        self.add_student()

    def create_ems_boy_toddler(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_toddler_time()
        self.select_section()
        self.select_student_boy()
        self.add_student()

    def create_ems_girl_preschool(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_preschool()
        self.select_section()
        self.select_student_girl()
        self.add_student()

    def create_ems_boy_preschool(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_preschool()
        self.select_section()
        self.select_student_boy()
        self.add_student()

    def create_ems_girl_prekindergarten(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_prekindergarten()
        self.select_section()
        self.select_student_girl()
        self.add_student()

    def create_ems_boy_prekindergarten(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_prekindergarten()
        self.select_section()
        self.select_student_boy()
        self.add_student()

    def create_ems_girl_kindergarten(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_kindergarten()
        self.select_section()
        self.select_student_girl()
        self.add_student()

    def create_ems_boy_kindergarten(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_grade_kindergarten()
        self.select_section()
        self.select_student_boy()
        self.add_student()

    def create_ems_girl_first_grade(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_first_grade()
        self.select_section()
        self.select_student_girl()
        self.add_student()

    def create_ems_boy_first_grade(self, first_name, last_name, ext_id):
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_first_grade()
        self.select_section()
        self.select_student_boy()
        self.add_student()

    def create_ems_girl_second_grade(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_first_grade()
        self.select_section()
        self.select_student_girl()
        self.add_student()
        self.click_create_students_button()

    def create_ems_boy_second_grade(self, first_name, last_name, ext_id):
        self.click_create_students_button()
        self.submit_student_full_name(first_name, last_name, ext_id)
        self.select_school()
        self.select_first_grade()
        self.select_section()
        self.select_student_boy()
        self.add_student()


    """CREATE STUDENTS LINK"""
    def click_create_students_button(self):
        time.sleep(1)
        self.open_ems_iframe()
        self.wait_until_css_clickable("[class*='plus-icon']").click()
        self.app.driver.switch_to.default_content()

    def submit_student_full_name(self, first_name, last_name, ext_id):
        time.sleep(1)
        self.open_ems_iframe()
        add_first_name = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [1]")
        add_first_name.send_keys(first_name)
        add_last_name = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [2]")
        add_last_name.send_keys(last_name)
        add_ext_id = self.wait_until_xpath_clickable("(//input[contains(@class,'emsInput__input')]) [3]")
        add_ext_id.send_keys(ext_id)
        self.app.driver.switch_to.default_content()

    def select_school (self):
        self.open_ems_iframe()
        self.wait_until_id_clickable("emsForm__select--student-school").click()
        self.wait_until_css_clickable("[label='Test School']").click()
        self.app.driver.switch_to.default_content()

    def select_section(self):
        self.open_ems_iframe()
        self.wait_until_id_clickable("emsForm__select--student-section").click()
        self.wait_until_css_clickable("[label='Test - Section']").click()
        self.app.driver.switch_to.default_content()

    def select_student_girl(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-gender"))
        select_grade.select_by_value("F")
        self.app.driver.switch_to.default_content()

    def select_student_boy(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-gender"))
        select_grade.select_by_value("M")
        self.app.driver.switch_to.default_content()

    def add_student(self):
        self.open_ems_iframe()
        click_save_button = self.wait_until_css_clickable("[class*='emsStudentButton__save']")
        click_save_button.click()
        self.app.driver.switch_to.default_content()

    """SELECT GRADES"""
    def select_grade_toddler_time(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-grade"))
        select_grade.select_by_value("toddlertime")
        self.app.driver.switch_to.default_content()

    def select_grade_preschool(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-grade"))
        select_grade.select_by_value("preschool")
        self.app.driver.switch_to.default_content()

    def select_grade_prekindergarten(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-grade"))
        select_grade.select_by_value("preschool")
        self.app.driver.switch_to.default_content()

    def select_grade_kindergarten(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-grade"))
        select_grade.select_by_value("kindergarten")
        self.app.driver.switch_to.default_content()

    def select_first_grade(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-grade"))
        select_grade.select_by_value("1")
        self.app.driver.switch_to.default_content()

    def select_second_grade(self):
        self.open_ems_iframe()
        select_grade = Select(self.app.driver.find_element_by_id("emsForm__select--student-grade"))
        select_grade.select_by_value("2")
        self.app.driver.switch_to.default_content()

            ### kindergarten