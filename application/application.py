from selenium import webdriver
from screen_pages.create_account_screen import CreateAccount
from screen_pages.onboarding_screen import Onboarding
from screen_pages.free_teacher_add_students_screen import FreeTeacherStudents
from screen_pages.login_screen import Login
from screen_pages.cc_information_screen import PaymentInformation
from screen_pages.free_teacher_screen import FreeTeacherScreen
from screen_pages.ems_teacher_screen import EmsTeacherScreen
from screen_pages.ems_teacher_add_students_screen import EmsStudents

class Application:
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(7)
        driver.maximize_window()


        self.sign_up = CreateAccount(self)
        self.onboarding = Onboarding(self)
        self.students = FreeTeacherStudents(self)
        self.ems_students = EmsStudents(self)
        self.login = Login(self)
        self.payment_info = PaymentInformation(self)
        self.free_teacher = FreeTeacherScreen(self)
        self.ems_teacher = EmsTeacherScreen(self)



