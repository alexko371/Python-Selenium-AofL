from screen_pages.base_screen import BaseScreen
import time

class Students(BaseScreen):

    def create_girl_toddler(self, name, birthday):
        self.student_name(name)
        self.toddler_time()
        self.student_girl()
        self.student_birthday(birthday)
        self.add_student()

    def create_boy_toddler(self, name, birthday):
        self.student_name(name)
        self.toddler_time()
        self.student_boy()
        self.student_birthday(birthday)
        self.add_student()

    def create_girl_preschool(self, name, birthday):
        self.student_name(name)
        self.preschool()
        self.student_girl()
        self.student_birthday(birthday)
        self.add_student()

    def create_boy_preschool(self, name, birthday):
        self.student_name(name)
        self.preschool()
        self.student_boy()
        self.student_birthday(birthday)
        self.add_student()

    def create_girl_pre_k(self, name, birthday):
        self.student_name(name)
        self.pre_k()
        self.student_girl()
        self.student_birthday(birthday)
        self.add_student()

    def create_boy_pre_k(self, name, birthday):
        self.student_name(name)
        self.pre_k()
        self.student_boy()
        self.student_birthday(birthday)
        self.add_student()

    def create_girl_kindergarten(self, name, birthday):
        self.student_name(name)
        self.kindergarten()
        self.student_girl()
        self.student_birthday(birthday)
        self.add_student()

    def create_boy_kindergarten(self, name, birthday):
        self.student_name(name)
        self.kindergarten()
        self.student_boy()
        self.student_birthday(birthday)
        self.add_student()

    def create_girl_first_grade(self, name, birthday):
        self.student_name(name)
        self.first_grade()
        self.student_girl()
        self.student_birthday(birthday)
        self.add_student()

    def create_boy_first_grade(self, name, birthday):
        self.student_name(name)
        self.first_grade()
        self.student_boy()
        self.student_birthday(birthday)
        self.add_student()

    def create_girl_second_grade(self, name, birthday):
        self.student_name(name)
        self.second_grade()
        self.student_girl()
        self.student_birthday(birthday)
        self.add_student()

    def create_boy_second_grade(self, name, birthday):
        self.student_name(name)
        self.second_grade()
        self.student_boy()
        self.student_birthday(birthday)
        self.add_student()


    def student_name(self, st_name):
        self.app.driver.find_element_by_id("students-name").send_keys(st_name)

    def student_birthday(self, st_birthday):
        self.app.driver.find_element_by_id("student-birthday").send_keys(st_birthday)

    def toddler_time(self, grade_level="div[data-value='0']"):
        self.app.driver.find_element_by_id("students-grade-select-button").click()
        self.app.driver.find_element_by_css_selector(grade_level).click()

    def preschool(self, grade_level="div[data-value='1']"):
        self.app.driver.find_element_by_id("students-grade-select-button").click()
        self.app.driver.find_element_by_css_selector(grade_level).click()

    def pre_k(self, grade_level="div[data-value='3']"):
        self.app.driver.find_element_by_id("students-grade-select-button").click()
        self.app.driver.find_element_by_css_selector(grade_level).click()

    def kindergarten(self, grade_level="div[data-value='5']"):
        self.app.driver.find_element_by_id("students-grade-select-button").click()
        self.app.driver.find_element_by_css_selector(grade_level).click()

    def first_grade(self, grade_level="div[data-value='7']"):
        self.app.driver.find_element_by_id("students-grade-select-button").click()
        self.app.driver.find_element_by_css_selector(grade_level).click()

    def second_grade(self, grade_level="div[data-value='9']"):
        self.app.driver.find_element_by_id("students-grade-select-button").click()
        self.app.driver.find_element_by_css_selector(grade_level).click()

    def student_girl(self):
        self.app.driver.find_element_by_id("students-gender-select-button").click()
        self.app.driver.find_element_by_css_selector("div[data-value='F']").click()

    def student_boy(self):
        self.app.driver.find_element_by_id("students-gender-select-button").click()
        self.app.driver.find_element_by_css_selector("div[data-value='M']").click()

    def add_student(self):
        self.app.driver.find_element_by_id("students-add-button").click()
        time.sleep(1)

    def confirm_class_proceed_to_step_3(self):
        # Add Student Next Button
        self.app.driver.find_element_by_id("add-students-next").click()
        self.app.driver.find_element_by_id("add-student-popup-next").click()