

def test_01_create_free_teacher_account(app):
    # app.free_teacher.open_teacher_registration_page("https://www.abcmouse.com/teacher-registration") # Update URL QTEST!
    app.free_teacher.open_teacher_registration_page("https://bn.qtest.abcmouse.com/teacher-registration")  # Update URL QTEST!
    app.free_teacher.input_name(fname="AK Test", lname="(Free Teacher)")
    app.free_teacher.submit_email("ft1@bn.test")
    app.free_teacher.submit_confirm_password("test123")
    app.free_teacher.submit_district_info_fields(state_value="CA", school_district_value="Abc Unified School District")
    app.free_teacher.submit_school_info_fields(school_name="Test ABCMouse", address="LA Test", city="Los Angeles", zip="12345",
                              district="Test Abc Unified School District", phone="1111111111", superintendent="Dr. Alex (test)",
                              website="Test", other_info="Test")

    app.free_teacher.proceed_to_welcome_page()
    assert app.free_teacher.welcome_to_abcmouse_text("Welcome to ABCmouse.com!")

    app.free_teacher.proceed_to_survey_page()
    assert app.free_teacher.survey_title("Survey")

    app.free_teacher.proceed_to_step_1_create_teacher_account_page()
    assert app.free_teacher.step_1_title("Step 1: Create Teacher Account")

    app.free_teacher.step_1_create_teacher_account("AK Test (Free Teacher)")
    app.free_teacher.proceed_to_step_2_add_students()
    assert app.free_teacher.step_2_title("Step 2: Add Students")

    app.students.create_girl_toddler(name="St-1 (Girl)", birthday="03/2017")
    app.students.create_boy_toddler(name="St-2 (Boy)", birthday="07/2017")
    app.students.create_girl_preschool(name="St-3 (Girl)", birthday="01/2016")
    app.students.create_boy_preschool(name="St-4 (Boy)", birthday="05/2016")
    app.students.create_girl_pre_k(name="St-5 (Girl)", birthday="04/2015")
    app.students.create_boy_pre_k(name="St-6 (Boy)", birthday="06/2015")
    app.students.create_girl_kindergarten(name="St-7 (Girl)", birthday="08/2014")
    app.students.create_boy_kindergarten(name="St-8 (Boy)", birthday="05/2014")
    app.students.create_girl_first_grade(name="St-9 (Girl)", birthday="07/2013")
    app.students.create_boy_first_grade(name="St-10 (Boy)", birthday="02/2013")
    app.students.create_girl_second_grade(name="St-11 (Girl)", birthday="01/2012")
    app.students.create_boy_second_grade(name="St-12 (Boy)", birthday="05/2011")

    app.students.confirm_class_proceed_to_step_3()
    assert app.free_teacher.step_3_title("Step 3: Get Started on ABCmouse.com")

    app.free_teacher.proceed_to_abcmouse_page()
    assert app.free_teacher.teacher_image_icon
    assert app.free_teacher.teacher_welcome_title("Welcome, AK Test (Free Teacher)")




def test_02_free_teacher_login(app):
    app.free_teacher.open_teacher_login_page("https://dk.qtest.abcmouse.com/teachers")  # Update URL QTEST!
    app.login.to_free_teacher_account(email="ft001@dk.test", password="test123")

    # app.free_teacher.proceed_to_survey_page()
    assert app.free_teacher.survey_title("Survey")

    app.free_teacher.proceed_to_step_1_create_teacher_account_page()
    assert app.free_teacher.step_1_title("Step 1: Create Teacher Account")

    app.free_teacher.step_1_create_teacher_account("AK Test (Free Teacher)")
    app.free_teacher.proceed_to_step_2_add_students()
    assert app.free_teacher.step_2_title("Step 2: Add Students")

    app.students.create_girl_toddler(name="St-1 (Girl)", birthday="03/2017")
    app.students.create_boy_toddler(name="St-2 (Boy)", birthday="07/2017")
    app.students.create_girl_preschool(name="St-3 (Girl)", birthday="01/2016")
    app.students.create_boy_preschool(name="St-4 (Boy)", birthday="05/2016")
    app.students.create_girl_pre_k(name="St-5 (Girl)", birthday="04/2015")
    app.students.create_boy_pre_k(name="St-6 (Boy)", birthday="06/2015")
    app.students.create_girl_kindergarten(name="St-7 (Girl)", birthday="08/2014")
    app.students.create_boy_kindergarten(name="St-8 (Boy)", birthday="05/2014")
    app.students.create_girl_first_grade(name="St-9 (Girl)", birthday="07/2014")
    app.students.create_boy_first_grade(name="St-10 (Boy)", birthday="02/2014")
    app.students.create_girl_second_grade(name="St-11 (Girl)", birthday="01/2014")
    app.students.create_boy_second_grade(name="St-12 (Boy)", birthday="05/2014")

    app.students.confirm_class_proceed_to_step_3()
    assert app.free_teacher.step_3_title("Step 3: Get Started on ABCmouse.com")

    app.free_teacher.proceed_to_abcmouse_page()

    assert app.free_teacher.teacher_welcome_title(welcome_string="Welcome, AK Test (Free Teacher)")
    assert app.free_teacher.teacher_image_icon

