def test_01_create_ems_organization(app):
    """Update URL QTEST!"""
    app.ems_teacher.open_ems_teacher_registration_page("https://fa.qtest.abcmouse.com/admin")
    app.ems_teacher.login_to_ems()
    app.ems_teacher.navigate_to_organizations()
    assert app.ems_teacher.create_organizations_title("Create Organization")

    """Update Organization Name"""
    app.ems_teacher.create_organization(org_name="AK-1 fa.qtest")
    assert app.ems_teacher.organizations_name("AK-1 fa.qtest")


def test_02_create_ems_institution(app):
    """Update URL QTEST!"""
    app.ems_teacher.open_ems_teacher_registration_page("https://fa.qtest.abcmouse.com/admin")
    app.ems_teacher.login_to_ems()

    app.ems_teacher.select_my_organization()
    app.ems_teacher.click_institution_button()
    assert app.ems_teacher.institution_title("Institutions")

    app.ems_teacher.create_institution(inst_name="A.K. Test")


def test_03_create_ems_schools(app):
    app.ems_teacher.open_ems_teacher_registration_page("https://fa.qtest.abcmouse.com/admin")
    app.ems_teacher.login_to_ems()

    app.ems_teacher.select_my_organization()
    app.ems_teacher.click_institution_button()
    app.ems_teacher.select_my_institution()

    app.ems_teacher.select_schools()
    """Update School Name"""
    app.ems_teacher.create_school(school_name="Test School 1", ext_id="1")
    # assert app.ems_teacher.school_title("Schools")


def test_04_create_ems_sections(app):
    app.ems_teacher.open_ems_teacher_registration_page("https://fa.qtest.abcmouse.com/admin")
    app.ems_teacher.login_to_ems()

    app.ems_teacher.select_my_organization()
    app.ems_teacher.click_institution_button()
    app.ems_teacher.select_my_institution()

    app.ems_teacher.select_sections()
    app.ems_teacher.create_section("Test - Section", "1")


def test_05_create_ems_teachers(app):
    app.ems_teacher.open_ems_teacher_registration_page("https://fa.qtest.abcmouse.com/admin")
    app.ems_teacher.login_to_ems()

    app.ems_teacher.select_my_organization()
    app.ems_teacher.click_institution_button()
    app.ems_teacher.select_my_institution()
    app.ems_teacher.select_teachers()

    """ ALWAYS UPDATE EMAIL """
    app.ems_teacher.create_teachers(first_name="Alex(test)", last_name="Ko", ext_id="1",
                                    ems_email="ems001@fa.test")  ###### ALWAYS UPDATE EMAIL!!!

    app.ems_teacher.return_to_my_institution_details_page()


def test_001_create_ems_teacher_account(app):
    """Update URL QTEST!"""
    app.ems_teacher.open_ems_teacher_registration_page("https://fa.qtest.abcmouse.com/admin")
    app.ems_teacher.login_to_ems()
    # app.ems_teacher.navigate_to_organizations()
    # assert app.ems_teacher.create_organizations_title("Create Organization")
    #
    # """Update Organization Name"""
    # app.ems_teacher.create_organization(org_name="AK-1 fa.qtest")
    # # assert app.ems_teacher.organizations_name("AK fa.qtest")

    app.ems_teacher.select_my_organization()
    app.ems_teacher.click_institution_button()
    assert app.ems_teacher.institution_title("Institutions")

    app.ems_teacher.create_institution(inst_name="AK Test")
    app.ems_teacher.select_my_institution()
    app.ems_teacher.select_schools()
    assert app.ems_teacher.school_title()

    app.ems_teacher.create_school(school_name="Test School", ext_id="1")
    app.ems_teacher.return_to_my_institution_details_page()

    app.ems_teacher.select_sections()
    app.ems_teacher.create_section("Test - Section", "1")
    app.ems_teacher.return_to_my_institution_details_page()

    app.ems_teacher.select_teachers()

    """ ALWAYS UPDATE EMAIL """
    app.ems_teacher.create_teachers(first_name="Alex(test)", last_name="Ko", ext_id="1",
                                    ems_email="ems@fa.test")   ###### ALWAYS UPDATE EMAIL!!!

    app.ems_teacher.return_to_my_institution_details_page()

    app.ems_teacher.select_students()

    app.ems_students.create_ems_girl_toddler(first_name="Student", last_name="Toddler", ext_id="1")
    app.ems_students.create_ems_boy_toddler(first_name="Boy", last_name="Toddler", ext_id="01")
    app.ems_students.create_ems_girl_preschool(first_name="Girl", last_name="Preschool", ext_id="2")
    app.ems_students.create_ems_boy_preschool(first_name="Boy", last_name="Preschool", ext_id="02")
    app.ems_students.create_ems_girl_prekindergarten(first_name="Girl", last_name="Pre-K", ext_id="3")
    app.ems_students.create_ems_boy_prekindergarten(first_name="Boy", last_name="Pre-K", ext_id="03")

    app.ems_students.create_ems_girl_kindergarten(first_name="Girl", last_name="K", ext_id="4")
    app.ems_students.create_ems_boy_kindergarten(first_name="Boy", last_name="K", ext_id="04")

    app.ems_students.create_ems_girl_first_grade(first_name="Girl", last_name="1st G", ext_id="5")
    app.ems_students.create_ems_boy_first_grade(first_name="Boy", last_name="1st G", ext_id="05")

    app.ems_students.create_ems_girl_first_grade(first_name="Girl", last_name="2nd G", ext_id="6")
    app.ems_students.create_ems_boy_first_grade(first_name="Boy", last_name="2nd G", ext_id="06")

    app.ems_teacher.return_to_my_institution_details_page()





def test_002_create_ems_teacher_account(app):
    app.ems_teacher.open_ems_teacher_registration_page("https://fa.qtest.abcmouse.com/admin")   # Update URL QTEST!
    app.ems_teacher.login_to_ems()
    app.ems_teacher.navigate_to_organizations()
    assert app.ems_teacher.create_organizations_title("Create Organization")

    app.ems_teacher.select_my_organization()
    app.ems_teacher.click_institution_button()
    assert app.ems_teacher.institution_title("Institutions")

    # app.ems_teacher.create_institution(inst_name="AK Test 1")  #CREATE INSTITUTION
    app.ems_teacher.select_my_institution()

    app.ems_teacher.select_schools()
    assert app.ems_teacher.school_title("Schools")

    app.ems_teacher.create_school(school_name="Test School", ext_id="1")

    app.ems_teacher.return_to_my_institution_details_page()

    # app.ems_teacher.select_sections()
    # app.ems_teacher.create_section("Test - Section", "1")
    # app.ems_teacher.return_to_my_institution_details_page()

    app.ems_teacher.select_teachers()
    #### ALWAYS UPDATE EMAIL
    # app.ems_teacher.create_teachers(first_name="Alex(test)", last_name="Ko", ext_id="1", ems_email="ems1@fa.test") #### ALWAYS UPDATE EMAIL
    app.ems_teacher.return_to_my_institution_details_page()

    app.ems_teacher.select_students()
    ####### app.ems_students.click_create_students_button()

    app.ems_students.create_ems_girl_toddler(first_name="Student", last_name="Toddler", ext_id="1")
    app.ems_students.create_ems_boy_toddler(first_name="Boy", last_name="Toddler", ext_id="01")
    app.ems_students.create_ems_girl_preschool(first_name="Girl", last_name="Preschool", ext_id="2")
    app.ems_students.create_ems_boy_preschool(first_name="Boy", last_name="Preschool", ext_id="02")
    app.ems_students.create_ems_girl_prekindergarten(first_name="Girl", last_name="Pre-K", ext_id="3")
    app.ems_students.create_ems_boy_prekindergarten(first_name="Boy", last_name="Pre-K", ext_id="03")

    app.ems_students.create_ems_girl_kindergarten(first_name="Girl", last_name="K", ext_id="4")
    app.ems_students.create_ems_boy_kindergarten(first_name="Boy", last_name="K", ext_id="04")

    app.ems_students.create_ems_girl_first_grade(first_name="Girl", last_name="1st G", ext_id="5")
    app.ems_students.create_ems_boy_first_grade(first_name="Boy", last_name="1st G", ext_id="05")

    app.ems_students.create_ems_girl_first_grade(first_name="Girl", last_name="2nd G", ext_id="6")
    app.ems_students.create_ems_boy_first_grade(first_name="Boy", last_name="2nd G", ext_id="06")

    app.ems_teacher.return_to_my_institution_details_page()




    app.ems_teacher.navigate_to_organizations()

