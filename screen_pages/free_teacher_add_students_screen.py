from screen_pages.base_screen import BaseScreen
import time

class FreeTeacherStudents(BaseScreen):

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
        self.wait_until_id_clickable("students-name").send_keys(st_name)

    def student_birthday(self, st_birthday):
        self.wait_until_id_clickable("student-birthday").send_keys(st_birthday)

    def toddler_time(self, grade_level="div[data-value='0']"):
        self.wait_until_id_clickable("students-grade-select-button").click()
        self.wait_until_css_clickable(grade_level).click()

    def preschool(self, grade_level="div[data-value='1']"):
        self.wait_until_id_clickable("students-grade-select-button").click()
        self.wait_until_css_clickable(grade_level).click()

    def pre_k(self, grade_level="div[data-value='3']"):
        self.wait_until_id_clickable("students-grade-select-button").click()
        self.wait_until_css_clickable(grade_level).click()

    def kindergarten(self, grade_level="div[data-value='5']"):
        self.wait_until_id_clickable("students-grade-select-button").click()
        self.wait_until_css_clickable(grade_level).click()

    def first_grade(self, grade_level="div[data-value='7']"):
        self.wait_until_id_clickable("students-grade-select-button").click()
        self.wait_until_css_clickable(grade_level).click()

    def second_grade(self, grade_level="div[data-value='9']"):
        self.wait_until_id_clickable("students-grade-select-button").click()
        self.wait_until_css_clickable(grade_level).click()

    def student_girl(self):
        self.wait_until_id_clickable("students-gender-select-button").click()
        self.wait_until_css_clickable("div[data-value='F']").click()

    def student_boy(self):
        self.wait_until_id_clickable("students-gender-select-button").click()
        self.wait_until_css_clickable("div[data-value='M']").click()

    def add_student(self):
        self.wait_until_id_clickable("students-add-button").click()
        time.sleep(1)

    def confirm_class_proceed_to_step_3(self):
        # Add Student Next Button
        self.wait_until_id_clickable("add-students-next").click()
        self.wait_until_id_clickable("add-student-popup-next").click()
