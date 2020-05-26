from selenium.webdriver.support.ui import WebDriverWait # Import at top of file
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_onboarding_process_gilr(app):
    app.onboarding.open_login_page("https://ay.qtest.abcmouse.com/login")
    app.login.to_abcmouse(email="gs5@ay.test", password="test123")

    # app.sign_up.click_submit_continue_registration_button()

    app.onboarding.welcome_page_click_get_started_button()
    app.onboarding.survey_click_continue_buttons()
    app.onboarding.input_parent_name(parent_first_name="AK Test", parent_family_name="Ko Test")

    ##### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
    app.onboarding.create_child_profile(child_name="Lilly (gs5)", gender="F", academic_level="preschool")

    app.onboarding.choose_avatar(avatar="girl_avatar09")  #####   |  boy_avatar03  |  girl_avatar03

    ####   |  hamster-1  |  hamster-2    #####   |  fish-1  |  fish-2
    app.onboarding.choose_hamster_and_fish(hamster="hamster-3", fish="fish-3", hamster_name="My Ham-StAr")
    app.onboarding.skip_video()
    app.onboarding.go_to_shp()



def test_onboarding_process_boy(app):
    app.onboarding.open_login_page("https://ay.qtest.abcmouse.com/login")
    app.login.to_abcmouse(email="gs05@ay.test", password="test123")

    # app.sign_up.click_submit_continue_registration_button()

    app.onboarding.welcome_page_click_get_started_button()
    app.onboarding.survey_click_continue_buttons()
    app.onboarding.input_parent_name(parent_first_name="AK Test", parent_family_name="Ko Test")

    ##### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
    app.onboarding.create_child_profile(child_name="Alex (pp02)", gender="M", academic_level="second-grade")

    app.onboarding.choose_avatar(avatar="boy_avatar09")  #####   |  boy_avatar07

    ####   |  hamster-1  |  hamster-2    #####   |  fish-1  |  fish-2
    app.onboarding.choose_hamster_and_fish(hamster="hamster-1", fish="fish-2", hamster_name="My Ham-StAr")
    app.onboarding.skip_video()
    app.onboarding.go_to_shp()





# def test_onboarding_process_gilr(app):
#     app.onboarding.open_login_page("https://ay.qtest.abcmouse.com/login")
#     app.login.to_abcmouse(email="pp01@ay.test", password="test123")
#
#     ###### ON-BOARDING PAGE
#     app.onboarding.welcome_page_click_get_started_button()
#     app.onboarding.survey_click_continue_buttons()
#     app.onboarding.input_parent_name(parent_first_name="AK Test", parent_family_name="Ko Test")
#     ###### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
#     app.onboarding.create_child_profile(child_name="Emmy (pp01)", gender="F", academic_level="pre-k")
#     app.onboarding.choose_avatar(avatar="girl_avatar15")  #####  girl_avatar01  |  girl_avatar16
#     app.onboarding.choose_hamster_and_fish(hamster="hamster-1", fish="fish-2", hamster_name="My Ham-StAr")
#     app.onboarding.skip_video()
#     app.onboarding.add_child()
#     ##### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
#     app.onboarding.create_child_profile(child_name="Tom", gender="M", academic_level="first-grade")
#     app.onboarding.choose_avatar(avatar="boy_avatar15")  #####   |  boy_avatar03  |  boy_avatar03
#     app.onboarding.choose_hamster_and_fish(hamster="hamster-3", fish="fish-4", hamster_name="My Ham-StAr")
#     app.onboarding.go_to_shp()
#     assert app.onboarding.mouse_pop_up()




# def test_onb_live(app):
#     app.onboarding.open_login_page("https://www.abcmouse.com/login")
#     app.login.to_abcmouse(email="sitetimer@live.test", password="test123")
#
#     ###### ON-BOARDING PAGE
#     app.sign_up.click_submit_continue_registration_button()
#     app.onboarding.welcome_page_click_get_started_button()
#     app.onboarding.survey_click_continue_buttons()
#     app.onboarding.input_parent_name(parent_first_name="AK Test", parent_family_name="Ko Test")
#     ##### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
#     app.onboarding.create_child_profile(child_name="B_1", gender="M", academic_level="first-grade")
#     app.onboarding.choose_avatar(avatar="boy_avatar03")  #####   |  boy_avatar03  |  girl_avatar03
#     app.onboarding.choose_hamster_and_fish(hamster="hamster-3", fish="fish-3", hamster_name="My Ham-StAr")
#     app.onboarding.skip_video()
#     app.onboarding.go_to_shp()
#     assert app.onboarding.mouse_pop_up()
#     assert app.driver.current_url == "https://www.abcmouse.com/html5#abc/student_home"